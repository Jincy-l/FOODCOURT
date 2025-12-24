from  .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path('',views.login,name='login'),
   path('home/',views.home, name='home'),
   path('register/',views.register, name='register'),
   path('verify-otp/', views.verify_otp, name='verify_otp'),
   path('logout/', views.logout_view, name="logout"),
   path('starter/', views.starter, name="starter"),
   path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
   path('drinks/', views.drinks, name='drinks'),
   path('ourspecial/', views.ourspecial, name='ourspecial'),
   path('offers/', views.offers, name='offers'),
   path('maincourse/', views.maincourse, name='maincourse'),
   
]

