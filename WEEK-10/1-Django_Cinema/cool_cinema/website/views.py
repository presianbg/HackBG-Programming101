from django.shortcuts import render
from .models import Movie, Projection


def index(request):
    movies = Movie.objects.all()
    movies = {'movies': movies}
    return render(request, 'website/index.html', movies)


def projections_for_movie(request, movie_id):
    projections = Projection.objects.filter(movie=movie_id)
    projections = {'projections': projections}
    return render(request, 'website/projections.html', projections)
