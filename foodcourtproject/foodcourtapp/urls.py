from  .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path('',views.login,name='login'),
   path('home/',views.home, name='home'),
   path('register/',views.register, name='register'),
   path('verify-otp/', views.verify_otp, name='verify_otp'),
   path('logout/', views.logout_view, name="logout"),
   path('dashboard/', views.dashboard, name="dashboard"),
   path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
   
   
]

