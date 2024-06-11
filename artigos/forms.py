from django import forms
from django.contrib.auth.models import User
from .models import Tema, Autor, Artigo, Comentario, Avaliacao

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['usuario', 'foto', 'bio']

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo', 'autor', 'imagem', 'tema']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 4}),
        }

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['artigo', 'autor', 'pontuacao', 'comentario']
