from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('members/', views.members, name="members"),
    path('profile/<str:pk_test>/', views.profile, name="profile"),

    path('create_tier/<str:pk>/',views.createTier, name="create_tier"),
    path('update_tier/<str:pk_tier>/',views.updateTier, name="update_tier"),
    path('delete_tier/<str:pk_item>/',views.deleteTier, name="delete_tier"),

    path('add_game/',views.newGame, name="add_game"),

    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

]
