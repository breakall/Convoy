from django.conf.urls.defaults import *
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from convoyapp.resources import UserModelResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#~ urlpatterns = patterns('',
    #~ # Example:
    #~ # (r'^convoy/', include('convoy.foo.urls')),

    #~ # Uncomment the admin/doc line below to enable admin documentation:
    #~ # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #~ # Uncomment the next line to enable the admin:
    #~ # (r'^admin/', include(admin.site.urls)),
#~ )

urlpatterns = patterns('',
    url(r'^$',          ListOrCreateModelView.as_view(resource=UserModelResource), name='User'),
    url(r'^(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=UserModelResource)),
)
