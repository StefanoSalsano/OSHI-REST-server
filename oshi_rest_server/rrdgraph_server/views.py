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


def _generate_rrdgraph(device, network_interface, time_scale, graph_title):
    return get_rrdgraph(os.path.join(config.RRD_FILE_PATH, device + '.rrd'), network_interface, graph_title)


def serve_static_file(request, rrd_graph_path):
    return serve(request, rrd_graph_path)
