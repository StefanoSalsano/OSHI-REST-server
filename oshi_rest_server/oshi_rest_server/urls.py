from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from rrdgraph_server import views

DEFAULT_FILE_SIGNATURE = '%(device)s/%(network_interface)s/%(rrd_data_source)s/%(time_scale)s/%(graph_title)s'
DEFAULT_REGEX = r'^%s$' % (DEFAULT_FILE_SIGNATURE % {
    'device': r'(?P<device>.+)',
    'network_interface': r'(?P<network_interface>.+)',
    'rrd_data_source': r'(?P<rrd_data_source>.+)',
    'time_scale': r'(?P<time_scale>.+)',
    'graph_title': r'(?P<graph_title>.+)',
})

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(DEFAULT_REGEX, viewset=views.RrdGraphViewSet, base_name='rrdgraph')

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       )
