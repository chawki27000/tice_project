from django.conf.urls import url

from gestion import views
from gestion.views import HomeView

urlpatterns = [
    url(
        regex=r'^index/$',
        view=HomeView.as_view(),
        name='index'
    ),

    url(r'^login/$', views.user_login, name='login'),
]

