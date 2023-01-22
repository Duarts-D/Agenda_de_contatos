from django.shortcuts import render,get_object_or_404,redirect
from contatos.models import Contatos
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q,Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated: 
        contatos = Contatos.objects .order_by('-id').filter(mostrar=True,user=request.user.id)
        paginator = Paginator(contatos,10)
        page = request.GET.get('page')
        contatos = paginator.get_page(page)
    else:
        contatos = Contatos.objects .order_by('-id').filter(mostrar=False)
        paginator = Paginator(contatos,10)
        page = request.GET.get('page')
        contatos = paginator.get_page(page)

    return render(request,'home/index.html',{'contatos':contatos})

def ver_contato(request,contato_id):
    contato = get_object_or_404(Contatos,id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request,'contato/detalhes.html',{'contato':contato})

def busca(request):
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.error(request,'Campo de busca nao pode fica vazio ')
        return redirect('index')

    campos = Concat('nome',Value(' '),'sobrenome')
    contatos = Contatos.objects.annotate(
        nome_completo=campos
    ).filter(nome_completo__icontains=termo
    )
    
    paginator = Paginator(contatos,5)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request,'home/busca.html',{'contatos':contatos})
    