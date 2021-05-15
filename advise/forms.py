from django import forms
from django.forms.fields import ChoiceField
from django.utils.regex_helper import Choice
from .api import choice

moedas = choice


class MoedaForm(forms.Form):
    coin_origin = forms.ChoiceField(choices=moedas)
    coin_destiny = forms.ChoiceField(choices=moedas)
