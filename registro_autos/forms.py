from django import forms
from .models import *

class Formturno(forms.ModelForm):

    class Meta:
        model=Turno
        fields=('__all__')

