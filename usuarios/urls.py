from django.urls import path
from usuarios.views import login,cadastro,dashboard,logout

urlpatterns = [
    path('login',login,name='login'),
    path('cadastro',cadastro,name='cadastro'),
    path('logout',logout,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
]
