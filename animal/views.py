from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, 'animal/index.html')

def pet_checker(request):
    return render(request, 'animal/index.html')


def medical(request):
    return render(request, 'animal/medical.html')


def meetup(request):
    meetup = Meetup.objects.all()
    context  = {'meetup':meetup}

    return render(request, 'animal/meetup.html', context)



# Render Pdf for meetup

def meetup_render_pdf_view(request, *args, **kwargs):
    pk  = kwargs.get('pk')
    meetup = get_object_or_404(Meetup, pk=pk)
    user = request.user



    template_path = 'animal/pdf2.html'
    context = {'meetup': meetup, 'user':user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] =  'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
