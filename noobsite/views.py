from django.shortcuts import render

# noobsite/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")