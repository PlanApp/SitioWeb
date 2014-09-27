from django.conf.urls import patterns, include, url
from django.contrib import admin
#New
from home import views
from django.conf.urls.static import static
#from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    #PAGE
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    #MEDIA
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/var/www/web/web/static'}),
)
