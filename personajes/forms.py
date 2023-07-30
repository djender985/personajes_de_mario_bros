from django import forms


class BuenoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    sexo = forms.CharField(required=True, max_length=9)
    bio = forms.CharField(widget=forms.Textarea)

class NeutralFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    sexo = forms.CharField(required=True, max_length=9)
    bio = forms.CharField(widget=forms.Textarea)

class MaloFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    sexo = forms.CharField(required=True, max_length=9)
    bio = forms.CharField(widget=forms.Textarea)

