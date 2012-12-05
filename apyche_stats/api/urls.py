from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import StatHandler

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

stat_resource = CsrfExemptResource( StatHandler )

urlpatterns = patterns( '',
    url( r'^stats/$', stat_resource )
)
