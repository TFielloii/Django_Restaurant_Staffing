from django import forms

from .models import Application, JobPosting, Location, Restaurant

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
        admin_loc = kwargs.pop('restaurant')
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.filter(restaurant=admin_loc)

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['address','city','state','restaurant']
    def __init__(self, *args, **kwargs):
        admin_loc = kwargs.pop('restaurant')
        super().__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(name=admin_loc)