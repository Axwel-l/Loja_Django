# Generated by Django 4.1.7 on 2023-03-13 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da Categoria', max_length=80, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
