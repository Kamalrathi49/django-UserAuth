from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    address = models.TextField(_('address'))

# class extrafield(models.Model):
#     address = models.TextField(max_length=100)
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='extrafield')

#     def __str__(self):
#         return self.user.username

