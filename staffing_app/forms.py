from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('resume',)
        widgets = {
            'resume': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].label = 'Resume/CV'
        self.fields['email'].label = 'Email'
        self.fields['resume'].widget.attrs['rows'] = 5