from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('search/', views.search, name='app-search'),
    path('about/', views.about, name='app-about')
]