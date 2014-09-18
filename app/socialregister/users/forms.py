# -*- coding: utf-8 -*-
from django import forms
from socialregister.users.models import User


class CompleteDataForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        if not 'password' in self.cleaned_data:
            raise forms.ValidationError("Enter a password.")
        elif not 'confirm_password' in self.cleaned_data:
            raise forms.ValidationError("Enter your password (again)")
        elif self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email", "password"]
        widgets = {'password': forms.PasswordInput()}
