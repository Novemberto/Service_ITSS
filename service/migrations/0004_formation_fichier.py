# Generated by Django 4.1.2 on 2022-12-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_categoryformation_formation'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='formation', verbose_name='Fichier'),
        ),
    ]
