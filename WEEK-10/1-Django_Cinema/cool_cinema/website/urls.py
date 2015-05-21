from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^projections/(?P<movie_id>[0-9]+)/$', views.projections_for_movie, name='projections'),
    url(r'^$', views.index, name='cinema-overview'),
]
