from django.urls import path
from .import views

urlpatterns = [
    path('static/', views.staticFile),
]