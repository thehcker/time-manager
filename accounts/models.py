from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	is_user = models.BooleanField(default=False)
	is_user_manager = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
