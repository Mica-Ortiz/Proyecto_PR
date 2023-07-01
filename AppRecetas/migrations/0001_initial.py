# Generated by Django 4.2.1 on 2023-07-01 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoría',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(default='', max_length=100, null=True)),
                ('ingredientes', models.CharField(max_length=1000)),
                ('pasos', models.CharField(max_length=1000)),
                ('tiempo_de_coccion', models.IntegerField()),
                ('fecha_hora_de_subida', models.DateTimeField(default=datetime.datetime.now)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
                ('categoria', models.ManyToManyField(to='AppRecetas.categoría')),
            ],
        ),
    ]
