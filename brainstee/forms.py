from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Seek,Help,Idea


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pro_photo','email','bio','location')

class SeekForm(forms.ModelForm):
    class Meta:
        model = Seek
        exclude =  []
        fields = ['what_do_you_do','which_skills_do_you_have','seek_help']

class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        exclude =  []
        fields = ['helpout',]

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude =  []
        fields = ['idea',]