# forms.py
from django import forms
from bandas.models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nome', 'foto', 'informacoes', 'nacionalidade', 'ano_criacao']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['banda', 'titulo', 'ano_lancamento', 'capa']

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['album', 'titulo', 'duracao', 'spotify_link', 'capa']
