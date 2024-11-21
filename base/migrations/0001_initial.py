# Generated by Django 5.1.1 on 2024-11-12 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Harajatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'beginner'), (2, 'waiting'), (3, 'accepted'), (4, 'rejected')], default=1)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('description', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'junior'), (2, 'middle'), (3, 'senior')], default=1)),
                ('city', models.CharField(max_length=255)),
                ('rank', models.JSONField()),
                ('requirements', models.JSONField()),
                ('dastur', models.JSONField()),
                ('scholarships', models.JSONField()),
                ('departments', models.JSONField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='universities/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shartnoma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tarif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tarif')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.university')),
            ],
        ),
    ]