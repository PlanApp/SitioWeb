from django.shortcuts import render
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
 
#def index(request):
#    return render_to_response('home/index.html', context_instance=RequestContext(request))

def index(request):
    return render_to_response('home/index.html')

def get_css(request):
    return render_to_response('bootstrap/css/bootstrap.css')

def get_css2(request):
    return render_to_response('bootstrap/css/bootstrap.min.css')

def get_css3(request):
    return render_to_response('bootstrap/css/bootstrap-theme.css')

def get_css4(request):
    return render_to_response('bootstrap/css/bootstrap-theme.min.css')

def get_js(request):
    return render_to_response('bootstrap/js/bootstrap.js')

def get_js2(request):
    return render_to_response('bootstrap/js/bootstrap.min.js')
