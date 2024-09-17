from django import forms
from .models import Profile, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'description', 'email', 'phone', 'skill']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skill', 'url']
