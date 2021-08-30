from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class extrafield(models.Model):
    address = models.TextField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extrafield')

    def __str__(self):
        return self.user.username