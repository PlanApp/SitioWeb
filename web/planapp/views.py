from django.shortcuts import render
from django.conf.urls import url
# Create your views here.
#from django.views.generic import TemplateView

class AboutView(TemplateView):
	template_name = "about.html"
