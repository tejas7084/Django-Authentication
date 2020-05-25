from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('loginpage/', views.loginpage, name='login'),
    path('logoutpage/', views.logoutpage, name='logout')
]
