# Generated by Django 2.2.16 on 2020-10-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCar', '0002_insumos'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionyVision',
            fields=[
                ('ident', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
            ],
        ),
    ]