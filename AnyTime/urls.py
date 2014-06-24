from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#import views
from AnyTimeHome.views import *
from django_cas.views import login,logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AnyTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomePage),
    url(r'^ajax/getServerStatus/$',checkstatus),
    url(r'^ajax/setServerNewTime/$',submitnewtime),
    url(r'^login/$', login),
    url(r'^logout/$',logout),

)
