from django.urls import path
from . import views


app_name = 'curso'

urlpatterns = [
    path('', views.curso_view, name='home'),
    path('disciplina/<int:id_disciplina>', views.disciplina_view, name='disciplina'),
    path('projeto/<int:id_projeto>', views.projeto_view, name='projeto'),
]