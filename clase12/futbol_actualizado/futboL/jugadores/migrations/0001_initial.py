# Generated by Django 5.2 on 2025-05-05 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=50)),
                ('numero_dorsal', models.PositiveIntegerField()),
                ('edad', models.PositiveIntegerField()),
            ],
        ),
    ]
