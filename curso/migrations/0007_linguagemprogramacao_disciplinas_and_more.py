# Generated by Django 4.0.6 on 2024-04-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_disciplina_apresentacao_disciplina_programa'),
    ]

    operations = [
        migrations.AddField(
            model_name='linguagemprogramacao',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, related_name='linguagens', to='curso.disciplina'),
        ),
        migrations.AlterField(
            model_name='linguagemprogramacao',
            name='projetos',
            field=models.ManyToManyField(blank=True, related_name='linguagens', to='curso.projeto'),
        ),
    ]
