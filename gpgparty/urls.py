from django.conf.urls import patterns, include, url

from django.contrib import admin
from gpgsign.views import me, index
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gpgparty.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'me/$', me, name="me"),        
    url(r'^$',index, name="index"),


)
