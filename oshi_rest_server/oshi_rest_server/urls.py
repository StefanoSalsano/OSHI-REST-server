from django.conf.urls import url, patterns, include
from rrdgraph_server.views import RrdGraphView

DEFAULT_FILE_SIGNATURE = 'rrdgraph/%(device)s/%(network_interface)s/%(rrd_data_source)s/%(time_scale)s/%(graph_title)s'
DEFAULT_REGEX = r'^%s$' % (DEFAULT_FILE_SIGNATURE % {
    'device': r'(?P<device>.+)',
    'network_interface': r'(?P<network_interface>.+)',
    'rrd_data_source': r'(?P<rrd_data_source>.+)',
    'time_scale': r'(?P<time_scale>.+)',
    'graph_title': r'(?P<graph_title>.+)',
})

urlpatterns = patterns('',
                       url(regex=DEFAULT_REGEX,
                           view=RrdGraphView.as_view(),
                           name="get_rrdgraph"),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       )
