# TODO: write a test to check if the generated graph is equal to expected_graph.png.
# expected_graph.png has been generated with the following rrdgraph command:
# rrdtool graph expected_graph.png                                 \
#         --start 920804400 --end 920808000               \
#         DEF:myspeed=test.rrd:speed:AVERAGE              \
#         LINE2:myspeed#FF0000
import os
from oshi_rest_server.rrdgraph_server.rrdgraphgenerator import get_rrdgraph


class TestRrdGraphGenerator(object):
    def test_get_rrdgraph(self):
        print("Testing rrdgraph generator (get_rrdgraph)")
        test_rrd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.rrd')
        print("Test RRD file path: {}".format(test_rrd_path))
        rrd_output = get_rrdgraph(test_rrd_path, 'speed', start_time=920804400, end_time=920808000)
        print("Log output: {}".format(rrd_output))
