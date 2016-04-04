from django.conf.urls import url

from gestion import views

urlpatterns = [
    url(
        regex=r'^categorie$',
        view=views.ListeCategorie.as_view(),
        name='dash_categorie'
    ),

    url(
        regex=r'^formateur$',
        view=views.FormateurView.as_view(),
        name='dash_formateur'
    ),

    url(
        regex=r'^ressource$',
        view=views.RessourceView.as_view(),
        name='dash_ressource'
    ),

    url(
        regex=r'^regroup$',
        view=views.RegroupView.as_view(),
        name='dash_regroup'
    ),

    url(
        regex=r'^teste$',
        view=views.TesteView.as_view(),
        name='dash_teste'
    ),

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

    # CRUD
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
]
