from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LoginPage (TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'login.html'
