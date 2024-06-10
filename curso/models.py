from django.db import models


class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    ects = models.IntegerField(default=180)
    competencias = models.TextField()
    num_semestres = models.IntegerField(default=6)


    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=100)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=50)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE, null=True, blank=True)
    cursos = models.ManyToManyField(Curso, related_name='disciplinas')
    apresentacao = models.TextField(default="")
    programa = models.TextField(default="")

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='projeto_imagens/')
    video_youtube = models.URLField()
    link_github = models.URLField()
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, related_name='projetos')

    def __str__(self):
        return f"{self.nome}, projeto de {self.disciplina}"


class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)
    projetos = models.ManyToManyField(Projeto, related_name='linguagens', blank=True)
    disciplinas = models.ManyToManyField(Disciplina, related_name='linguagens', blank=True)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField(Disciplina, related_name='docentes')

    def __str__(self):
        return self.nome
