# Generated by Django 5.0.6 on 2024-11-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_experience_experienceproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Project Tag',
                'verbose_name_plural': 'Project Tags',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('stack', models.CharField(max_length=50, verbose_name='Стэк')),
                ('tags', models.ManyToManyField(to='main.projecttag')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.DeleteModel(
            name='ExperienceProject',
        ),
    ]