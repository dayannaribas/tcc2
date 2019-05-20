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


def parametros(request):
    if request.method == 'POST':
        form = create_or_update_form(request, Cadastro, ParametrosForm)
        if form.is_valid():
            form.save()
            return redirect('parametros')
    else:
        form = ParametrosForm()

    return render(request, "parametros.html", {'form': form, 'title': 'Parâmetros'})


def ligacao_view(request):
    form = None
    aviso = None

    if Cadastro.objects.all():
        cadastro = Cadastro.objects.all()[0]

        if request.method == 'POST':
            form = LigacaoForm(request.POST)
            form.cadastro = cadastro

            if form.is_valid():
                form.save()
                return redirect('ligacao')
        else:
            form = LigacaoForm()
    else:
        aviso = 'Por favor, cadastre uma conta na página de Parâmetros'

    return render(request, 'ligacao.html', {'form': form, 'title': 'Ligacao', 'aviso': aviso})
