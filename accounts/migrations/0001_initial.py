# Generated by Django 3.0.7 on 2020-11-15 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('college', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=255, null=True, unique=True)),
                ('phone', models.CharField(max_length=200, null=True, unique=True)),
                ('mem_id', models.CharField(default=uuid.uuid4, editable=False, max_length=200, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Game')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tierlist', models.CharField(choices=[('Tier 1', 'Tier 1'), ('Tier 2', 'Tier 2'), ('Tier 3', 'Tier 3')], max_length=200, null=True)),
                ('played', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Game')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Member')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Member')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=200, null=True, unique=True)),
                ('phone', models.CharField(max_length=200, null=True, unique=True)),
                ('adhaar', models.CharField(max_length=200, null=True, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('is_apply', models.BooleanField(default=False)),
                ('is_lead', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
