from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise TypeError(_('Superuser must be assigned to is_staff=True.'))
        if other_fields.get('is_superuser') is not True:
            raise TypeError(_('Superuser must be assigned to is_superuser=True.'))
        if password is None:
            raise TypeError(_('You must provide a password '))
        if not user_name:
            raise TypeError(_('You must provide an username'))
        if not email:
            raise TypeError(_('You must provide an email address'))

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not user_name:
            raise TypeError(_('You must provide an username'))
        if not email:
            raise TypeError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True, db_index=True)
    user_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email
