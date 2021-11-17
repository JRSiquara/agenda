from django.contrib.auth.models import User  # Inserido através do (alt+enter)
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

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
    data_atual = datetime.now() - timedelta(hours=1) # Diminui 1 hora do tempo atual
    #evento = Evento.objects.get(id=2)      # Faz uma consulta, apenas um registro.
    #evento = Evento.objects.all()          # Faz uma consulta, pegando todos registros. Traz uma lista.
    evento = Evento.objects.filter(usuario=usuario, # É a mesma coisa do "all()" mas agora esta com filtro.
                                   data_evento__gt=data_atual) # "__gt" equivale ao ">="
    dados = {'eventos':evento}                                 # "__lt" equivale ao "<="
    return render(request, 'agenda.html', dados)   # template "D:\Drago\DIO-CURSOS-EAD\PYTHON\Projetos\agenda\templates"

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.local = local
                evento.save()

            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                          data_evento=data_evento,
            #                                           descricao=descricao,
            #                                           local=local)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  local=local,
                                  usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

# @login_required(login_url='/login/')  # Caso quiera passar para uma aplicação externa, como se fosse uma API
def json_lista_evento(request, id_usuario):         # (ir na url "agenda/evento/)
    usuario = User.objects.get(id=id_usuario)
    #usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False) # Precisa desse safe=False pq tá passando uma lista.

