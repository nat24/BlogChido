# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 20:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import techlinx.Staff.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(max_length=180, unique=True)),
                ('biografia', models.TextField(help_text='Biografia del miembro del Staff')),
                ('imagen', models.ImageField(help_text='Imagen del miembro del staff', upload_to=techlinx.Staff.models.path_save_images)),
                ('autor', models.BooleanField(default=False, help_text='Marcar si es autor', verbose_name='¿Es autor?')),
                ('editor', models.BooleanField(default=False, help_text='Marcar si es Editor', verbose_name='¿Es Editor?')),
                ('facebook', models.URLField(blank=True, help_text='URL del Perfil de Facebook', null=True, verbose_name='Perfil de Facebook')),
                ('twitter', models.URLField(blank=True, help_text='URL del Perfil de Twitter', null=True, verbose_name='Perfil de Twitter')),
                ('GitHub', models.URLField(blank=True, help_text='URL del Perfil de GitHub', null=True, verbose_name='Perfil de GitHub')),
                ('pagina_personal', models.URLField(blank=True, help_text='URL del Perfil de pagina personal', null=True, verbose_name='Pagina personal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
