from django.db import models
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(_('date of birth'))
    phone_number = models.CharField(_('phone number'), max_length=12)


class UpdateProfile(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'image', 'url', 'biography', '...'] # Keep listing whatever fields 
    # the combined UserProfile and User exposes.
    template_name = 'user_update.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'