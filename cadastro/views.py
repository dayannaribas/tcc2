from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from panico.ligacao import realiza_chamada
from .form import *


def home(request):
    return render(request, 'home.html')


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'home.html')


def ligar(request):
    # realiza_chamada(mensagem="Ola! estou em perigo!", de='+555140421486', para='+5554999629652')
    return render(request, 'ligacao.html')


def parametros(request):
    if request.method == 'POST':
        form = ParametrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parametros')
    else:
        form = ParametrosForm()

    return render(request, "parametros.html", {'form': form, 'title': 'Parâmetros'})
