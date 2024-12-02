from django.core.management import BaseCommand
from main.models import Experience
from datetime import date


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        huawei, _ = Experience.objects.get_or_create(
            company_name = 'Huawei',
            vacancy_name = 'Инженер сетей IMS',
            description = '''- Автоматизировал сбор статистики и расчет ключевых значений системы;
- Автоматизировал создание конфигурации сетевых элементов на основе IP схемы проекта;
- Проектирование сетей IMS/VoLTE/VoWIFI;
- Развертывание и настройка NFVI решений Huawei;
- Запуск и поддержка запуска сети;
- Наблюдение и анализ KPI;
- Troubleshooting;''',
            date_start = date(2021, 3, 13),
            date_finish = date(2022, 8, 20)
        )

        pao_mts, _ = Experience.objects.get_or_create(
            company_name = 'Мобильные ТелеСистемы (МТС)',
            vacancy_name = 'Технический эксперт',
            description = '''- Автоматизировал сбор информации с оборудования;
- Придумал и написал архитектуру структуризации и автоматизации DPI;
- Написал преобразователь конфигурации оборудования с одного вендора на другого;
- Работал с данными в БД Vertica, ClickHouse;''',
            date_start = date(2022, 8, 20),
            date_finish = date(2024, 4, 12)
        )

        mts_digital, _ = Experience.objects.get_or_create(
            company_name = 'МТС Диджитал',
            vacancy_name = 'Ведущий разработчик (Middle Developer)',
            description = '''- Написал Flask приложение для потребителей проекта;
- Создал клиент Diameter с последующим анализом данных и записью в БД ignite;
- Создал sftp интерфейс для записи напрямую в S3 minio (без записи во внутреннюю память);
- Автоматизировал CICD для развертывания/обновления приложений;
- Перенес структуры проекта в Docker(Podman) compose;
- Настройка и развертывание loguru + fluent-bit + grafana loki для анализа логов;
- Автоматизирование тестов Allure TestOps через Gitlab pipeline;
- Использовал Theading, asyncio, concurrent для ускорения приложений с IO задачами; 
- Работа с данными в БД ClickHouse, Ignite;''',
            date_start = date(2024, 4, 12)
        )

        ind_projects, _ = Experience.objects.get_or_create(
            company_name = 'Проектная деятельность (Python-разработка)',
            vacancy_name = 'Python-разработчик',
            description = '''- Писал сайты на основе Django, Postgres
- Создавал Telegram-боты с ролями и системой управления
- Автоматизировал приложения с помощью компьютерного зрения

Портфолио можно посмотреть по ссылке: https://github.com/BungaaFACE''',
            date_start = date(2023, 8, 20)
        )

#         cookie_bot, _ = ExperienceProject.objects.get_or_create(
#             name = 'Bungaa_Cookie_Clicker_Bot',
#             link = 'https://github.com/BungaaFACE/Bungaa_Cookie_Clicker_Bot',
#             description = '''Тема: автоматизация приложения, компьютерное зрение''',
#             stack = 'OpenCV, pywin32, threading',
#             experience = ind_projects
#         )
#         resender_bot, _ = ExperienceProject.objects.get_or_create(
#             name = 'Bungaa_Resender_Bot',
#             link = 'https://github.com/BungaaFACE/Bungaa_Resender_Bot',
#             description = '''Функции:
# - Пересылка новостей с пользовательского аккаунта по настроенным каналам/диалогам;
# - 2 роли для администрирования бота; - Подписка в чате бота;
# - Возможность подписчику выбрать только интересующие его каналы''',
#             stack = 'Telethon, SQLite3, ООП, async',
#             experience = ind_projects
#         )
#         vacancy_parser, _ = ExperienceProject.objects.get_or_create(
#             name = 'Bungaa_vacancy_parser',
#             link = 'https://github.com/BungaaFACE/Bungaa_vacancy_parser',
#             description = '''Функции:
# - Поиск вакансий hh.ru и superjob;
# - Фильтрация вакансий по зарплате;
# - Сохранение списка вакансий в файлы JSON, XLSX, CSV, TXT- Загрузка вакансий из файлов;
# - Вывод списка вакансий в консоль;
# - Возможность выбора платформы для поиска и формата сохранения''',
#             stack = 'API, JSON, ООП, requests',
#             experience = ind_projects
#         )
#         online_school, _ = ExperienceProject.objects.get_or_create(
#             name = 'Online_school_DRF_project',
#             link = 'https://github.com/BungaaFACE/online_school_DRF_project',
#             description = '''Функции:
# - Авторизация Simple_jwt;
# - Добавление курсов и уроков;
# - Покупка уроков и курсов в системе оплаты Stripe;
# - Роль модератора для редактирования курсов/уроков;
# - Блокировка неактивных пользователей;
# - Разрешения CRUD;
# - Валидация данных''',
#             stack = 'DRF, Celery, PostgreSQL',
#             experience = ind_projects
#         )
#         django_shop, _ = ExperienceProject.objects.get_or_create(
#             name = 'Django_shop_project',
#             link = 'https://github.com/BungaaFACE/Django_shop_project',
#             description = '''Функции:
# - Система аккаунтов с подтверждением почты, смена и сброс пароля;
# - Добавление, изменение продуктов зарегистрированным пользователям;
# - Роль Модератор с правами редактирования описания, категорий и статуса публикации продукта после модерации;
# - Блог и отдельная группа Контент-Менеджер для его ведения;
# - Система рассылки писем для всех пользователей с возможностью добавить своих клиентов, темплейт письма и создания рассылки с разной периодичностью;
# - Роль Менеджер для просмотра и, при необходимости, отключения рассылки, а также блокировки пользователей;
# - Система логирования рассылок''',
#             stack = 'Django, PostgreSQL',
#             experience = ind_projects
#         )
#         exercises_tg_bot, _ = ExperienceProject.objects.get_or_create(
#             name = 'ExercisesTelegramBot',
#             link = 'https://github.com/BungaaFACE/ExercisesTelegramBot',
#             description = '''Функции:
# - Периодическая синхронизация задач и их статистики с сайта codeforces;
# - Автоматический выбор главной тематики на основе кол-ва задач в тематике;
# - Telegram бот для поиска задач по тематике+сложности, либо по названию;
# - Вывод описания и условий задачи в боте''',
#             stack = 'AsyncIO, SQLAlchemy, Telethon, PostgreSQL, BeautifulSoup, API-запросы',
#             experience = ind_projects
#         )