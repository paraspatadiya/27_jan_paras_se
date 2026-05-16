from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    # Existing URLs
    path('', views.index, name='index'),
    path('getall/', views.getall),
    path('getid/<int:id>', views.getid),
    path('deleteid/<int:id>', views.deleteid),
    path('adddoctor/', views.adddoctor),
    path('updateid/<int:id>/', views.updateid),

    # New Tool URLs
    path('maps/', views.get_coordinates, name='maps'),
    path('github/', views.github_tools, name='github'),
    path('twitter/', views.twitter_feed, name='twitter'),
    path('countries/', views.country_info, name='countries'),
    path('distance/', views.calculate_distance, name='distance'),
    path('doctor-map/', views.doctor_map, name='doctor_map'),
]