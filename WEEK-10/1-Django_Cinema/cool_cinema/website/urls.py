from django.conf.urls import url
from .views import index, projections_for_movie, projection_info

urlpatterns = [
    url(r'^projections/(?P<movie_id>[0-9]+)/$', projections_for_movie, name='projection'),
    url(r'^projection_info/(?P<projection_id>[0-9]+)/$', projection_info, name='proj_info'),
    url(r'^$', index, name='cinema-overview'),
]
