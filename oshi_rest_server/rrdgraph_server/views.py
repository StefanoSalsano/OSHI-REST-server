import os
from django import http
from rrdgraph_server import config
from rrdgraph_server.exceptions import RrdGraphError
from django.views.static import serve
from rrdgraphgenerator import get_rrdgraph
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny


class RrdtoolViewSet(viewsets.ViewSet):
    @detail_route(url_path='rrdgraph', permission_classes=[AllowAny])
    def produce_rrdgraph(self, request, **kwargs):
        """
            This endpoint generates a graph of an RRD using rrdgraph.
            ---
            parameters_strategy: replace
            parameters:
                - name: pk
                  description: "RRD file name (excluding extension). Must be present in the
                               rrdgraph_server.config.RRD_FILE_PATH directory, configured in
                               OSHI-REST-server/oshi_rest_server/rrdgraph_server/config.py"
                  required: true
                  type: string
                  paramType: path
                - name: rrd_data_source
                  description: "RRD data source. Must be defined in the specified RRD file. For simplicity we set this
                                as an enumeration of data sources available in RRDs produced by OSHI-monitoring. It
                                could be set to the name of any data source available in the specified RRD."
                  required: true
                  type: string
                  paramType: query
                  allowMultiple: false
                  enum: ["rx_bytes","tx_bytes","rx_packets","tx_packets","sdn_rx_bytes","sdn_tx_bytes","sdn_rx_packets",
                         "sdn_tx_packets"]
                - name: time_scale
                  description: Graph time scale
                  required: true
                  type: string
                  paramType: query
                  allowMultiple: false
                  enum: ["10_mins","1_hour","1_day","1_week","1_month"]
                - name: graph_title
                  description: Graph title
                  required: false
                  type: string
                  paramType: query
        """
        rrd_file_name = kwargs.get('pk') + '.rrd'
        rrd_data_source = request.query_params.get('rrd_data_source')
        time_scale = request.query_params.get('time_scale')
        graph_title = request.query_params.get('graph_title')

        try:
            rrd_graph_path = _generate_rrdgraph(rrd_file_name, rrd_data_source, time_scale, graph_title)
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


def _generate_rrdgraph(rrd_file_name, rrd_data_source, time_scale, graph_title):
    end = 'now'
    start = 'end' + _RRDGRAPH_TIME_SCALES[time_scale]
    return get_rrdgraph(os.path.join(config.RRD_FILE_PATH, rrd_file_name), rrd_data_source,
                        graph_title=graph_title, start_time=start, end_time=end)


def serve_static_file(request, rrd_graph_path):
    rrd_graph_path = unicode(rrd_graph_path, "ascii")
    return serve(request, rrd_graph_path, document_root='/')
