from django.contrib import admin
from .models import Banda, Album, Musica

@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'informacoes')
    search_fields = ('nome',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'ano_lancamento')
    list_filter = ('banda', 'ano_lancamento')
    search_fields = ('titulo', 'banda__nome')

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'duracao')
    list_filter = ('album',)
    search_fields = ('titulo', 'album__titulo')
