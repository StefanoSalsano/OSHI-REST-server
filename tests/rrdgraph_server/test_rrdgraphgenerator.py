# expected_graph.png has been generated with the following rrdgraph command:
# rrdtool graph expected_graph.png                                 \
#         --start 920804400 --end 920808000               \
#         DEF:myspeed=test.rrd:speed:AVERAGE              \
#         LINE2:myspeed#FF0000
from PIL import Image
import ImageChops
import os
from oshi_rest_server.rrdgraph_server.rrdgraphgenerator import get_rrdgraph


class TestRrdGraphGenerator(object):
    def test_get_rrdgraph(self):
        print("Testing rrdgraph generator (get_rrdgraph)")
        test_rrd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.rrd')
        print("Test RRD file path: {}".format(test_rrd_path))
        rrd_output = get_rrdgraph(test_rrd_path, 'speed', start_time=920804400, end_time=920808000, line_width=2)
        print("RRD Graph output: {}".format(rrd_output))
        result = Image.open(rrd_output)
        expected = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'expected_graph.png'))
        assert _are_images_equal(result, expected) is True


def _are_images_equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None
