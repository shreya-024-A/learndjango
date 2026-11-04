from django.db import transaction
from .models import Booking, Seat
from theatres.models import Show

def book_seats(user, show_id, seat_ids):
    show = Show.objects.get(id=show_id)

    seats = Seat.objects.filter(id__in=seat_ids, show=show)

    # check availability
    if seats.filter(is_booked=True).exists():
        return "Some seats already booked"

    with transaction.atomic():
        seats.update(is_booked=True)

        booking = Booking.objects.create(
            user=user,
            show=show,
            total_amount=len(seats) * 150
        )

        booking.seats.set(seats)

    return booking