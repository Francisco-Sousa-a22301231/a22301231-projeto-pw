import json
from bandas.models import *

Banda.objects.all().delete()
Musica.objects.all().delete()
Album.objects.all().delete()

with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)

    # autores é um dicionario de autores, tendo como
    # chave o nome do autor, e como
    # valor um dicionario com informação do autor

    for banda in bandas:
            b = Banda.objects.create(
                nome=banda["nome"],
                nacionalidade=banda["nacionalidade"],
                ano_criacao=banda["ano_criacao"],
            )

with open('bandas/json/discos.json') as f:
    discos = json.load(f)

    # livros é uma lista de dicionarios,
    # cada dicionario tendo informacao de um livro

    for disco in discos:

            banda = Banda.objects.get(nome=disco['banda'])

            a = Album.objects.create(
                titulo=disco["titulo"],
                ano_lancamento=disco["ano_lancamento"],
                banda=banda,
            )

            for musica in disco['musicas']:

                m = Musica.objects.create(
                    album=a,
                    titulo=musica['titulo'],
                    duracao=musica['duracao'],
                )