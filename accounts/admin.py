from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin ( UserAdmin ) :
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']

    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
        ('Personal info',
         {'fields' : ('first_name', 'last_name', 'email', 'phone_number', 'address', 'birth_date', 'age')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields' : ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2',
                        'is_staff', 'is_active')
        }),
    )

    search_fields = ['username', 'email']
    ordering = ['username']


admin.site.register ( User, CustomUserAdmin )