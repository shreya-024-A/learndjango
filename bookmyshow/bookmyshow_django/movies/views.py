from django.shortcuts import render,redirect 
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Movie
from theatres.models import Show
from bookings.models import Seat,Booking

def movie_list(request):
    movies = Movie.objects.all()

    return render(
        request,
        'movies/movie_list.html',
        {'movies': movies}
    )


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)

    shows = Show.objects.filter(movie=movie)

    theatre_shows = {}

    for show in shows:
        theatre = show.theatre

        if theatre not in theatre_shows:
            theatre_shows[theatre] = []

        theatre_shows[theatre].append(show)

    return render(
        request,
        'movies/movie_detail.html',
        {
            'movie': movie,
            'theatre_shows': theatre_shows
        }
    )

@login_required
def seat_selection(request, id):

    show = Show.objects.get(id=id)

    seats = Seat.objects.filter(show=show)
    
    seat_rows = {}

    for seat in seats:

        row = seat.seat_number[0]

        if row not in seat_rows:
            seat_rows[row] = []

        seat_rows[row].append(seat)  

    if request.method == "POST":

        selected_seats = request.POST.getlist('seats')
        
        if not selected_seats:
                return HttpResponse("Please select at least one available seat.")
        
        for seat_id in selected_seats:

            seat = Seat.objects.get(id=seat_id)

            if seat.is_booked:
                    return HttpResponse("Sorry! One or more selected seats are already booked.")


            seat.is_booked = True

            seat.save()

        selected_objects = Seat.objects.filter(id__in=selected_seats)

        ticket_price = 200

        total_amount = ticket_price * len(selected_seats)
        
        
        booking=Booking.objects.create(
            user=request.user,
            show=show,
            total_amount = total_amount
        )
        
        booking.seats.set(selected_objects)

        

        return render(request, "booking_success.html", {
            "movie": show.movie,
            "theatre": show.theatre,
            "show": show,
            "selected_seats": selected_objects,
            "total_amount": total_amount
        })
    
    

    return render(
        request,
        'seat_selection.html',
        {
            'show': show,
            'seat_rows': seat_rows,
        }
    )

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = RegisterForm()

    return render(request, "register.html", {"form": form})