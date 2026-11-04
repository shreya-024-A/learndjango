from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bookings.models import Booking

@login_required
def profile(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        "users/profile.html",
        {
            "bookings": bookings
        }
    )
# Create your views here.
