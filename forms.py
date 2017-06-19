from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Profile2, Friend, Applicant2


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ['bio','location','profile_image']


class ProfileForm2(forms.ModelForm):
    class Meta:

        model = Profile2
        fields = ['name', 'University', 'Country']


class InternForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['skills_needed','Description', 'other_info']


class Cover(forms.ModelForm):
    class Meta:
        model = Applicant2
        exclude = ('prof', 'user', 'user2')


