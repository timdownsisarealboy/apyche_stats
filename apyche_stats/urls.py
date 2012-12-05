from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^api/', include('web_stats.api.urls')),
)
