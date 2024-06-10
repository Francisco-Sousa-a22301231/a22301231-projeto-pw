from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('jukebox/', views.jukebox_view, name='jukebox'),
    path('music/<int:id_music>', views.musica_view, name='music'),
    path('album/<int:id_album>', views.album_view, name='album'),
    path('all_bands/', views.bandas_view, name='all_bands'),
    path('band/<int:id_banda>', views.banda_view, name='band'),
    path('band/add/', views.banda_create, name='banda_create'),
    path('band/<int:pk>/edit/', views.banda_edit, name='banda_edit'),
]