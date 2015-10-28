from django.conf.urls import url, patterns
from rrdgraph_server.views import RrdGraphView


DEFAULT_FILE_SIGNATURE = 'rrdgraph/%(device)s/%(network_interface)s/%(time_scale)s/%(graph_title)s'
DEFAULT_REGEX = r'^%s$' % (DEFAULT_FILE_SIGNATURE % {
    'device': r'(?P<device>.+)',
    'network_interface': r'(?P<network_interface>.+)',
    'time_scale': r'(?P<time_scale>.+)',
    'graph_title': r'(?P<graph_title>.+)',
})

urlpatterns = patterns('',
                       url(regex=DEFAULT_REGEX,
                           view=RrdGraphView.as_view(),
                           name="get_rrdgraph")
                       )
