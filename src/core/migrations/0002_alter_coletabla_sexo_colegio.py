# Generated by Django 4.2 on 2023-06-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coletabla',
            name='sexo_colegio',
            field=models.TextField(blank=True, db_column='sexo_colegio', null=True),
        ),
    ]