from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('media/', views.media_index, name='index'),
    path('media/<int:media_id>/', views.media_detail, name='detail'),
    path('media/create/', views.MediaCreate.as_view(),name='media_create'),
    path('media/<int:pk>/update/', views.MediaUpdate.as_view(), name="media_update"),
    path('media/<int:pk>/delete/', views.MediaDelete.as_view(), name="media_delete"),
]