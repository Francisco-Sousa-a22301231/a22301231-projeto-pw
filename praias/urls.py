from django.urls import path
from . import views

app_name = 'praias'

urlpatterns = [
    path('', views.praias_view, name='praias'),
    path('praia/<int:id_praia>', views.praia_view, name='praia'),
]