from django.shortcuts import render

def index_view(request):
    context = {}
    return render(request, 'novaapp/index.html', context)

def hotel_view(request):
    context = {}
    return render(request, 'novaapp/hotel.html', context)

def spa_view(request):
    context = {}
    return render(request, 'novaapp/spa.html', context)
