from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('',views.index),
    path('getall/',views.getall),
    path('getid/<int:id>',views.getid),
    path('deleteid/<int:id>',views.deleteid),
    path('addstudent/', views.addstudent),
    path('updateid/<int:id>/', views.updateid),
    path('getcourse/',views.getcourse),
    path('getcourseid/<int:id>/',views.getcourseid),
    path('addcourse/',views.addcourse),
    path('updatecourse/<int:id>/',views.updatecourse),
    path('deletecourse/<int:id>/',views.deletecourse),

]
