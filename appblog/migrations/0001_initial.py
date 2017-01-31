# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('criado', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('imagem', models.ImageField(upload_to='imagens')),
                ('categoria', models.ForeignKey(to='appblog.Categoria')),
            ],
        ),
    ]
