# Generated by Django 4.1.7 on 2023-04-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crear_campeones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campeon', models.CharField(max_length=10)),
                ('dificultad_campeon', models.PositiveIntegerField()),
                ('descripcion_campeon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Crear_mapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mapa', models.CharField(max_length=10)),
                ('cantidad_jugadores', models.PositiveIntegerField()),
                ('descripcion_mapa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Crear_ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ward', models.CharField(max_length=10)),
                ('rango_vision', models.PositiveIntegerField()),
                ('descripcion_ward', models.CharField(max_length=50)),
            ],
        ),
    ]
