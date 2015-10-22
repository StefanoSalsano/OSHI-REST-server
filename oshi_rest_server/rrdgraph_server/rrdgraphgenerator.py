from os import path
import time
from oshi_rest_server.rrdgraph_server.exceptions import RrdDoesNotExist
from pyrrd.graph import DEF, LINE, Graph


def get_rrdgraph(rrd_file_name, data_source_name, start_time='N', end_time='N', width=None, height=None,
                 line_color='#FF0000'):

    rrd_input = rrd_file_name
    if path.isfile(rrd_input) is not True:
        raise RrdDoesNotExist("{} not available".format(rrd_file_name))
    output_file = '/tmp/rrd_graph_{0}.png'.format(int(time.time() * 1000))
    def1 = DEF(rrdfile=rrd_file_name, vname=data_source_name, dsName=data_source_name)
    line1 = LINE(value=data_source_name, color=line_color)
    g = Graph(output_file, start=start_time, end=end_time, x_grid='MINUTE:10:HOUR:1:MINUTE:120:0:%R',
              lower_limit=0, imgformat='PNG', width=width, height=height)
    g.data.extend([def1, line1])
    g.write()
    return output_file
