from django.urls import path
from .import views

urlpatterns = [
    path('tag/', views.showTag),
    path('multiValue/', views.ShowTagforMultiple)
]