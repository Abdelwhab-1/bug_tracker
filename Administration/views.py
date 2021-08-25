from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import Group 
from authinticator.models import Profile
from django.views.generic import FormView, UpdateView, CreateView, DeleteView
from operation.models import Project
from .forms import RolesManager
from .mixins import OwnerOnlyUpdateMixin
# Create your views here.

class ManageRoles(PermissionRequiredMixin, FormView):  
    permission_required = 'authinticator.can_manage_roles'
    form_class = RolesManager
    template_name = 'administration/manage_roles.html'
    success_url = reverse_lazy('administration:manage_roles')
        

    # TODO: retreive all the user and and their roles. 
    def form_valid(self, form): 
        profiles = form.cleaned_data.get('users')
        role = form.cleaned_data['role']
        # check to see if the user is admin or not 
        if role == "Admins" and 'Admins' not in [group.name for group in self.request.user.groups.all() ]: 
            error = ValidationError('You are not Admin to assign Admin roles to users.')
            form.add_error('role', error)
            return super().form_invalid(form)
            
        group = Group.objects.get_by_natural_key(role)

        # Add every user to the spesefied group by the admin 
        for profile in profiles: 
            user = Profile.objects.get(id=profile)
            user.user.groups.add(group)
            user.user.save()
            return super().form_valid(form)
        

    def get_success_url(self): 
        return reverse_lazy('administration:manage_roles')


class CreateProject(PermissionRequiredMixin,CreateView):
    permission_required = 'authinticator.can_manage_roles'
    model = Project
    template_name = 'administration/create_project.html'
    fields = ['title', 'descreption', 'url', 'developers', 'project_manager', 'image']

    def get_success_url(self): 
        return reverse_lazy('operation:projects')


class UpdateProject(PermissionRequiredMixin,UpdateView):
    permission_required = 'authinticator.can_manage_roles'
    model = Project
    template_name = 'administration/update_project.html'
    fields = ['title', 'descreption', 'url', 'developers', 'project_manager', 'image']
    
    
    def get_success_url(self): 
        return reverse_lazy('operation:project_details', kwargs={'pk':self.object.id})


    def get_form(self, form_class=None):
        form = super().get_form( form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        return form 

class DeletProject(PermissionRequiredMixin, DeleteView):
    permission_required = 'authinticator.can_manage_roles'
    model = Project 
    success_url = reverse_lazy('authinticator:projects')
    template_name = 'delete_project.html'
    
 