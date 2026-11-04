from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey('theatres.Show', on_delete=models.CASCADE)
    seats = models.ManyToManyField('bookings.Seat')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def __str__(self):
        return f"{self.user.username} - {self.show}"
    

class Seat(models.Model):
    show = models.ForeignKey(
        'theatres.Show',
        on_delete=models.CASCADE
    )

    seat_number = models.CharField(max_length=10)

    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number