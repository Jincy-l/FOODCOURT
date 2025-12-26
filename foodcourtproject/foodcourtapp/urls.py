from  .import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',views.login,name='login'),
   path('home/',views.home, name='home'),
   path('register/',views.register, name='register'),
   path('verify-otp/', views.verify_otp, name='verify_otp'),
   path('logout/', views.logout_view, name="logout"),
   
   path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
   path('drinks/', views.drinks, name='drinks'),
   path('ourspecial/', views.ourspecial, name='ourspecial'),
   path('offers/', views.offers, name='offers'),
   path('maincourse/', views.maincourse, name='maincourse'),
   path('starter/', views.starter, name="starter"),
   

    path(
        'starter/delete/<int:id>/',
        views.delete_starter,
        name='delete_starter'
    ),

   #  path(
   #      'starter/edit/<int:id>/',
   #      views.edit_starter,
   #      name='edit_starter'
   #  ),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

