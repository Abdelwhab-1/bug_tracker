from django import forms 
from authinticator.models import Profile
from django.contrib.auth.models import Group

def get_all_profiles(profile):
        
        all_profiles = profile.objects.all()
        profile_choices = []
        for Profile in all_profiles: 
            profile_choices.append((Profile.id, Profile.full_name))
        return profile_choices

def get_all_roles(gruop):
    all_groups = Group.objects.all()
    group_choices = []
    for group in all_groups: 
        group_choices.append((group.name, group.name))
    return group_choices


class RolesManager(forms.Form):

    users = forms.MultipleChoiceField(required=True ,choices=get_all_profiles(Profile))
    role = forms.CharField(required=True,widget=forms.Select(choices= get_all_roles(Group)))
