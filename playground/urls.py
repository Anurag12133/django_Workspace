from . import views
from django.urls import path, include

urlpatterns = [
    path('demo/', views.dummy)
]