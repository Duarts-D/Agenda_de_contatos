from django.contrib import admin
from contatos.models import Contatos

class ContatosAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','data_criacao','categoria','mostrar')
    list_display_links =('id','nome','sobrenome',)
    list_per_page = 10
    list_editable = ('telefone','categoria','mostrar')
    list_filter = ('categoria',)
    search_fields = ('nome','sobrenome',)
    

    def __str__(self):
        return self.nome

admin.site.register(Contatos,ContatosAdmin)