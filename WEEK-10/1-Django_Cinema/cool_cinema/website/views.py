from django.shortcuts import render, redirect
from .models import Movie, Projection, Reservation
from cool_cinema.settings import HALL_SEATS


def index(request):
    movies = Movie.objects.all()
    movies = {'movies': movies}
    return render(request, 'website/index.html', movies)


def projections_for_movie(request, movie_id):
    projections = Projection.objects.filter(movie=movie_id)
    projections = {'projections': projections,
                   'hall_seats': HALL_SEATS}
    return render(request, 'website/projections.html', projections)


def projection_info(request, projection_id):
    proj_info = Projection.objects.get(id=projection_id)
    reserv_for_proj = Reservation.objects.filter(projection=projection_id)
    available_seats = HALL_SEATS - reserv_for_proj.count()
    hall_cols = range(1, 11)
    hall_rows = range(11)
    taken_seats = []
    for proj in reserv_for_proj:
        taken_seats.append((proj.row, proj.col))
    all_info = {'reserv_for_proj': reserv_for_proj,
                'available_seats': available_seats,
                'hall_cols': hall_cols,
                'hall_rows': hall_rows,
                'taken_seats': taken_seats,
                'proj_info': proj_info}

    if request.method == "POST":
        name = request.POST['user']
        row = request.POST['row']
        col = request.POST['col']
        try:
            Reservation.objects.create(username=name, projection=proj_info, row=row, col=col)
            return redirect("cinema:proj_info", projection_id=projection_id)
        except:
            return redirect("cinema:proj_info", projection_id=projection_id)

    return render(request, 'website/projection_info.html', all_info)
