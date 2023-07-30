from django import forms


class BuenoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    sexo = forms.CharField(required=True, max_length=9)
    bio = forms.CharField(required=True, max_length=256)

class NeutralFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    sexo = forms.CharField(required=True, max_length=9)
    bio = forms.CharField(required=True, max_length=256)

class MaloFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    sexo = forms.CharField(required=True, max_length=9)
    bio = forms.CharField(required=True, max_length=256)

