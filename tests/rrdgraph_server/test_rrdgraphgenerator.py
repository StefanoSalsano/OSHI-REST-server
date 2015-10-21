# TODO: write a test to check if the generated graph is equal to expected_graph.png.
# expected_graph.png has been generated with the following rrdgraph command:
# rrdtool graph expected_graph.png                                 \
#         --start 920804400 --end 920808000               \
#         DEF:myspeed=test.rrd:speed:AVERAGE              \
#         LINE2:myspeed#FF0000
