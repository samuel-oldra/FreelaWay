from django.urls import path

from . import views

urlpatterns = [
    path('encontrar_jobs/', views.encontrar_jobs, name="encontrar_jobs"),
]
