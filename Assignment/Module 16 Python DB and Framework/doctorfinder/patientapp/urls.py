from django.urls import path
from patientapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('profile/', views.profile, name='profile'),
    path('doctors/', views.doctors, name='doctors'),
    path('about/', views.about, name='about'),
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('booking-success/<int:appointment_id>/', views.booking_success, name='booking_success'),
]