from django.conf.urls import patterns, include, url
from django.contrib import admin
#New
from home import views
#from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^min_css/', 'home.views.get_css'),
    url(r'^min2_css/', 'home.views.get_css2'),
    url(r'^min3_css/', 'home.views.get_css3'),
    url(r'^min4_css/', 'home.views.get_css4'),

    url(r'^js/', 'home.views.get_js'),
    url(r'^js2/', 'home.views.get_js2')

)
