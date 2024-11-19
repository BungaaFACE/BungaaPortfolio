from django.core.management import BaseCommand
from main.models import SkillCategory, Skill


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        web_development, _ = SkillCategory.objects.get_or_create(name='Веб-разработка')
        databases, _ = SkillCategory.objects.get_or_create(name='Базы данных')
        api, _ = SkillCategory.objects.get_or_create(name='API')
        orm, _ = SkillCategory.objects.get_or_create(name='ORM')
        multitasking, _ = SkillCategory.objects.get_or_create(name='Мультизадачность')
        tg_bots, _ = SkillCategory.objects.get_or_create(name='Telegram-боты')
        deployment, _ = SkillCategory.objects.get_or_create(name='Развертывание')
        other, _ = SkillCategory.objects.get_or_create(name='Другое')

        Skill.objects.get_or_create(
            name='Django',
            percent=85,
            category=web_development
        )
        Skill.objects.get_or_create(
            name='Flask',
            percent=55,
            category=web_development
        )

        Skill.objects.get_or_create(
            name='Postgres',
            percent=90,
            category=databases
        )
        Skill.objects.get_or_create(
            name='ClickHouse',
            percent=75,
            category=databases
        )
        Skill.objects.get_or_create(
            name='Ignite',
            percent=35,
            category=databases
        )

        Skill.objects.get_or_create(
            name='DRF',
            percent=85,
            category=api
        )
        Skill.objects.get_or_create(
            name='Flask',
            percent=70,
            category=api
        )

        Skill.objects.get_or_create(
            name='Django ORM',
            percent=95,
            category=orm
        )
        Skill.objects.get_or_create(
            name='SQLAlchemy ORM',
            percent=60,
            category=orm
        )

        Skill.objects.get_or_create(
            name='AsyncIO',
            percent=70,
            category=multitasking
        )
        Skill.objects.get_or_create(
            name='Threading',
            percent=85,
            category=multitasking
        )

        Skill.objects.get_or_create(
            name='aiogram',
            percent=90,
            category=tg_bots
        )
        Skill.objects.get_or_create(
            name='Telethon',
            percent=90,
            category=tg_bots
        )

        Skill.objects.get_or_create(
            name='Docker/docker-compose',
            percent=90,
            category=deployment
        )
        Skill.objects.get_or_create(
            name='gitlab-pipeline',
            percent=85,
            category=deployment
        )

        Skill.objects.get_or_create(
            name='OpenCV',
            percent=40,
            category=other
        )
        Skill.objects.get_or_create(
            name='win32api',
            percent=30,
            category=other
        )
