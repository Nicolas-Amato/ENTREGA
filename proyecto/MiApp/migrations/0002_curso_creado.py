# Generated by Django 4.1.2 on 2022-11-10 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='curso_creado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
