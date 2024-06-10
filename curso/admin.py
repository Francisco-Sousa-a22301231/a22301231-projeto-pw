from django.contrib import admin
from .models import AreaCientifica, Curso, Disciplina, Projeto, LinguagemProgramacao, Docente

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'area_cientifica')
    list_filter = ('ano', 'semestre', 'area_cientifica')
    search_fields = ('nome',)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objetivos', 'competencias')
    search_fields = ('nome',)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'disciplina')
    list_filter = ('ano', 'semestre', 'cursos')
    search_fields = ('nome', 'descricao', 'disciplina__nome')


class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(AreaCientifica)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)
