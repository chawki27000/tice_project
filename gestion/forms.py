from django import forms

from gestion.models import Categorie, Formateur, Ressource, Apprenant
from tice_project.users.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('lib_categ',)


class FormateurForm(forms.ModelForm):
    class Meta:
        model = Formateur
        fields = ('user', 'spec_formation', 'type_formation',)


class ApprenantForm(forms.ModelForm):
    class Meta:
        model = Apprenant
        fields = ('user', 'grade_util', 'diplome_appr', 'formation',)


class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ('lib_ress', 'type_ress', 'chapitre',)
