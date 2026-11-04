from django.urls import path
from .views import movie_list,movie_detail,seat_selection,register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('<int:id>/',movie_detail,name='movie_detail'),
    path('show/<int:id>/',seat_selection,name='seat_selection'),  
    path('register/', register, name='register'),

    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]