from django.shortcuts import render


def manda_valor_gas(request):
    return render('templates/home.html', request, {'valor_gas': 1234})
