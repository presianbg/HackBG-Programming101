from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=10)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    title = models.CharField(max_length=50, unique=True)
    rating = models.FloatField()
    movie_genre = models.ManyToManyField(Genre)

    def get_genres(self):
        return ', '.join([obj.genre_name for obj in self.movie_genre.all()])

    get_genres.short_description = 'Geners'

    def __str__(self):
        return '{} - {}'.format(self.title, self.rating)


class ProjectionType(models.Model):
    ptype = models.CharField(unique=True, max_length=5, verbose_name="Dimension")
    pcost = models.PositiveSmallIntegerField(verbose_name="Price for ticket (BGN)")

    def __str__(self):
        return '{} - {} lv.'.format(self.ptype, self.pcost)


class Projection(models.Model):
    dimension = models.ForeignKey(ProjectionType)
    date = models.DateTimeField()
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie.title, self.dimension, self.date.strftime("%d/%m/%y %H:%M"))


class Reservation(models.Model):
    username = models.CharField(max_length=10)
    projection = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (("projection", "row", "col"),)

    def __str__(self):
        return '{} - {} - {}'.format(self.username, (self.row, self.col), self.projection)
