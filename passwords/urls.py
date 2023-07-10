from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.passwords, name='passwords')
]
