from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget

from App_Components.models import Blog

class BuscarUsuarioForm(forms.Form):
    username = forms.CharField()

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=40)
    surname = forms.CharField(max_length=40)
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=CKEditorWidget())
    website = forms.CharField(max_length=100)

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField(required=False)

    class Meta:
        model = Blog
        fields = ["title", "content", "image"]
        widgets = {
            'content': CKEditorWidget()
        }

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Correo', help_text='Es necesario que sea menor a 150 caracteres')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { key: '' for key in fields }

