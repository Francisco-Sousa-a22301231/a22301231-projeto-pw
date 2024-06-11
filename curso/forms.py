from django import forms
from .models import AreaCientifica, Curso, Disciplina, Projeto, LinguagemProgramacao, Docente

class AreaCientificaForm(forms.ModelForm):
    class Meta:
        model = AreaCientifica
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nome', 'apresentacao', 'objetivos', 'ects',
            'competencias', 'num_semestres'
        ]

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = [
            'nome', 'ano', 'semestre', 'ects',
            'curricularIUnitReadableCode', 'area_cientifica',
            'cursos', 'apresentacao', 'programa'
        ]
        widgets = {
            'cursos': forms.CheckboxSelectMultiple
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'nome', 'ano', 'semestre', 'descricao',
            'conceitos_aplicados', 'tecnologias_usadas', 'imagem',
            'video_youtube', 'link_github', 'disciplina', 'cursos'
        ]
        widgets = {
            'cursos': forms.CheckboxSelectMultiple
        }

class LinguagemProgramacaoForm(forms.ModelForm):
    class Meta:
        model = LinguagemProgramacao
        fields = ['nome', 'projetos', 'disciplinas']
        widgets = {
            'projetos': forms.CheckboxSelectMultiple,
            'disciplinas': forms.CheckboxSelectMultiple
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nome', 'disciplinas']
        widgets = {
            'disciplinas': forms.CheckboxSelectMultiple
        }
