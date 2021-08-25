from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, FormView
from authinticator.models import User, Profile
from .models import Project, Ticket, Comment 
from .forms import TicketFile, ProfileForm
from Administration.mixins import OwnerOnlyUpdateMixin
from django.urls import reverse_lazy
from .mixins import DemoNoSave
# Create your views here.
class ProjectsView(LoginRequiredMixin ,ListView):
    model = Project
    template_name = 'operation/projects.html'
    paginate_by = 3
    ordering = ['title']


    def get(self, request, *args, **kwargs):
        return super().get(request=request)


class ProjectView(LoginRequiredMixin, DetailView):
    model = Project 
    template_name = 'operation/single_project.html'


class UserProjects(ListView):
    model = User
    template_name = 'operation/my_projects.html'
    paginate_by = 3 
    def get_queryset(self): 
        return self.request.user.project_set.all()


class TicketView(DetailView):
    model = Ticket
    template_name = 'operation/single_ticket.html'


    def post(self, request, *args, **kwargs): 
        self.request = request 
        self.user = request.user 
        self.model = Comment 

        comment = Comment(owner=self.user, project=Ticket.objects.get(id=self.kwargs['pk']), body=request.POST['comment'])
        comment.save()
        return redirect(reverse_lazy('operation:view_ticket', kwargs={'pk':self.kwargs['pk']}))


class CreateTicket(DemoNoSave, LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'operation/create_ticket.html'
    form_class = TicketFile


    def form_valid(self, form): 
        owner = self.request.user 
        project = Project.objects.get(id=self.kwargs['pk'])
        ticket = form.back_door_save(commit=False, owner=owner, project=project)
        return super().form_valid(form)


    def get_success_url(self): 
        return reverse_lazy('operation:view_ticket', kwargs={'pk':self.object.id})


class UserTickets(LoginRequiredMixin, ListView): 

    model = Ticket 
    template_name = 'operation/my_tickets.html'
    paginate_by = 3 
    def get_queryset(self): 
        return self.request.user.ticket_set.all()


class TicketUpdate(DemoNoSave, OwnerOnlyUpdateMixin, UpdateView):
    model = Ticket 
    fields = ['body', 'title', 'kind', 'priority']
    template_name = 'operation/update_ticket.html'
    

    def get_form_class(self): 
        self.object = self.get_object()
        group = Group.objects.get(name="Admins")
        if group in self.request.user.groups.all() or self.object.project.project_manager == self.request.user: 

            if self.object.owner == self.request.user:
                self.fields.append("assigned_developer")
                return super().get_form_class()


            self.fields = ["assigned_developer"]
            return super().get_form_class()
        
        return super().get_form_class()
        

    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        return form 


    def get_success_url(self): 
        return reverse_lazy('operation:view_ticket', kwargs={"pk": self.kwargs['pk']})


class ProfileUpdate(DemoNoSave,LoginRequiredMixin, FormView):
    model = Profile 
    form_class = ProfileForm
    template_name = "operation/profile.html"

    def get_form(self, form_class=None):
        
        if not form_class:
            form_class = self.get_form_class()
        return form_class(instance=self.get_object(), **self.get_form_kwargs())

    def form_valid(self, form): 
        self.obj = form.save()
        self.obj.user.email = form.cleaned_data["email"]
        self.obj.user.save()
        return super().form_valid(form)


    def get_object(self): 
        self.obj = self.request.user.profile
        return self.obj


    def get_success_url(self): 
        return reverse_lazy('operation:view_profile', kwargs={"pk": self.obj.id})


class ViewProfile(DeleteView):
    model = Profile 
    template_name = "operation/view_profile.html"
