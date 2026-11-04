from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from bookings.models import Seat

class Theatre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    seats_count=models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return f"{self.movie.title} - {self.theatre.name}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        

        if is_new:
            for i in range(1, self.theatre.seats_count + 1):
                Seat.objects.create(
                    show=self,
                    seat_number=f"S{i}",
                    is_booked=False
                )

