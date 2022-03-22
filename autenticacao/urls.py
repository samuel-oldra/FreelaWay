from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('logar/', views.logar, name="logar"),
    path('sair/', views.sair, name="sair"),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="password_reset"),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm_view.html"),
         name="password_reset_confirm"),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
         name="password_reset_complete"),
]
