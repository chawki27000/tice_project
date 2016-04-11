from django.shortcuts import get_object_or_404

# Create your views here.
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
