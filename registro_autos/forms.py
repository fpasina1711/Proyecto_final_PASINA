from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class Formturno(forms.ModelForm):

    class Meta:
        model=Turno
        fields=('__all__')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=50 ,required=True)
    first_name = forms.CharField(max_length=50 ,required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

class UserEditForm(UserChangeForm):
   
  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model=User
    fields=('email', 'first_name', 'last_name', 'password1', 'password2')

  def clean_password2(self):

    print(self.cleaned_data)

    password2 = self.cleaned_data["password2"]
    if password2 != self.cleaned_data["password1"]:
      raise forms.ValidationError("Las contraseñas no coinciden!")
    return password2
