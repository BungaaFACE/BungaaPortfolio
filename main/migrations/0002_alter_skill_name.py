# Generated by Django 5.0.6 on 2024-05-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Skill name'),
        ),
    ]