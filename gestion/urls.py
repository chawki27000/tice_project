from django.conf.urls import patterns, url

from gestion.views import HomeView

urlpatterns = [
    url(
        regex=r'^index/$',
        view=HomeView.as_view(),
        name='index'
    ),
]

