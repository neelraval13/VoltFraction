# Generated by Django 3.0.7 on 2020-11-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201126_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='is_add',
            field=models.BooleanField(default=False),
        ),
    ]
