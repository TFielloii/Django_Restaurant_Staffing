from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('email', 'resume')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'resume': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].label = 'Resume/CV'
        self.fields['email'].label = 'Email'
        self.fields['resume'].widget.attrs['rows'] = 5

class ApplicantCreationForm(UserCreationForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'password1', 'password2']