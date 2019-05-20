from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from panico.ligacao import realiza_chamada
from .form import *


def create_or_update_form(request, model, form):
    obj = model.objects.last()
    if obj:
        form_instance = form(request.POST, instance=obj)
    else:
        form_instance = form(request.POST)
    return form_instance


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
        form = create_or_update_form(request, Cadastro, ParametrosForm)
        if form.is_valid():
            form.save()
            return redirect('parametros')
    else:
        form = ParametrosForm()

    return render(request, "parametros.html", {'form': form, 'title': 'Parâmetros'})
