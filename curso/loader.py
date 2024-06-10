import json
from curso.models import *

Curso.objects.all().delete()
Disciplina.objects.all().delete()

with open('curso/json/lei.json') as f:
    dados = json.load(f)

    curso = dados['courseDetail']

    c = Curso.objects.create(
        nome=curso["courseName"],
        apresentacao=curso["presentation"],
        objetivos=curso["objectives"],
        competencias=curso["competences"],
        ects=curso["courseECTS"],
        num_semestres=curso["semesters"],
    )

    for disciplina in dados['courseFlatPlan']:
        d_original = Disciplina.objects.filter(nome=disciplina["curricularUnitName"])

        if not d_original:

            d = Disciplina.objects.create(
                nome=disciplina["curricularUnitName"],
                ano=disciplina["curricularYear"],
                semestre=disciplina["semester"],
                ects=disciplina["ects"],
                curricularIUnitReadableCode=disciplina["curricularIUnitReadableCode"],
            )

            d.cursos.set([c])
