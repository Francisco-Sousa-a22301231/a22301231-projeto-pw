from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'artigos'

urlpatterns = [
    path('', views.artigos_view, name='home'),
    path('tema/<int:id_tema>/', views.tema_view, name='tema'),
    path('artigo/<int:id_artigo>/', views.artigo_view, name='artigo'),
    path('autor/<int:id_autor>/', views.autor_view, name='autor'),
    path("register_artigos/", views.register_artigos, name = "register"),
    path("profile_artigos/", views.profile_artigos, name = "profile"),
    path("login_artigos/", views.loginPage_artigos, name = "login"),
    path('logout_artigos/', auth_views.LogoutView.as_view(next_page='/home/'), name='logout'),
    path ('update_profile_artigos/', views.update_profile_artigos, name='update_profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="artigos/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="artigos/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="artigos/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="artigos/password_reset_done.html"), name="password_reset_complete"),
    path('toggle-like/', views.toggle_like, name='toggle_like'),

]