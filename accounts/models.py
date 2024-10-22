from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    age = models.IntegerField(_('Возраст'), null=True, blank=True)