from django.urls import path

from . import views    # Importa archivo en el mismo directorio

urlpatterns = [
    path("enero", views.index)
]
