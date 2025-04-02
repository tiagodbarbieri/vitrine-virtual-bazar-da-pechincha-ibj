from django.shortcuts import render
from django.views.generic.edit import FormView
from main import forms


# Create your views here.
class Home(FormView):
    template_name = "home.html"
    form_class = forms.Search
    success_url = "/"
