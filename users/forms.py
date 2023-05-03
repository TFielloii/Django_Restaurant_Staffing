from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from staffing_app.models import Location

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = self.fields.pop('username', self.fields.get('email'))
        self.fields['username'].widget.attrs.update({'autofocus': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        # Reorder the fields
        self.fields['password'].widget.order = 1
        self.fields['username'].widget.order = 0
        # Update the rendering order of the fields
        self.order_fields(['username','password'])

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length = 200)
    class Meta:
        model = get_user_model()
        fields = ['email','first_name','last_name']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class CustomUserCreationForm(UserCreationForm):
    location = forms.ModelChoiceField(Location.objects.all(), required=False)
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_hiring_manager', 'is_restaurant_administrator', 'location')
    def clean(self):
        cleaned_data = super().clean()
        is_hiring_manager = cleaned_data.get('is_hiring_manager')
        is_restaurant_administrator = cleaned_data.get('is_restaurant_administrator')
        location = cleaned_data.get('location')
        if (is_hiring_manager or is_restaurant_administrator) and not location:
            raise forms.ValidationError('Location is required for hiring managers and restaurant administrators.')

class CustomUserChangeForm(UserChangeForm):
    location = forms.ModelChoiceField(Location.objects.all(), required=False)
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_hiring_manager', 'is_restaurant_administrator', 'location')
    def clean(self):
        cleaned_data = super().clean()
        is_hiring_manager = cleaned_data.get('is_hiring_manager')
        is_restaurant_administrator = cleaned_data.get('is_restaurant_administrator')
        location = cleaned_data.get('location')
        if (is_hiring_manager or is_restaurant_administrator) and not location:
            raise forms.ValidationError('Location is required for hiring managers and restaurant administrators.')