# Generated by Django 5.0.6 on 2025-01-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='demo',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
