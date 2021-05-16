# Generated by Django 3.2.2 on 2021-05-14 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='joinUsModel',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=12)),
                ('wpPhone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=250)),
                ('occupation', models.CharField(max_length=100)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]