from django.shortcuts import reverse
from django.views import generic
from .form import Registration
from .models import *
from django.shortcuts import render


class Home(generic.TemplateView):
    template_name = 'index.html'

    
class Register(generic.CreateView):
    template_name = 'signup.html'   
    form_class = Registration

 
    def get_succes_url(self):
        return reverse('django:home')
