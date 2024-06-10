from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('hotel/', views.hotel_view, name='hotel'),
    path('spa/', views.spa_view, name='spa'),
]