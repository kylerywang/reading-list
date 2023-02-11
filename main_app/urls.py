from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('media/', views.media_index, name='index'),
]