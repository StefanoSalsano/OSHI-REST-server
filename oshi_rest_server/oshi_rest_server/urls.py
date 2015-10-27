from django.conf.urls import url, patterns
from rrdgraph_server.views import RrdGraphView

urlpatterns = patterns('',
                       url(regex=r'^rrdgraph$',
                           view=RrdGraphView.as_view(),
                           name="get_rrdgraph"))
