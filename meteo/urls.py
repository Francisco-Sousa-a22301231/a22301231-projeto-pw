from django.urls import path
from . import views


app_name="meteo"


urlpatterns = [
    path('', views.index, name='index'),
    path('weather/<int:city_id>/', views.weather_detail, name='weather_detail'),
]
