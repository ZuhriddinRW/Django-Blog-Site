from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User


class CustomUserCreationForm ( UserCreationForm ) :
    email = forms.EmailField ( required=True )
    first_name = forms.CharField ( max_length=25, required=False )
    last_name = forms.CharField ( max_length=25, required=False )
    phone_number = forms.CharField ( max_length=15, required=False )
    address = forms.CharField ( max_length=150, required=False )
    birth_date = forms.DateTimeField ( required=False )

    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'birth_date', 'password1',
                  'password2']

    def clean_email(self) :
        email = self.cleaned_data.get ( 'email' )
        if not email :
            raise forms.ValidationError ( "Email is required" )
        if User.objects.filter ( email=email ).exists () :
            raise forms.ValidationError ( "Email already exists" )
        return email

    def clean_username(self) :
        username = self.cleaned_data.get ( 'username' )
        if User.objects.filter ( username=username ).exists () :
            raise forms.ValidationError ( "Username already exists" )
        return username

    def save(self, commit=True) :
        user = super ().save ( commit=False )
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get ( 'first_name', '' )
        user.last_name = self.cleaned_data.get ( 'last_name', '' )
        user.phone_number = self.cleaned_data.get ( 'phone_number', '' )
        if commit :
            user.save ()
        return user


class CustomUserChangeForm ( UserChangeForm ) :
    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'birth_date', 'is_active',
                  'is_staff']


class SignUpForm ( UserCreationForm ) :
    email = forms.EmailField (
        required=True,
        widget=forms.EmailInput ( attrs={
            'placeholder' : 'you@example.com'
        } )
    )

    password1 = forms.CharField (
        label='Password',
        widget=forms.PasswordInput ( attrs={
            'placeholder' : '••••••••'
        } )
    )

    password2 = forms.CharField (
        label='Confirm Password',
        widget=forms.PasswordInput ( attrs={
            'placeholder' : '••••••••'
        } )
    )

    class Meta :
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username' : forms.TextInput ( attrs={
                'placeholder' : 'johndoe'
            } )
        }


class SignInForm ( AuthenticationForm ) :
    username = forms.CharField (
        widget=forms.TextInput ( attrs={
            'placeholder' : 'johndoe'
        } )
    )

    password = forms.CharField (
        widget=forms.PasswordInput ( attrs={
            'placeholder' : '••••••••'
        } )
    )