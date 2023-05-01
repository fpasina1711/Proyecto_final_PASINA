# Generated by Django 4.2 on 2023-05-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('vehiculo', models.CharField(max_length=50)),
                ('comentario', models.CharField(max_length=50)),
            ],
        ),
    ]
