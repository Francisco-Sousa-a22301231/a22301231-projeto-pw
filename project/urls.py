from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/', include('pwsite.urls')),
    path('novaapp/', include('novaapp.urls')),
    path('bandas/', include('bandas.urls')),
    path('curso/', include('curso.urls')),
    path('praias/', include('praias.urls')),
    path('artigos/', include('artigos.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('', include('portfolio.urls')),
    path('meteo', include('meteo.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="autenticacao/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="autenticacao/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="autenticacao/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="autenticacao/password_reset_done.html"), name="password_reset_complete"),
]
