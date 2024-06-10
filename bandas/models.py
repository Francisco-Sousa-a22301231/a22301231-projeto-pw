from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.FileField(null=True, blank=True)
    informacoes = models.TextField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=200, null=True, blank=True)
    ano_criacao = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns')
    titulo = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField(null=True, blank=True)
    capa = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.banda.nome}"

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    titulo = models.CharField(max_length=200)
    duracao = models.IntegerField(help_text="Duração em segundos", null=True, blank=True)
    spotify_link = models.URLField(blank=True, null=True)
    capa = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.album.titulo}"
