from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import Azucar, Vegano, GlutenFree

# Formulario de Registro de Usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Formulario de Inicio de Sesión
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


# Formulario para ingresar una producto sin azucar
class AzucarForm(forms.ModelForm):
    class Meta:
        model = Azucar  # Asegúrate de que este sea el nombre correcto de tu modelo
        fields = ['nombre_producto', 'nombre_comercio', 'descripcion', 'fecha_subida', 'precio']  # Campos que quieres incluir


class VeganoForm(forms.ModelForm):
    class Meta:
        model = Vegano  # Asegúrate de que este sea el nombre correcto de tu modelo
        fields = ['nombre_producto', 'nombre_comercio', 'descripcion', 'fecha_subida', 'precio']  # Campos que quieres incluir

class GlutenFreeForm(forms.ModelForm):
    class Meta:
        model = GlutenFree  # Asegúrate de que este sea el nombre correcto de tu modelo
        fields = ['nombre_producto', 'nombre_comercio', 'descripcion', 'fecha_subida', 'precio']  # Campos que quieres incluir


class BuscarProductoForm(forms.Form):
    query = forms.CharField(label='Buscar producto', max_length=100)