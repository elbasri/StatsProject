# Generated by Django 4.2.7 on 2023-11-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='topProd',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]