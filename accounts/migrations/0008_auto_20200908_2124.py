# Generated by Django 3.0.7 on 2020-09-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200908_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='tier',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tier',
            name='won',
            field=models.IntegerField(default=0, null=True),
        ),
    ]