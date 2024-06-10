from django.db import models

class Regiao(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Praia(models.Model):
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='praias')
    nome = models.CharField(max_length=300)
    servicos = models.ManyToManyField(Servico, related_name='praias')
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome

