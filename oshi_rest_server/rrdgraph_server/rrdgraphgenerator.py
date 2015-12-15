from os import path
import time
from rrdgraph_server.exceptions import RrdDoesNotExist
from pyrrd.graph import DEF, LINE, Graph


def get_rrdgraph(rrd_file_path, data_source_name, graph_title=None, start_time='N', end_time='N', width=None,
                 height=None, line_color='#FF0000', line_width=1):
    if path.isfile(rrd_file_path) is not True:
        raise RrdDoesNotExist("{} not available".format(rrd_file_path))
    output_file = '/tmp/rrd_graph_{0}.png'.format(int(time.time() * 1000))
    data_source_name = data_source_name.encode("ascii")
    def1 = DEF(rrdfile=rrd_file_path, vname=data_source_name, dsName=data_source_name)
    line1 = LINE(value=data_source_name, color=line_color, width=line_width)
    g = Graph(output_file, start=start_time, end=end_time, title=graph_title,
              lower_limit=0, imgformat='PNG', width=width, height=height)
    g.data.extend([def1, line1])
    g.write()
    return output_file
