from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'})
    )
    # phone_num = forms.IntegerField(widget=forms.NumberInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Enter your phone number'
    # })
# )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('user_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        # phone_num = cleaned_data.get('phone_num')

        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose a different one.")

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered. Please use a different email address.")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        # if phone_num and len(str(phone_num)) != 10:
        #     raise forms.ValidationError("Phone number must be exactly 10 digits!")

        return cleaned_data


class SigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password.")
            self.user = user  # Save the user
        return cleaned_data
