from django import forms

class BuscarUsuarioForm(forms.Form):
    username = forms.CharField()