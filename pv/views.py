from django.shortcuts import get_object_or_404

# Create your views here.
from gestion.models import Apprenant
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint


def admin_order_pdf(request, order_id):
    article = get_object_or_404(Apprenant, id=order_id)
    html = render_to_string('pv/apprenant.html', {'ex': article})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"apprenant.pdf"'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
