from django.contrib import admin
from django.urls import path,include
from adminapp import views


urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('view-doctors/', views.view_doctors, name='view_doctors'),
    path('update-doctor/<int:id>/', views.update_doctor, name='update_doctor'),
    path('delete-doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),

]