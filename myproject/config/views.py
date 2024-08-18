from django.http import HttpResponse
from django.views.generic import TemplateView

def hello_world(request):
    return HttpResponse('Hello World !')

def hello_japan(request):
    return HttpResponse('Hello Japan !')

class FirstClassBaseView(TemplateView):
    template_name = 'first-class-base.html'

class CompanyDetailView(TemplateView):
    template_name = 'company-detail.html'

class IndexView(TemplateView):
    template_name = 'config/index.html'