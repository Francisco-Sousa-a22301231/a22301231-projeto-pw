from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm


def home_view(request):
    return render(request, 'bandas/home.html', {})

def bandas_view(request):
    bandas = []
    for b in Banda.objects.all():
        bandas.append({
            'id' : b.id,
            'nome' : b.nome,
            'nacionalidade' : b.nacionalidade,
            'ano_criacao' : b.ano_criacao,
            'foto' : b.foto,
        })
    return render(request, 'bandas/bandas.html', {'bandas' : bandas})

def banda_view(request, id_banda):
    albuns = []
    for a in Album.objects.filter(banda__id=id_banda):
        albuns.append({
            'id' : a.id,
            'nome' : a.titulo,
            'capa' : a.capa,
        })

    context = {
        'banda' : Banda.objects.get(id=int(id_banda)),
        'albums' : albuns,
    }

    return render(request, 'bandas/banda.html', context)

def album_view(request, id_album):

    musics = []
    for a in Musica.objects.filter(album__id=id_album):
        musics.append({
            'id' : a.id,
            'nome' : a.titulo,
            'capa' : a.capa,
        })

    context = {
        'album' : Album.objects.get(id=int(id_album)),
        'musics' : musics,
    }

    return render(request, 'bandas/album.html', context)

def jukebox_view(request):
    musics = []

    for musica in Musica.objects.all():
        musics.append({
            'id' : musica.id,
            'titulo' : musica.titulo,
            'album' : musica.album,
            'duracao' : musica.duracao / 100,
            'link' : musica.spotify_link,
            'foto' : musica.capa,
        })


    return render(request, 'bandas/musicas.html', {'musics' : musics})

def musica_view(request, id_music):
    musica = Musica.objects.get(id=id_music)
    context = {
        'titulo' : musica.titulo,
        'album' : musica.album,
        'duracao' : musica.duracao / 100,
        'link' : musica.spotify_link,
        'foto' : musica.capa,
    }
    return render(request, 'bandas/musica.html', context)

@login_required
def banda_create(request):
    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            banda = form.save()
            return banda_view(request, banda.pk)
    else:
        form = BandaForm()
    return render(request, 'bandas/banda_form.html', {'form': form})

@login_required
def banda_edit(request, pk):
    banda = get_object_or_404(Banda, pk=pk)
    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            banda = form.save()
            return banda_view(request, pk)
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/banda_form.html', {'form': form})


