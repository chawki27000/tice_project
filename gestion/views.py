from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .forms import ChapitreForm, AnimerForm, RegroupementForm, TestForm, CoursForm
from .forms import LoginForm, UserRegistrationForm, CategorieForm, FormateurForm, RessourceForm, ApprenantForm
from .serializers import *
from .models import *


# CBV TempleteView :

class RessourceView(TemplateView):
    template_name = "gestion/formateur/dash_formateur_ressource.html"


class RegroupView(TemplateView):
    template_name = "gestion/formateur/dash_formateur_regroup.html"


class TesteView(TemplateView):
    template_name = "gestion/formateur/dash_formateur_test.html"


class FormateurView(TemplateView):
    template_name = "gestion/admin/dash_admin_formateur.html"


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


##########################################################################################

# CBV : Categorie
class ListeCategorie(ListView):
    model = Categorie
    context_object_name = "derniers_articles"
    template_name = "gestion/admin/dash_admin_categorie.html"


class CreateCategorie(CreateView):
    model = Categorie
    template_name = "gestion/admin/categorie_create_form.html"
    form_class = CategorieForm
    success_url = reverse_lazy('gestion:dash_categorie')

    def form_valid(self, form):
        categorie = form.save(commit=False)
        categorie.administrateur = self.request.user.administrateur
        return super(CreateCategorie, self).form_valid(form)


class UpdateCategorie(UpdateView):
    model = Categorie
    template_name = "gestion/admin/categorie_update_form.html"
    form_class = CategorieForm
    success_url = reverse_lazy(HomeView)

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_categorie')


class DeleteCategorie(DeleteView):
    model = Categorie
    context_object_name = "categorie"
    template_name = "gestion/admin/categorie_delete.html"
    success_url = reverse_lazy('gestion:dash_categorie')


# CBV : Formateur
class ListeFormateur(ListView):
    model = Formateur
    context_object_name = "derniers_articles"
    template_name = "gestion/admin/dash_admin_formateur.html"


class CreateFormateur(CreateView):
    model = Formateur
    template_name = "gestion/admin/formateur_create_form.html"
    form_class = FormateurForm
    success_url = reverse_lazy('gestion:dash_formateur')

    def form_valid(self, form):
        categorie = form.save(commit=False)
        categorie.administrateur = self.request.user.administrateur
        return super(CreateFormateur, self).form_valid(form)


class UpdateFormateur(UpdateView):
    model = Formateur
    template_name = "gestion/admin/formateur_update_form.html"
    form_class = RessourceForm
    success_url = reverse_lazy('gestion:dash_formateur')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_formateur')


class DeleteFormateur(DeleteView):
    model = Formateur
    context_object_name = "formateur"
    template_name = "gestion/admin/formateur_delete.html"
    success_url = reverse_lazy('gestion:dash_formateur')


# CBV : Ressource
class ListeRessource(ListView):
    model = Ressource
    context_object_name = "derniers_articles"
    template_name = "gestion/formateur/dash_formateur_ressource.html"


def create_ressource(request):
    sauvegarde = False

    if request.method == "POST":
        form = RessourceForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Ressource()
            contact.lib_ress = form.cleaned_data["lib_ress"]
            contact.type_ress = form.cleaned_data["type_ress"]
            contact.docfile = form.cleaned_data["docfile"]
            contact.chapitre = form.cleaned_data["chapitre"]
            contact.save()

            sauvegarde = True
            print('hahaha')
    else:
        form = RessourceForm()

    return render(request, 'gestion/formateur/ressource_create_form.html', locals())


class UpdateRessource(UpdateView):
    model = Ressource
    template_name = "gestion/formateur/ressource_update_form.html"
    form_class = RessourceForm
    success_url = reverse_lazy('gestion:dash_ressource')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_ressource')


class DeleteRessource(DeleteView):
    model = Ressource
    context_object_name = "ressource"
    template_name = "gestion/formateur/ressource_delete.html"
    success_url = reverse_lazy('gestion:dash_ressource')


# CBV : Apprenant
class ListeApprenant(ListView):
    model = Apprenant
    context_object_name = "derniers_articles"
    template_name = "gestion/admin/dash_admin_apprenant.html"


class CreateApprenant(CreateView):
    model = Apprenant
    template_name = "gestion/admin/apprenant_create_form.html"
    form_class = ApprenantForm
    success_url = reverse_lazy('gestion:dash_apprenant')

    def form_valid(self, form):
        form.save(commit=False)
        return super(CreateApprenant, self).form_valid(form)


class UpdateApprenant(UpdateView):
    model = Apprenant
    template_name = "gestion/admin/apprenant_update_form.html"
    form_class = RessourceForm
    success_url = reverse_lazy('gestion:dash_apprenant')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_apprenant')


class DeleteApprenant(DeleteView):
    model = Apprenant
    context_object_name = "apprenant"
    template_name = "gestion/admin/apprenant_delete.html"
    success_url = reverse_lazy('gestion:dash_apprenant')


# CBV : Animation
class ListeAnimation(ListView):
    model = Animer
    context_object_name = "derniers_articles"
    template_name = "gestion/formateur/dash_formateur_animation.html"


class CreateAnimation(CreateView):
    model = Animer
    template_name = "gestion/formateur/animation_create_form.html"
    form_class = AnimerForm
    success_url = reverse_lazy('gestion:dash_anime')

    def form_valid(self, form):
        form.save(commit=False)
        return super(CreateAnimation, self).form_valid(form)


class UpdateAnimation(UpdateView):
    model = Animer
    template_name = "gestion/formateur/animation_update_form.html"
    form_class = AnimerForm
    success_url = reverse_lazy('gestion:dash_apprenant')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_anime')


class DeleteAnimation(DeleteView):
    model = Animer
    context_object_name = "animation"
    template_name = "gestion/formateur/animation_delete.html"
    success_url = reverse_lazy('gestion:dash_anime')


# CBV : Chapitre
class ListeChapitre(ListView):
    model = Chapitre
    context_object_name = "derniers_articles"
    template_name = "gestion/formateur/dash_formateur_chapitre.html"


class CreateChapitre(CreateView):
    model = Chapitre
    template_name = "gestion/formateur/chapitre_create_form.html"
    form_class = ChapitreForm
    success_url = reverse_lazy('gestion:dash_chapitre')

    def form_valid(self, form):
        form.save(commit=False)
        return super(CreateChapitre, self).form_valid(form)


class UpdateChapitre(UpdateView):
    model = Chapitre
    template_name = "gestion/formateur/chapitre_update_form.html"
    form_class = ChapitreForm
    success_url = reverse_lazy('gestion:dash_chapitre')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_chapitre')


class DeleteChapitre(DeleteView):
    model = Chapitre
    context_object_name = "chapitre"
    template_name = "gestion/formateur/chapitre_delete.html"
    success_url = reverse_lazy('gestion:dash_chapitre')


# CBV : Regroupement
class ListeRegroupement(ListView):
    model = Regroupement
    context_object_name = "derniers_articles"
    template_name = "gestion/formateur/dash_formateur_regroup.html"


class CreateRegroupement(CreateView):
    model = Regroupement
    template_name = "gestion/formateur/reg_create_form.html"
    form_class = RegroupementForm
    success_url = reverse_lazy('gestion:dash_regroup')

    def form_valid(self, form):
        form.save(commit=False)
        return super(CreateRegroupement, self).form_valid(form)


class UpdateRegroupement(UpdateView):
    model = Regroupement
    template_name = "gestion/formateur/reg_update_form.html"
    form_class = RegroupementForm
    success_url = reverse_lazy('gestion:dash_regroup')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_regroup')


class DeleteRegroupement(DeleteView):
    model = Regroupement
    context_object_name = "reg"
    template_name = "gestion/formateur/reg_delete.html"
    success_url = reverse_lazy('gestion:dash_regroup')


# CBV : Test
class ListeTest(ListView):
    model = Test
    context_object_name = "derniers_articles"
    template_name = "gestion/formateur/dash_formateur_test.html"


class CreateTest(CreateView):
    model = Test
    template_name = "gestion/formateur/test_create_form.html"
    form_class = TestForm
    success_url = reverse_lazy('gestion:dash_test')

    def form_valid(self, form):
        form.save(commit=False)
        return super(CreateTest, self).form_valid(form)


class UpdateTest(UpdateView):
    model = Test
    template_name = "gestion/formateur/test_update_form.html"
    form_class = TestForm
    success_url = reverse_lazy('gestion:dash_test')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_test')


class DeleteTest(DeleteView):
    model = Test
    context_object_name = "test"
    template_name = "gestion/formateur/test_delete.html"
    success_url = reverse_lazy('gestion:dash_test')


# CBV : Cours
class ListeCours(ListView):
    model = Cours
    context_object_name = "derniers_articles"
    template_name = "gestion/formateur/dash_formateur_cours.html"


class CreateCours(CreateView):
    model = Cours
    template_name = "gestion/formateur/cours_create_form.html"
    form_class = CoursForm
    success_url = reverse_lazy('gestion:dash_cours')

    def form_valid(self, form):
        form.save(commit=False)
        return super(CreateCours, self).form_valid(form)


class UpdateCours(UpdateView):
    model = Cours
    template_name = "gestion/formateur/cours_update_form.html"
    form_class = CoursForm
    success_url = reverse_lazy('gestion:dash_cours')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Votre profil a ete mis a jour avec succes.")
        return redirect('gestion:dash_cours')


class DeleteCours(DeleteView):
    model = Cours
    context_object_name = "cours"
    template_name = "gestion/formateur/cours_delete.html"
    success_url = reverse_lazy('gestion:dash_cours')


# READ : Consultation
class ConsultationView(ListView):
    model = Test
    context_object_name = "derniers_articles"
    template_name = "gestion/apprenant/dash_apprenant_consul.html"

    def get_queryset(self):
        return Test.objects.filter(id_util=self.request.user.apprenant.id)


"""--------------------------------------- API's Views----------------------------------"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class TimeStampedModelViewSet(viewsets.ModelViewSet):
#     queryset = TimeStampedModel.objects.all()
#     serializer_class = TimeStampedModelSerializer


class AdministrateurViewSet(viewsets.ModelViewSet):
    queryset = Administrateur.objects.all()
    serializer_class = AdministrateurSerializer


class FormateurViewSet(viewsets.ModelViewSet):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer


class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer


class ApprenantViewSet(viewsets.ModelViewSet):
    queryset = Apprenant.objects.all()
    serializer_class = ApprenantSerializer


class RegroupementViewSet(viewsets.ModelViewSet):
    queryset = Regroupement.objects.all()
    serializer_class = RegroupementSerializer


class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerialzer


class ChapitreViewSet(viewsets.ModelViewSet):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer


class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer


class AnimerViewSet(viewsets.ModelViewSet):
    queryset = Animer.objects.all()
    serializer_class = AnimerSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
