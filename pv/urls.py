from django.conf.urls import url, include, patterns

from pv import views

urlpatterns = [

    url(r'^apprenant/pdf/(?P<order_id>\d+)/$', views.admin_order_pdf, name='admin_order_pdf'),
]
