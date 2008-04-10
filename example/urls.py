from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Blog
    (r'^blog/', include('cblog.urls')),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    
    # Admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
