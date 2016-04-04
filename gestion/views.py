from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from gestion.models import Categorie, Formateur, Ressource
from .forms import LoginForm, UserRegistrationForm, CategorieForm, FormateurForm, RessourceForm


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
    template_name = "gestion/crud/create_categorie.html"


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


# CBV : Categorie
class ListeCategorie(ListView):
    model = Categorie
    context_object_name = "derniers_articles"
    template_name = "gestion/dash_admin_categorie.html"


class CreateCategorie(CreateView):
    model = Categorie
    template_name = "gestion/categorie_create_form.html"
    form_class = CategorieForm
    success_url = reverse_lazy('gestion:dash_categorie')

    def form_valid(self, form):
        categorie = form.save(commit=False)
        categorie.administrateur = self.request.user.administrateur
        return super(CreateCategorie, self).form_valid(form)


class UpdateCategorie(UpdateView):
    model = Categorie
    template_name = "gestion/categorie_update_form.html"
    form_class = CategorieForm
    success_url = reverse_lazy(HomeView)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_categorie')


class DeleteCategorie(DeleteView):
    model = Categorie
    context_object_name = "categorie"
    template_name = "gestion/categorie_delete.html"
    success_url = reverse_lazy('gestion:dash_categorie')


# CBV : Formateur
class ListeFormateur(ListView):
    model = Formateur
    context_object_name = "derniers_articles"
    template_name = "gestion/dash_admin_formateur.html"


class CreateFormateur(CreateView):
    model = Formateur
    template_name = "gestion/formateur_create_form.html"
    form_class = FormateurForm
    success_url = reverse_lazy('gestion:dash_formateur')

    def form_valid(self, form):
        categorie = form.save(commit=False)
        categorie.administrateur = self.request.user.administrateur
        return super(CreateFormateur, self).form_valid(form)


class UpdateFormateur(UpdateView):
    model = Formateur
    template_name = "gestion/formateur_update_form.html"
    form_class = RessourceForm
    success_url = reverse_lazy('gestion:dash_formateur')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_formateur')


class DeleteFormateur(DeleteView):
    model = Formateur
    context_object_name = "formateur"
    template_name = "gestion/formateur_delete.html"
    success_url = reverse_lazy('gestion:dash_formateur')


# CBV : Formateur
class ListeRessource(ListView):
    model = Ressource
    context_object_name = "derniers_articles"
    template_name = "gestion/dash_formateur_ressource.html"


class CreateRessource(CreateView):
    model = Ressource
    template_name = "gestion/ressource_create_form.html"
    form_class = RessourceForm
    success_url = reverse_lazy('gestion:dash_ressource')

    def form_valid(self, form):
        categorie = form.save(commit=False)
        categorie.administrateur = self.request.user.administrateur
        return super(CreateRessource, self).form_valid(form)


class UpdateRessource(UpdateView):
    model = Ressource
    template_name = "gestion/ressource_update_form.html"
    form_class = RessourceForm
    success_url = reverse_lazy('gestion:dash_ressource')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_ressource')


class DeleteRessource(DeleteView):
    model = Ressource
    context_object_name = "ressource"
    template_name = "gestion/ressource_delete.html"
    success_url = reverse_lazy('gestion:dash_ressource')
