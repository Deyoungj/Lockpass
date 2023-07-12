from django.urls import path
# from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()

# router.register('api', viewset=)


urlpatterns = [
    path('api/', views.passwords, name='passwords'),
    path('api/<int:pk>/', views.view_or_update_or_delete_password, name='password'),
]
