from django.conf.urls import patterns, include, url
from django.contrib import admin
#New
from home import views
#from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', WelcomeView.as_view(), name='welcome'),
    url(r'^$', 'home.views.index')
    #pruebas url
    #url(r'^about/', TemplateView.planapp(template_name="about.html")),
)
