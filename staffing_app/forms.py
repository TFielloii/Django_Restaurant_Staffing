from django import forms

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
        self.fields['resume'].widget.attrs['rows'] = 5

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'location', 'description', 'requirements', 'salary']
    def __init__(self, *args, **kwargs):
        admin_loc = kwargs.pop('location')
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.filter(id=admin_loc.id)