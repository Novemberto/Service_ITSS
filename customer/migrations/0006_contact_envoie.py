# Generated by Django 4.0.10 on 2023-05-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='envoie',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
