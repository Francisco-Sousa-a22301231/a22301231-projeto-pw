from django.shortcuts import render
from praias.models import *

def praias_view(request):
    return render(request, 'praias/praias.html', { 'regioes' : Regiao.objects.all() })

def praia_view(request, id_praia):
    context = {}

    try:
        praia = Praia.objects.get(id=id_praia)
        context['praia'] = praia
    except:
        pass

    return render(request, 'praias/praia.html', context)