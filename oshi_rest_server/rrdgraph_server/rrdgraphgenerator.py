from sys import path
import time
import rrdtool
from oshi_rest_server.rrdgraph_server.exceptions import RrdDoesNotExist


def get_rrdgraph(**_kwargs):
    rrd_file_name = _kwargs.get('rrd_file_name', '')
    data_source_name = _kwargs.get('data_source_name', '')
    start_time = _kwargs.get('start_time', 'N')
    end_time = _kwargs.get('end_time', 'N')

    # Graph config
    width = '785'
    height = '120'
    color = '0000FF'

    rrd_input = rrd_file_name
    if path.isfile(rrd_input) is not True:
        raise RrdDoesNotExist("{} not available".format(rrd_file_name))

    output_file = '/tmp/rrd_graph_{0}.png'.format(int(time.time() * 1000))

    data_definition = "DEF:vname={0}:{1}:AVERAGE".format(rrd_input, data_source_name)
    line_definition = "LINE1:vname#{0}:{1}".format(color, data_source_name)
    rrdtool.graph(output_file, '--start', str(start_time), '--end', str(end_time),
                  '-a', 'PNG',
                  '--lower-limit', '0',
                  '-w', str(width), '-h', str(height),
                  '--x-grid', 'MINUTE:10:HOUR:1:MINUTE:120:0:%R',
                  data_definition, line_definition)
    return output_file
