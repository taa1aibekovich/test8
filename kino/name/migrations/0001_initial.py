# Generated by Django 5.0.6 on 2024-07-06 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='actor/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('tagline', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='posters/')),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=32)),
                ('world_premiere', models.DateField()),
                ('budget', models.BigIntegerField()),
                ('fees_in_usa', models.BigIntegerField()),
                ('fess_in_world', models.BigIntegerField()),
                ('actors', models.ManyToManyField(related_name='movies', to='name.actor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.category')),
                ('directors', models.ManyToManyField(related_name='movies', to='name.director')),
                ('genres', models.ManyToManyField(related_name='movies', to='name.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=32)),
                ('text', models.TextField()),
                ('stars', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='name.movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='name.reviews', verbose_name='Родитель')),
            ],
        ),
    ]