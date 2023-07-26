# Generated by Django 4.2 on 2023-07-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenidoscolegio',
            name='c_acceso',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='estatusthinkific',
            name='e_acceso',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modulocontenido',
            name='cm_acceso',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='salontabla',
            name='s_acceso',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
