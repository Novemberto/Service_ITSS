# Generated by Django 4.1.2 on 2022-12-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Offre',
                'verbose_name_plural': 'Offres',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Titre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('file', models.FileField(blank=True, null=True, upload_to='service/', verbose_name='File')),
                ('icone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Icône')),
                ('is_actif', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
