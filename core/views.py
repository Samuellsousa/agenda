from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
#def index(request):
    #return redirect(' /agenda/')



def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return rediresct('/')

def submit_login (request):
    if request.POST:
        username = request.POST.get('username')
        password = resquest.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not none:
            login(request, usuario)
            return redirect('/')
    else:
        redirest('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados= {'eventos':evento}
    return render(request,'agenda.html',dados)