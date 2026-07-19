from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  phone_number = models.CharField(max_length=15, unique=True, verbose_name="Phone number")

  def __str__(self):
    return f"{self.last_name} {self.first_name} - {self.phone_number}"