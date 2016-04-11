from django.conf.urls import url, include, patterns

from pv import views

urlpatterns = [

    url(r'^apprenant/pdf/$', views.note_apprenant, name='admin_order_pdf'),
]
