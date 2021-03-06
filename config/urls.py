# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

from rest_framework import routers

from gestion.views import HomeView

from gestion import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'administrateurs', views.AdministrateurViewSet)
router.register(r'formateurs', views.FormateurViewSet)
router.register(r'categories', views.CategorieViewSet)
router.register(r'formations', views.FormationViewSet)
router.register(r'apprenants', views.ApprenantViewSet)
router.register(r'regroupement', views.RegroupementViewSet)
router.register(r'cours', views.CoursViewSet)
router.register(r'chapitres', views.ChapitreViewSet)
router.register(r'ressources', views.RessourceViewSet)
router.register(r'animers', views.AnimerViewSet)
router.register(r'tests', views.TestViewSet)

urlpatterns = [
                  url(r'^$', HomeView.as_view(), name="home"),
                  url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

                  # Django Admin, use {% url 'admin:index' %}
                  url(settings.ADMIN_URL, include(admin.site.urls)),

                  # User management
                  url(r'^users/', include("tice_project.users.urls", namespace="users")),
                  url(r'^accounts/', include('allauth.urls')),

                  # Your stuff: custom urls includes go here
                  url(r'^gestion/', include('gestion.urls', namespace='gestion')),
                  url(r'^pv/', include('pv.urls', namespace='pv')),

                  # Apis
                  url(r'^api/', include(router.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
