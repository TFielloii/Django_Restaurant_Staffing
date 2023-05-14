from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import get_user_model

from staffing_app.models import Location, Restaurant
from .models import CustomUser

# User registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    # Overrides the save() method to set email field.
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rename username field to email field.
        self.fields['username'] = self.fields.pop('username', self.fields.get('email'))
        self.fields['username'].widget.attrs.update({'autofocus': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

        # Reorders the fields.
        self.fields['password'].widget.order = 1
        self.fields['username'].widget.order = 0
        self.order_fields(['username','password'])

# User update form.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length = 200)
    class Meta:
        model = get_user_model()
        fields = ['email','first_name','last_name']

# Set password form.
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

# Custom user creation form.
class CustomUserCreationForm(UserCreationForm):
    restaurant = forms.ModelChoiceField(Restaurant.objects.all(), required=False)
    location = forms.ModelChoiceField(Location.objects.all(), required=False)
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_hiring_manager', 'is_restaurant_administrator', 'restaurant', 'location')
    
    # Overrides the clean() method to check for required location field for certain user types.
    def clean(self):
        cleaned_data = super().clean()
        is_hiring_manager = cleaned_data.get('is_hiring_manager')
        is_restaurant_administrator = cleaned_data.get('is_restaurant_administrator')
        if is_hiring_manager and is_restaurant_administrator:
            raise forms.ValidationError('Users can be an administrator or manager, but not both.')
        if is_restaurant_administrator:
            restaurant = cleaned_data.get('restaurant')
            if not restaurant:
                raise forms.ValidationError('A restaurant is required for administrators.')
        if is_hiring_manager:
            location = cleaned_data.get('location')
            if not location:
                raise forms.ValidationError('A location is required for hiring managers.')

# Custom user change form.
class CustomUserChangeForm(UserChangeForm):
    restaurant = forms.ModelChoiceField(Restaurant.objects.all(), required=False)
    location = forms.ModelChoiceField(Location.objects.all(), required=False)
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_hiring_manager', 'is_restaurant_administrator', 'restaurant', 'location')
    
    # Overrides the clean() method to check for required location field for certain user types.
    def clean(self):
        cleaned_data = super().clean()
        is_hiring_manager = cleaned_data.get('is_hiring_manager')
        is_restaurant_administrator = cleaned_data.get('is_restaurant_administrator')
        if is_restaurant_administrator:
            restaurant = cleaned_data.get('restaurant')
            if not restaurant:
                raise forms.ValidationError('A restaurant is required for administrators.')
        if is_hiring_manager:
            location = cleaned_data.get('location')
            if not location:
                raise forms.ValidationError('A location is required for hiring managers.')