# Generated by Django 5.0.6 on 2024-05-18 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Skill Category',
                'verbose_name_plural': 'Skill Categories',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Skill name')),
                ('percent', models.PositiveIntegerField(verbose_name='Aknowlegment Percent')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.skillcategory', verbose_name='Skill Category')),
            ],
            options={
                'verbose_name': 'Скилл категория',
                'verbose_name_plural': 'Скилл категории',
            },
        ),
    ]
