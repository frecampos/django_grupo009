# Generated by Django 2.2.16 on 2020-10-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCar', '0003_misionyvision'),
    ]

    operations = [
        migrations.AddField(
            model_name='misionyvision',
            name='numero',
            field=models.IntegerField(default=1),
        ),
    ]