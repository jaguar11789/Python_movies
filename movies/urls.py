from . import views
from django.urls import path

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('popular/', views.popular, name='popular')
]