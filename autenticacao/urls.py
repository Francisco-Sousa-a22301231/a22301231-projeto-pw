from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from allauth.account.views import logout

app_name = 'autenticacao'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("", views.loginPage, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/logout/', logout, name='account_logout'),
    path('update_profile/', views.update_profile, name='update_profile'),

]
