from django.contrib import admin
from django.urls import include, path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view),
    path('about/', views.second_view),
    path('contacts/', views.third_view),
    path('interview/', views.fourth_view),
    path('resume/', views.five_view),
    path('register/', include('allauth.urls')),
]
