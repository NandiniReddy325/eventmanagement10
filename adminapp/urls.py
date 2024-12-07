from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('AdminHomePage/', views.AdminHomePage, name='AdminHomePage'),
    path('logout/', views.AdminLogout, name='AdminLogout'),
    path('register/', views.register, name='register'),
]
