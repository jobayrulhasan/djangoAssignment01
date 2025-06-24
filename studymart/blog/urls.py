from django.urls import path
from .import views

urlpatterns = [
    path('blo/', views.blog),
]