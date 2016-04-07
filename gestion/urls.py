from django.conf.urls import url

from gestion import views

urlpatterns = [

    url(
        regex=r'^consultation$',
        view=views.ConsultationView.as_view(),
        name='dash_consul'
    ),

    # urls for atomic function
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    # change password urls
    url(r'^password-change/$','django.contrib.auth.views.password_change',name='password_change'),
    url(r'^password-change/done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),

    url(r'^register/$', views.register, name='register'),

    # CRUD (Categorie)
    url(
        regex=r'^categorie$',
        view=views.ListeCategorie.as_view(),
        name='dash_categorie'
    ),

    url(
        regex=r'^categorie/new$',
        view=views.CreateCategorie.as_view(),
        name='create_categ'

    ),

    url(
        regex=r'^categorie/edit/(?P<pk>\d+)$',
        view=views.UpdateCategorie.as_view(),
        name='update_categ'
    ),

    url(
        regex=r'^categorie/del/(?P<pk>\d+)$',
        view=views.DeleteCategorie.as_view(),
        name='delete_categ'
    ),

    # CRUD (Formateur)
    url(
        regex=r'^formateur$',
        view=views.ListeFormateur.as_view(),
        name='dash_formateur'
    ),

    url(
        regex=r'^formateur/new$',
        view=views.CreateFormateur.as_view(),
        name='create_formateur'
    ),

    url(
        regex=r'^formateur/edit/(?P<pk>\d+)$',
        view=views.UpdateFormateur.as_view(),
        name='update_formateur'
    ),

    url(
        regex=r'^formateur/del/(?P<pk>\d+)$',
        view=views.DeleteFormateur.as_view(),
        name='delete_formateur'
    ),

    # CRUD (Ressource)
    url(
        regex=r'^ressource$',
        view=views.ListeRessource.as_view(),
        name='dash_ressource'
    ),

    url(
        regex=r'^ressource/new$',
        view=views.CreateRessource.as_view(),
        name='create_ressource'
    ),

    url(
        regex=r'^ressource/edit/(?P<pk>\d+)$',
        view=views.UpdateRessource.as_view(),
        name='update_ressource'
    ),

    url(
        regex=r'^ressource/del/(?P<pk>\d+)$',
        view=views.DeleteRessource.as_view(),
        name='delete_ressource'
    ),

    # CRUD (Apprenant)
    url(
        regex=r'^apprenant$',
        view=views.ListeApprenant.as_view(),
        name='dash_apprenant'
    ),

    url(
        regex=r'^apprenant/new$',
        view=views.CreateApprenant.as_view(),
        name='create_apprenant'
    ),

    url(
        regex=r'^apprenant/edit/(?P<pk>\d+)$',
        view=views.UpdateApprenant.as_view(),
        name='update_apprenant'
    ),

    url(
        regex=r'^apprenant/del/(?P<pk>\d+)$',
        view=views.DeleteApprenant.as_view(),
        name='delete_apprenant'
    ),

    # CRUD (Animer)
    url(
        regex=r'^anime$',
        view=views.ListeAnimation.as_view(),
        name='dash_anime'
    ),

    url(
        regex=r'^anime/new$',
        view=views.CreateAnimation.as_view(),
        name='create_anime'
    ),

    url(
        regex=r'^anime/edit/(?P<pk>\d+)$',
        view=views.UpdateAnimation.as_view(),
        name='update_anime'
    ),

    url(
        regex=r'^anime/del/(?P<pk>\d+)$',
        view=views.DeleteAnimation.as_view(),
        name='delete_anime'
    ),


    # CRUD (Chapitre)
    url(
        regex=r'^chapitre$',
        view=views.ListeChapitre.as_view(),
        name='dash_chapitre'
    ),

    url(
        regex=r'^chapitre/new$',
        view=views.CreateChapitre.as_view(),
        name='create_chapitre'
    ),

    url(
        regex=r'^chapitre/edit/(?P<pk>\d+)$',
        view=views.UpdateChapitre.as_view(),
        name='update_chapitre'
    ),

    url(
        regex=r'^chapitre/del/(?P<pk>\d+)$',
        view=views.DeleteChapitre.as_view(),
        name='delete_chapitre'
    ),

    # CRUD (Regroupement)
    url(
        regex=r'^regroup',
        view=views.ListeRegroupement.as_view(),
        name='dash_regroup'
    ),

    url(
        regex=r'^reg/new$',
        view=views.CreateRegroupement.as_view(),
        name='create_reg'
    ),

    url(
        regex=r'^reg/edit/(?P<pk>\d+)$',
        view=views.UpdateRegroupement.as_view(),
        name='update_reg'
    ),

    url(
        regex=r'^reg/del/(?P<pk>\d+)$',
        view=views.DeleteRegroupement.as_view(),
        name='delete_reg'
    ),

    # CRUD (Test)
    url(
        regex=r'^test',
        view=views.ListeTest.as_view(),
        name='dash_test'
    ),

    url(
        regex=r'^t/new$',
        view=views.CreateTest.as_view(),
        name='create_t'
    ),

    url(
        regex=r'^t/del/(?P<pk>\d+)$',
        view=views.DeleteTest.as_view(),
        name='delete_t'
    ),

    url(
        regex=r'^t/edit/(?P<pk>\d+)$',
        view=views.UpdateTest.as_view(),
        name='update_t'
    ),

]
