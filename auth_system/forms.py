from django import forms
from django.contrib.auth.forms import UserCreationForm
from auth_system.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  phone_number = forms.CharField(
    label="Номер телефону",
    widget=forms.TextInput(attrs={
      "class": "form-control",
      "placeholder": "Номер телефону"
    })
  )
  
  class Meta:
    model = CustomUser
    fields = ("username", "first_name", "last_name", "phone_number", "password1", "password2")



    