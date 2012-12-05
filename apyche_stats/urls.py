from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^api/', include('apyche_stats.api.urls')),
)
