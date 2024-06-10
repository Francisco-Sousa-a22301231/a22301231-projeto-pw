from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.usuario.username

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='artigos')
    imagem = models.ImageField(blank=True, null=True)
    tema = models.ForeignKey(Tema, related_name="artigos",on_delete=models.SET_NULL , null=True, blank=True)
    gostos = models.ManyToManyField(User, related_name="gostos", blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor}: {self.conteudo[:40]}..."

class Avaliacao(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='avaliacoes')
    autor = models.CharField(max_length=100)
    pontuacao = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.autor}: {self.pontuacao}"
