# Generated by Django 4.1.6 on 2023-02-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='score',
            field=models.CharField(default=3, max_length=1),
            preserve_default=False,
        ),
    ]
