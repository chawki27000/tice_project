from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from gestion.models import Apprenant
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint


def note_apprenant(request):
    article = get_object_or_404(Apprenant, id=request.user.apprenant.id)
    html = render_to_string('pv/notes_apprenant.html', {'article': article})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"apprenant.pdf"'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response


class PVApprenantView(TemplateView):
    template_name = "pv/dash_pv_apprenant.html"


def all_apprenant(request):
    article = Apprenant.objects.all()
    html = render_to_string('pv/all_apprenant.html', {'article': article})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"apprenant.pdf"'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response


class PVFormateurView(TemplateView):
    template_name = "pv/dash_pv_formateur.html"
