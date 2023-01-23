from django.urls import path
from contatos.views import index,ver_contato,busca,categoria

urlpatterns = [
    path('',index,name='index'),
    path('busca/',busca,name='busca'),
    path('busca/<str:categoria_name>',categoria,name='categoria'),
    path('contatos/<str:contato_id>',ver_contato,name='ver_contato'),
]
