from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import render

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-id')

    return render(
        request,
        'bookings/my_bookings.html',
        {'bookings': bookings}
    )
def success_page(request):
    return HttpResponse("Booking Successful!")