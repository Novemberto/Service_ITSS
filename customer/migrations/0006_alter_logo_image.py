# Generated by Django 4.1.2 on 2022-12-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_logo_is_black'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.FileField(upload_to='logo/', verbose_name='Image'),
        ),
    ]
