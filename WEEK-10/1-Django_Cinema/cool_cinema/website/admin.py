from django.contrib import admin
from .models import Movie, Genre, Projection, ProjectionType, Reservation


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'get_genres')
    search_fields = ['title', 'movie_genre__genre_name']


class ProjectionAdmin(admin.ModelAdmin):
    '''
        Admin View for Projection
    '''
    list_display = ('get_movie_name', 'get_proj_type', 'get_proj_price', 'date')

    def get_movie_name(self, obj):
        return obj.movie.title

    def get_proj_type(self, obj):
        return obj.dimension.ptype

    def get_proj_price(self, obj):
        return obj.dimension.pcost

    get_movie_name.admin_order_field = 'movie'
    get_movie_name.short_description = 'Movie Title'
    get_proj_type.admin_order_field = 'dimension'
    get_proj_type.short_description = 'Dimension'
    get_proj_price.admin_order_field = 'dimension'
    get_proj_price.short_description = 'Ticket Price'


class ProjectionTypeAdmin(admin.ModelAdmin):
    '''
        Admin View for ProjectionType
    '''
    list_display = ('ptype', 'pcost')


class ReservationAdmin(admin.ModelAdmin):
    '''
        Admin View for Reservation
    '''
    list_display = ('username', 'projection', 'get_seat')

    def get_seat(self, obj):
        return (obj.row, obj.col)

    get_seat.short_description = 'Seats'

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ProjectionType, ProjectionTypeAdmin)
admin.site.register(Projection, ProjectionAdmin)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
