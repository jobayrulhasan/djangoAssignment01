from django.urls import path
from .import views

urlpatterns = [
    path('fr/', views.resource),
]