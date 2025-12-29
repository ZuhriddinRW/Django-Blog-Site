from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel ( models.Model ) :
    created_at = models.DateTimeField ( auto_now_add=True )
    updated_at = models.DateTimeField ( auto_now=True )

    class Meta :
        abstract = True


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager ( BaseUserManager ) :
    def create_user(self, username, email=None, password=None, **extra_fields) :
        if not username :
            raise ValueError ( 'Username is required!' )

        email = self.normalize_email ( email ) if email else None
        user = self.model ( username=username, email=email, **extra_fields )
        user.set_password ( password )
        user.save ( using=self._db )
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields) :
        extra_fields.setdefault ( 'is_staff', True )
        extra_fields.setdefault ( 'is_superuser', True )

        if extra_fields.get ( 'is_staff' ) is not True :
            raise ValueError ( "Superuser's property is_staff must be True" )
        if extra_fields.get ( 'is_superuser' ) is not True :
            raise ValueError ( "Superuser's property is_superuser must be True" )

        return self.create_user ( username, email, password, **extra_fields )


class User ( AbstractUser, PermissionsMixin ) :
    email = models.EmailField ( blank=True, null=True )
    age = models.PositiveIntegerField ( null=True, blank=True )
    phone_number = models.CharField ( unique=True, max_length=15, blank=True, null=True )

    objects = UserManager ()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) :
        return self.username