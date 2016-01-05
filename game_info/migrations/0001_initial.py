# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('score', models.IntegerField()),
                ('duration', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cvar', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('port', models.IntegerField()),
                ('get_info', models.BooleanField(default=True)),
                ('get_players', models.BooleanField(default=True)),
                ('get_rules', models.BooleanField(default=True)),
                ('up', models.BooleanField(default=True, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('server', models.OneToOneField(primary_key=True, serialize=False, to='game_info.Server')),
                ('server_name', models.CharField(max_length=256)),
                ('map', models.CharField(max_length=64)),
                ('folder', models.CharField(max_length=64)),
                ('game', models.CharField(max_length=64)),
                ('app_id', models.IntegerField()),
                ('player_count', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('bot_count', models.IntegerField()),
                ('server_type', models.IntegerField(choices=[(68, b'Dedicated'), (100, b'Dedicated'), (108, b'Non-dedicated'), (112, b'SourceTV')])),
                ('platform', models.IntegerField(choices=[(76, b'Linux'), (108, b'Linux'), (109, b'Mac OS X'), (111, b'Mac OS X'), (119, b'Windows')])),
                ('password_protected', models.BooleanField()),
                ('vac_enabled', models.BooleanField()),
                ('version', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='rule',
            name='server',
            field=models.ForeignKey(to='game_info.Server'),
        ),
        migrations.AddField(
            model_name='player',
            name='server',
            field=models.ForeignKey(to='game_info.Server'),
        ),
    ]
