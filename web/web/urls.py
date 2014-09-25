from django.conf.urls import patterns, include, url
from django.contrib import admin
#New
from home import views
#from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index')
)
