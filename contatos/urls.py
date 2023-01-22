from django.urls import path
from contatos.views import index,ver_contato,busca

urlpatterns = [
    path('',index,name='index'),
    path('busca/',busca,name='busca'),
    path('contatos/<str:contato_id>',ver_contato,name='ver_contato'),
]
