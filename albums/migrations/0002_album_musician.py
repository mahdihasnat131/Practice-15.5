# Generated by Django 5.0.6 on 2024-07-07 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='musician',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='musics.music'),
        ),
    ]