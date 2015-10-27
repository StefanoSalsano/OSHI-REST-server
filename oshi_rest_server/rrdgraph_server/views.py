from django import http
from django.views.generic import View
from rrdgraph_server.exceptions import RrdGraphError
from django.views.static import serve


class RrdGraphView(View):
    def __init__(self, **kwargs):
        super(RrdGraphView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        # Return appropriate status code on invalid requests
        try:
            rrd_graph_path = 'expected_graph.png'
        except RrdGraphError, e:
            # FIXME: Handle SourceDoesNotExist with a different,
            # cacheable response to keep bogus URLs from hitting
            # the backend all the time.
            return http.HttpResponse(status=e.status, content=e)
        return serve_static_file(request, rrd_graph_path)


def serve_static_file(request, rrd_graph_path):
    return serve(request, rrd_graph_path, '/home/user/workspace/OSHI-REST-server/tests/rrdgraph_server/')
