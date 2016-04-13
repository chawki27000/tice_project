from django.conf.urls import url, include, patterns

from pv import views

urlpatterns = [

    url(r'^apprenant/pdf/info/etudiant$', views.note_apprenant, name='etudiant_pdf'),
    url(r'^apprenant/dash$', views.PVApprenantView.as_view(), name='dash_apprenant'),
    url(r'^formateur/dash$', views.PVFormateurView.as_view(), name='dash_formateur'),
    url(r'^formateur/dash/info/liste$', views.all_apprenant, name='all_apprenant'),
]
