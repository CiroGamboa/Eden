# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotoUrl', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=32)),
                ('cuerpo', models.CharField(max_length=300)),
                ('autor', models.CharField(max_length=32)),
                ('precio', models.FloatField()),
                ('editorial', models.CharField(max_length=32)),
                ('fechaPublicacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='libroUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Libros')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contraseña', models.CharField(max_length=32)),
                ('nombre', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('pais', models.CharField(max_length=32)),
                ('ciudad', models.CharField(max_length=32)),
                ('fechaNacimiento', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='librouser',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.User'),
        ),
        migrations.AddField(
            model_name='fotos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.User'),
        ),
    ]