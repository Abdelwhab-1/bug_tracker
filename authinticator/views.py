from django.shortcuts import render, redirect
from django import forms 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.forms import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group 
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, User
from .forms import SignUPForm
# Create your views here.



class Index(TemplateView):
    template_name = 'index.html'


class SignUp(FormView):
    template_name = 'registration/register.html'
    form_class = SignUPForm
    success_url = reverse_lazy('lgoin')
    user = get_user_model() 
    profile = Profile

    def create(self, form):

        user = self.user.objects.create_user(email=form.cleaned_data['email'], 
            password=form.cleaned_data['password1'])

        
        profile = self.profile.objects.create(user=user, first_name=form.cleaned_data['first_name'], 
            last_name=form.cleaned_data['last_name'])

        return profile  
    
    def get_success_url(self): 
        return reverse_lazy('authinticator:login')

        
    def form_valid(self, form):
        self.create(form)
        return super().form_valid(form)






