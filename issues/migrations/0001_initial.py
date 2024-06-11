# Generated by Django 5.0.6 on 2024-06-08 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('complexity', models.IntegerField(blank=True, choices=[(1, 'Smallest'), (2, 'Low mid'), (3, 'Medium'), (5, 'High mid'), (8, 'High'), (13, 'Very high')], default=1, null=True)),
                ('priority', models.CharField(blank=True, choices=[('LO', 'Low'), ('MD', 'Mid'), ('HI', 'High')], max_length=2, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=0)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
