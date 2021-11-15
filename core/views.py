from django.shortcuts import render, redirect
from core.models import Evento
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# def agenda(request, var):
#     tit_evento = Evento.objects.get(titulo = var)
#     return HttpResponse('<h1>Local: {} </h1>'.format(tit_evento))
# def desc(request, var):
#     tit_evento = Evento.objects.get(descricao = var)
#     return HttpResponse('<h1>Local Desc.: {} </h1>'.format(tit_evento))

# def index(request):                 # Essa view redireciona pra uma URL.
#     return redirect('/agenda/')    # Permiter redirecionar quando não digita nada na URL.



def lista_eventos(request):                # view
    #usuario = request.user
    #evento = Evento.objects.get(id=2)      # Faz uma consulta, apenas um registro.
    evento = Evento.objects.all()          # Faz uma consulta, pegando todos registros. Traz uma lista.
    #evento = Evento.objects.filter(usuario=usuario) # É a mesma coisa do "all()" mas agora esta com filtro.
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)   # template "D:\Drago\DIO-CURSOS-EAD\PYTHON\Projetos\agenda\templates"
