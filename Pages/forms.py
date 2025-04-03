from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class LoginForm(forms.Form):
    DOCUMENT_CHOICES = [
        ('DNI', 'DNI'),
        ('CE', 'Carné de Extranjería'),
    ]

    tipo_documento = forms.ChoiceField(choices=DOCUMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    numero_documento = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu número de documento'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu contraseña'}))
