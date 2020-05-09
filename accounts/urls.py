from django.urls import path
from . import views


urlpatterns = [
    path('sign_up/', views.sign_up, name='sing_up'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]