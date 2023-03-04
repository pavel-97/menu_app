from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('category/<str:category_name>/', views.category, name='category'),
]
