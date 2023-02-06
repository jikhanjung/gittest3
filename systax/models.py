from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(_('email address'),unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(default=timezone.now)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    def __str__(self):
        return self.email

class Taxon(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
