from django import forms
from post import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Coment
        fields = ('coment',)

class CreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'thumbnail',
            'title',
            'content',
            'slug',
            'autor',
        ]