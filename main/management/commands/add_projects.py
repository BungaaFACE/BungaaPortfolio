from django.core.management import BaseCommand
from main.models import ProjectTag, Project


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        tags = {
            'Web-разработка': None, 
            'Базы данных': None, 
            'ORM': None, 
            'Self-API': None, 
            'Remote API': None, 
            'Мультизадачность': None, 
            'Telegram-боты': None, 
            'Deployment': None, 
            'Работа с изображениями': None,
            'Автоматизация': None,
        }
        for tag_name in tags.keys():
            tag, _ = ProjectTag.objects.get_or_create(name=tag_name)
            tags[tag_name] = tag
        
        def get_tags(*args):
            return [tags[tag_str] for tag_str in args]


        cookie_bot, _ = Project.objects.get_or_create(
            name = 'Bungaa_Cookie_Clicker_Bot',
            link = 'https://github.com/BungaaFACE/Bungaa_Cookie_Clicker_Bot',
            description = '''Тема: автоматизация приложения, компьютерное зрение''',
            stack = 'OpenCV, pywin32, threading'
        )
        cookie_bot.tags.add(*get_tags('Базы данных', 'Работа с изображениями', 'Мультизадачность', 'Автоматизация'))
        cookie_bot.save()

        resender_bot, _ = Project.objects.get_or_create(
            name = 'Bungaa_Resender_Bot',
            link = 'https://github.com/BungaaFACE/Bungaa_Resender_Bot',
            description = '''Функции:
- Пересылка новостей с пользовательского аккаунта по настроенным каналам/диалогам;
- 2 роли для администрирования бота; - Подписка в чате бота;
- Возможность подписчику выбрать только интересующие его каналы''',
            stack = 'Telethon, SQLite3, ООП, async'
        )
        resender_bot.tags.add(*get_tags('Автоматизация', 'Мультизадачность', 'Telegram-боты'))
        resender_bot.save()

        vacancy_parser, _ = Project.objects.get_or_create(
            name = 'Bungaa_vacancy_parser',
            link = 'https://github.com/BungaaFACE/Bungaa_vacancy_parser',
            description = '''Функции:
- Поиск вакансий hh.ru и superjob;
- Фильтрация вакансий по зарплате;
- Сохранение списка вакансий в файлы JSON, XLSX, CSV, TXT- Загрузка вакансий из файлов;
- Вывод списка вакансий в консоль;
- Возможность выбора платформы для поиска и формата сохранения''',
            stack = 'API, JSON, ООП, requests'
        )
        vacancy_parser.tags.add(*get_tags('Автоматизация', 'Remote API'))
        vacancy_parser.save()

        online_school, _ = Project.objects.get_or_create(
            name = 'Online_school_DRF_project',
            link = 'https://github.com/BungaaFACE/online_school_DRF_project',
            description = '''Функции:
- Авторизация Simple_jwt;
- Добавление курсов и уроков;
- Покупка уроков и курсов в системе оплаты Stripe;
- Роль модератора для редактирования курсов/уроков;
- Блокировка неактивных пользователей;
- Разрешения CRUD;
- Валидация данных''',
            stack = 'DRF, Celery, PostgreSQL'
        )
        online_school.tags.add(*get_tags('Self-API', 'ORM'))
        online_school.save()

        django_shop, _ = Project.objects.get_or_create(
            name = 'Django_shop_project',
            link = 'https://github.com/BungaaFACE/Django_shop_project',
            description = '''Функции:
- Система аккаунтов с подтверждением почты, смена и сброс пароля;
- Добавление, изменение продуктов зарегистрированным пользователям;
- Роль Модератор с правами редактирования описания, категорий и статуса публикации продукта после модерации;
- Блог и отдельная группа Контент-Менеджер для его ведения;
- Система рассылки писем для всех пользователей с возможностью добавить своих клиентов, темплейт письма и создания рассылки с разной периодичностью;
- Роль Менеджер для просмотра и, при необходимости, отключения рассылки, а также блокировки пользователей;
- Система логирования рассылок''',
            stack = 'Django, PostgreSQL'
        )
        django_shop.tags.add(*get_tags('Web-разработка', 'ORM', 'Self-API'))
        django_shop.save()

        exercises_tg_bot, _ = Project.objects.get_or_create(
            name = 'ExercisesTelegramBot',
            link = 'https://github.com/BungaaFACE/ExercisesTelegramBot',
            description = '''Функции:
- Периодическая синхронизация задач и их статистики с сайта codeforces;
- Автоматический выбор главной тематики на основе кол-ва задач в тематике;
- Telegram бот для поиска задач по тематике+сложности, либо по названию;
- Вывод описания и условий задачи в боте''',
            stack = 'AsyncIO, SQLAlchemy, Telethon, PostgreSQL, BeautifulSoup, API-запросы'
        )
        exercises_tg_bot.tags.add(*get_tags('Базы данных', 'ORM', 'Remote API', 'Мультизадачность', 'Telegram-боты'))

        bungaa_portfolio, _ = Project.objects.get_or_create(
            name = 'BungaaPortfolio',
            link = 'https://github.com/BungaaFACE/BungaaPortfolio',
            description = '''Сайт, на котором вы находитесь.''',
            stack = 'Django, SQLite3, Javascript, CSS, HTML, CI/CD, gunicorn, nginx, docker, docker-compose'
        )
        bungaa_portfolio.tags.add(*get_tags('Web-разработка', 'ORM', 'Deployment'))
        bungaa_portfolio.save()

        repo_coppier, _ = Project.objects.get_or_create(
            name = 'repo-coppier',
            link = 'https://github.com/BungaaFACE/repo-coppier',
            description = '''Функции:
- Создание зеркала репозитория на другом ресурсе
- Проверка даты последнего коммита - зеркалирование репозиториев только с изменениями
- Если в репозитории-зеркале произошли изменения - включение force-push
- Простая интеграция новых сервисов на основе абстрактного класса
Может понадобиться, если сервис любимый сервис репозиториев не gitlab, а использовать gitlab cicd удобнее
''',
            stack = 'ООП, requests, git, ci/cd'
        )
        repo_coppier.tags.add(*get_tags('Remote API', 'Deployment', 'Автоматизация'))
        repo_coppier.save()

        npmhelper, _ = Project.objects.get_or_create(
            name = 'NginxProxyManagerHelper',
            link = 'https://github.com/BungaaFACE/NginxProxyManagerHelper',
            description = '''Описание:
NginxProxyManagerHelper - cli-интерфейс для Nginx-Proxy-Manager. Сделан для автоматизации добавления proxy/stream с помощью gitlab runner.
Функции:
- Создание proxy/stream
- Проверка proxy/stream с таким же forward host:port и при необходимости его удаление
''',
            stack = 'ООП, requests, ci/cd'
        )
        npmhelper.tags.add(*get_tags('Remote API', 'Deployment', 'Автоматизация'))
        npmhelper.save()

        sudoku_solver, _ = Project.objects.get_or_create(
            name = 'BungaaSudokuSolver',
            link = 'https://github.com/BungaaFACE/BungaaSudokuSolver',
            description = '''Описание:
BungaaSudokuSolver - приложение, которое позволяет автоматизированно решить судоку. На вход можно подать фотографию или матрицу. 
Сначала приложение пытается решить игру логически, используя известные методы решения судоку. Если логического решения нет - решение находится брутфорсом.
Функции:
- Чтение поля судоку с фотографии или с матрицы
- Логическое решение судоку
- Если логически судоку не заполнить - решение находится брутфорсом
''',
            stack = 'cv2, numpy, EasyOCR, ООП'
        )
        sudoku_solver.tags.add(*get_tags('Работа с изображениями', 'Автоматизация'))
        sudoku_solver.save()

        