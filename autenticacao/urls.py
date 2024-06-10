from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'autenticacao'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("", views.loginPage, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/autenticacao/'), name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),

]
