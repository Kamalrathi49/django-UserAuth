from django.db import models
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    full_name = models.CharField(_('full name'), max_length=150)
    profession = models.CharField(_('profession'), max_length=150)
    address = models.CharField(_('address'), max_length=150)
    image = models.ImageField(_('image'), blank=True, null=True, upload_to="images/")
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=12)


