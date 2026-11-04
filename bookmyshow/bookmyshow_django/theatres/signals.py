from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Show
from bookings.models import Seat

@receiver(post_save, sender=Show)
def create_seats(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.theatre.seats_count + 1):
            Seat.objects.create(
                show=instance,
                seat_number=f"S{i}"
            )