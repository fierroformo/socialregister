# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = CustomUserManager.normalize_email(email)
        user = self.model(
            email=email, username=email, first_name=first_name,
            last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        u = self.create_user(email, first_name, last_name, password)
        u.is_admin = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, verbose_name=u"nombre(s)")
    last_name = models.CharField(max_length=50, verbose_name=u"apellidos")
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name)
