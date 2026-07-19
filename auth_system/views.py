from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from auth_system.forms import CustomUserCreationForm

def register_view(request):
  if request.method == 'GET':
    register_form = CustomUserCreationForm()
  else:
    register_form = CustomUserCreationForm(request.POST)
    if register_form.is_valid():
      user = register_form.save()
      login(request, user)
      return redirect('houses-list')
    
  context = {
    "register_form": register_form
  }

  return render(
    request,
    "auth_system/register.html",
    context
    )

def login_view(request):
  if request.method == 'GET':
    login_form = AuthenticationForm()
  else:
    login_form = AuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
      user = login_form.get_user()
      login(request, user)
      return redirect('houses-list')
    else:
      messages.error(request, "Невірний логін або пароль")

  context = {
    "login_form": login_form
  }

  return render(
    request,
    "auth_system/login.html",
    context
    )


def logout_view(request):
  pass
