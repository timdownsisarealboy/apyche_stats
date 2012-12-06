from django.conf.urls.defaults import *
from django.views.static import * 
from django.conf import settings

urlpatterns = patterns('',
    (r'^api/', include('apyche_stats.api.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
