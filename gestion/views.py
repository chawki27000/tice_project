from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from gestion.models import Categorie
from .forms import LoginForm, UserRegistrationForm
from django.views.generic import TemplateView, ListView


# CBV TempleteView :
class ConsultationView(TemplateView):
    template_name = "gestion/dash_apprenant_consul.html"


class RessourceView(TemplateView):
    template_name = "gestion/dash_formateur_ressource.html"


class RegroupView(TemplateView):
    template_name = "gestion/dash_formateur_regroup.html"


class TesteView(TemplateView):
    template_name = "gestion/dash_formateur_teste.html"


class FormateurView(TemplateView):
    template_name = "gestion/dash_admin_formateur.html"


class CategrieView(TemplateView):
    template_name = "gestion/dash_admin_categorie.html"


class HomeView(TemplateView):
    template_name = "base.html"


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'gestion/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'gestion/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'gestion/register.html', {'user_form': user_form})


# CBV : tmp
class ListeCategorie(ListView):
    model = Categorie
    context_object_name = "derniers_articles"
    template_name = "gestion/dash_admin_categorie.html"
