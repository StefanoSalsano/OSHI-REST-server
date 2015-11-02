import os
from django import http
from django.views.generic import View
from rrdgraph_server import config
from rrdgraph_server.exceptions import RrdGraphError
from django.views.static import serve
from rrdgraphgenerator import get_rrdgraph


class RrdGraphView(View):
    def __init__(self, **kwargs):
        super(RrdGraphView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        try:
            rrd_graph_path = _generate_rrdgraph(**kwargs)
        except RrdGraphError, e:
            # Return appropriate status code on invalid requests
            return http.HttpResponse(status=e.status, content=e)
        return serve_static_file(request, rrd_graph_path)

_RRDGRAPH_TIME_SCALES = {
    '10_mins': '-600',
    '1_hour': '-3600',
    '1_day': '-86400',
    '1_week': '-604800',
    '1_month': '-16934400'
}


def _generate_rrdgraph(device, network_interface, rrd_data_source, time_scale, graph_title):
    end = 'now'
    start = 'end' + _RRDGRAPH_TIME_SCALES[time_scale]
    return get_rrdgraph(os.path.join(config.RRD_FILE_PATH, device + '-' + network_interface + '.rrd'), rrd_data_source,
                        graph_title=graph_title, start_time=start, end_time=end)


def serve_static_file(request, rrd_graph_path):
    return serve(request, rrd_graph_path)
