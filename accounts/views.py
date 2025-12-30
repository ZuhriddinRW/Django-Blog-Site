from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, SignInForm


def sign_up(request) :
    if request.user.is_authenticated :
        return redirect ( 'home' )

    if request.method == 'POST' :
        form = SignUpForm ( request.POST )
        if form.is_valid () :
            user = form.save ()
            login ( request, user )
            messages.success ( request, 'Account created successfully!' )
            return redirect ( 'home' )
        else :
            for field, errors in form.errors.items () :
                for error in errors :
                    messages.error ( request, f'{field}: {error}' )
    else :
        form = SignUpForm ()

    return render ( request, 'Authentication/signup.html', {'form' : form} )


def sign_in(request) :
    if request.user.is_authenticated :
        return redirect ( 'home' )

    if request.method == 'POST' :
        form = SignInForm ( request, data=request.POST )
        if form.is_valid () :
            username = form.cleaned_data.get ( 'username' )
            password = form.cleaned_data.get ( 'password' )
            user = authenticate ( username=username, password=password )

            if user is not None :
                login ( request, user )
                remember_me = request.POST.get ( 'remember-me' )
                if not remember_me :
                    request.session.set_expiry ( 0 )  # Session expires on browser close
                messages.success ( request, f'Welcome back, {username}!' )
                return redirect ( 'home' )
        else :
            messages.error ( request, 'Invalid username or password.' )
    else :
        form = SignInForm ()

    return render ( request, 'Authentication/signin.html', {'form' : form} )


def sign_out(request) :
    logout ( request )
    messages.success ( request, 'You have been logged out successfully.' )
    return redirect ( 'signin' )


@login_required
def home(request) :
    return render ( request, 'home.html' )