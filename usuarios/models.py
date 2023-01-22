from django.db import models
from contatos.models import Contatos
from django import forms

class FormContato(forms.ModelForm):
    class Meta:
        model = Contatos
        exclude = {}