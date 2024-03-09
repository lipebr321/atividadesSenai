from django.shortcuts import render
from .models import pessoas

# Create your views here.


def home (request):
    return render (request,'users/home.html')


def cadastrar (resquest):
    novo = pessoas()
    novo.nome = resquest.POST.get('nome')

    novo.email = resquest.POST.get('email')

    novo.telefone = resquest.POST.get('telefone')

    novo.mensagem = resquest.POST.get('mensagem')
    
    novo.save()

    
    cadastrar = {
        'cadastrar' : pessoas.objects.all()
    } 
    return render(resquest, 'users/sucesso.html', cadastrar) 