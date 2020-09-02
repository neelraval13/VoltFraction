from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('members/', views.members),
    path('profile/<str:pk_test>/', views.profile),
]
