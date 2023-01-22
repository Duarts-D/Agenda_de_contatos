from django.shortcuts import render,redirect
from usuarios.forms import LoginForms,CadastroForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form['username'].value() 
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=username,
                password=senha            
            )
            if usuario is not None:
                auth.login(request,usuario)
                messages.success(request,f'Bem vindo {username}')

                return redirect('dashboard')
            else:
                messages.error(request,'Usuario ou senha incorretos')
                return redirect('login') 
    return render(request,'usuarios/login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    form = CadastroForm()
    
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            nome = form['nome'].value()
            sobrenome = form['sobrenome'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            username = form['username'].value()
            
            usuario = User.objects.create_user(
                username=username,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
                )
            
            usuario.save()
            messages.success(request,'Cadastro realizado com sucesso')
            return redirect('login')
    return render(request,'usuarios/cadastro.html',{'form':form})

@login_required(login_url='login')
def dashboard(request):
    return render(request,'usuarios/dashboard.html')
