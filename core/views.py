from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# def agenda(request, var):
#     tit_evento = Evento.objects.get(titulo = var)
#     return HttpResponse('<h1>Local: {} </h1>'.format(tit_evento))
# def desc(request, var):
#     tit_evento = Evento.objects.get(descricao = var)
#     return HttpResponse('<h1>Local Desc.: {} </h1>'.format(tit_evento))

# def index(request):                 # Essa view redireciona pra uma URL.
#     return redirect('/agenda/')    # Permiter redirecionar quando não digita nada na URL.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha Inválido.") # Envia p/ login.html
    return redirect('/')

@login_required(login_url='/login/')        # @ identifica que é um decorador
def lista_eventos(request):                # view
    usuario = request.user
    #evento = Evento.objects.get(id=2)      # Faz uma consulta, apenas um registro.
    #evento = Evento.objects.all()          # Faz uma consulta, pegando todos registros. Traz uma lista.
    evento = Evento.objects.filter(usuario=usuario) # É a mesma coisa do "all()" mas agora esta com filtro.
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)   # template "D:\Drago\DIO-CURSOS-EAD\PYTHON\Projetos\agenda\templates"
