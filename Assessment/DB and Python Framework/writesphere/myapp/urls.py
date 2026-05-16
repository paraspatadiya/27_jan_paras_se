from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('createblog/', views.createblog, name='createblog'),
    path('myblogs/', views.myblogs, name='myblogs'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('editcomment/<int:id>/', views.editcomment, name='editcomment'),
    path('deletecomment/<int:id>/', views.deletecomment, name='deletecomment'),


    path('deleteblog/<int:id>/', views.deleteblog, name='deleteblog'),
    path('read/<int:id>/', views.readblog, name='readblog'),
    path('editblog/<int:id>/', views.editblog, name='editblog'),
    path('like/<int:id>/', views.like, name='like'),
    path('follow/<int:id>/', views.follow, name='follow'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
