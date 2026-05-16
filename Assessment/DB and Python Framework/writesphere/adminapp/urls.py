from django.urls import path
from . import views

urlpatterns = [
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),

    path('addcategory/', views.addcategory, name='addcategory'),
    path('deletecategory/<int:id>/', views.deletecategory, name='deletecategory'),

    path('addtag/', views.addtag, name='addtag'),
    path('deletetag/<int:id>/', views.deletetag, name='deletetag'),

    path('changepassword/<int:id>/', views.changepassword, name='changepassword'),

]