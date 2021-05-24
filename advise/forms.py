from django import forms
from .api import choice

moedas = choice


class MoedaForm(forms.Form):
    coin_origin = forms.ChoiceField(choices=moedas)
    coin_destiny = forms.ChoiceField(choices=moedas)
