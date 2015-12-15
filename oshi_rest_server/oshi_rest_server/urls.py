from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from rrdgraph_server import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'rrdtool', viewset=views.RrdtoolViewSet, base_name='rrdtool')

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       )
