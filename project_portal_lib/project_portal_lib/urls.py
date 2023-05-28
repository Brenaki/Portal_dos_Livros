from django.urls import path
from app_portal_lib import views

urlpatterns = [
    # Rota, view responsavel, nome de referencia
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('authenticator/', views.auth, name='auth'),
]
