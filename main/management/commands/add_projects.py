from django.core.management import BaseCommand
from main.models import ProjectImage, ProjectTag, Project


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        tags = {
            'Web-разработка': None, 
            'Базы данных': None, 
            'ORM': None, 
            'REST': None, 
            'API-запросы': None, 
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
            description = '''Приложение автоматически находит на экране "золотую и основную печьнку" в игре Cookie Clicker (Steam). 
Основная сложность в том, что печенька появляется в рандомном месте на экране, под рандомным углом и большую часть времени полупрозрачна.
Для решения этой проблемы использовался алгоритм поиска Feature Matching, который ищет изображение на основе выделения признаков и соотношения расстояния между ними.
В этом проекте также использовался PyWin32 для использования API Windows. Благодаря ему Cookie Clicker не должен быть в фокусе, может быть спрятан за окнами, размер окна может меняться и окно может быть передвинуто прямо во время работы скрипта, ведь скриншоты окна и отправка команд нажатий отправляется напрямую в окно игры.
В качестве основы приложения использовался threading - под кликер основной печеньки, под поиск и нажатие золотой печеньки и под listener горячих клавиш для включения, отключения и паузы.
Есть поддержка горячих клавиш.''',
            stack = 'OpenCV, pywin32, threading'
        )
        cookie_bot.tags.add(*get_tags('Базы данных', 'Работа с изображениями', 'Мультизадачность', 'Автоматизация'))
        cookie_bot.save()

        # TEST DEMO AND IMAGE #
        # ProjectImage.objects.get_or_create(
        #     image='img/test_image1.png',
        #     project=cookie_bot
        # )
        # ProjectImage.objects.get_or_create(
        #     image='img/test_image2.png',
        #     project=cookie_bot
        # )
        # cookie_bot.demo='https://demo.bungaa-server.ru'
        # cookie_bot.save()
        #######################

        resender_bot, _ = Project.objects.get_or_create(
            name = 'Bungaa_Resender_Bot',
            link = 'https://github.com/BungaaFACE/Bungaa_Resender_Bot',
            description = '''Бот перессылает новости из каналов реального аккаунта (не бота) всем подписанным людям с подпиской.
Источником новостей является реальный аккаунт с подпиской на каналы.

При получении новости/сообщения бот проверяет, надо ли перессылать сообщения из этого источника. При положительном результате аккаунт бота рассылает всем подписавшимся на этот канал новость.

Также в боте можно выбрать индивидуальную подписку только на определенные каналы.
- Перессылка новостей с пользовательского аккаунта по настроенным каналам/диалогам
- 2 роли для администрирования бота
- Добавление/удаление канала и внутреннего чата (в случае канала с топиками) в чате бота
- Добавление/подписчика канала внутри чата бота
- Подписка в чате бота (в доработке)
- Возможность подписчику выбрать только интересующие его каналы''',
            stack = 'Telethon, SQLite3, ООП, async'
        )
        resender_bot.tags.add(*get_tags('Автоматизация', 'Мультизадачность', 'Telegram-боты'))
        resender_bot.save()

        vacancy_parser, _ = Project.objects.get_or_create(
            name = 'Bungaa_vacancy_parser',
            link = 'https://github.com/BungaaFACE/Bungaa_vacancy_parser',
            description = '''Программа получает информацию о вакансиях с разных платформ в России, сохраняет ее в файл и позволяет удобно работать с ней (добавление, фильтрация, удаление).Поддерживаются платформы hh.ru и superjob.ru

- Поиск вакансий hh.ru и superjob;
- Фильтрация вакансий по зарплате;
- Сохранение списка вакансий в файлы JSON, XLSX, CSV, TXT- Загрузка вакансий из файлов;
- Вывод списка вакансий в консоль;
- Возможность выбора платформы для поиска и формата сохранения''',
            stack = 'API, JSON, ООП, requests'
        )
        vacancy_parser.tags.add(*get_tags('Автоматизация', 'API-запросы'))
        vacancy_parser.save()

        online_school, _ = Project.objects.get_or_create(
            name = 'Online_school_DRF_project',
            link = 'https://github.com/BungaaFACE/online_school_DRF_project',
            description = '''Проект включает в себя api сервер для онлайн школы, системы пользователей, покупки курсов и уроков. Проведена интеграция с системой платежей Stripe.
- Авторизация Simple_jwt;
- Добавление курсов и уроков;
- Покупка уроков и курсов в системе оплаты Stripe;
- Роль модератора для редактирования курсов/уроков;
- Блокировка неактивных пользователей;
- Разрешения CRUD;
- Валидация данных

Роли и команды:
- Superuser
Команда: python manage.py csu
Логин: admin@gmail.com
Пароль: admin
- Пользователи
Команда: python manage.py add_users
Назначение: создает пользователей user1 - user5 @gmail.com
Пароль: user
- Модератор
- Команда: python manage.py cmoder
Назначение: Создание пользователя и группы модераторов. Модераторы имеют права работы с любыми уроками или курсами, но без возможности их удалять и создавать новые.
Логин: moder@gmail.com
Пароль: moder
- Уроки и курсы
Команда: python manage.py add_learn_material
Назначение: создает пять курсов по пять уроков
- Оплаты
Команда: python manage.py add_payments
Назначение: создает записи оплаты
Включение блокировки неактивных пользователей
Команда: python manage.py per_task_block_inactive_users
Назначение: создает периодическую задачу по блокирвке неактивных пользователей (не заходили более 30 дней).''',
            stack = 'DRF, Celery, PostgreSQL'
        )
        online_school.tags.add(*get_tags('REST', 'ORM'))
        online_school.save()

        django_shop, _ = Project.objects.get_or_create(
            name = 'Django_shop_project',
            link = 'https://github.com/BungaaFACE/Django_shop_project',
            description = '''Веб-приложение для интернет магазина для тестирования возможностей Django. Тестовое приложение AsIs
- Система аккаунтов с подтверждением почты, смена и сброс пароля;
- Добавление, изменение продуктов зарегистрированным пользователям;
- Роль Модератор с правами редактирования описания, категорий и статуса публикации продукта после модерации;
- Блог и отдельная группа Контент-Менеджер для его ведения;
- Система рассылки писем для всех пользователей с возможностью добавить своих клиентов, темплейт письма и создания рассылки с разной периодичностью;
- Роль Менеджер для просмотра и, при необходимости, отключения рассылки, а также блокировки пользователей;
- Система логирования рассылок''',
            stack = 'Django, PostgreSQL'
        )
        django_shop.tags.add(*get_tags('Web-разработка', 'ORM', 'REST'))
        django_shop.save()

        exercises_tg_bot, _ = Project.objects.get_or_create(
            name = 'ExercisesTelegramBot',
            link = 'https://github.com/BungaaFACE/ExercisesTelegramBot',
            description = '''Данный бот автоматически парсит задачи с ресурса codeforces.com и выводит задачи по фильтру в Telegram-боте. Периодичность парсера можно настроить.
- Периодическая синхронизация задач и их статистики с сайта codeforces;
- Автоматический выбор главной тематики на основе кол-ва задач в тематике;
- Telegram бот для поиска задач по тематике+сложности, либо по названию;
- Вывод описания и условий задачи в боте''',
            stack = 'AsyncIO, SQLAlchemy, Telethon, PostgreSQL, BeautifulSoup, API-запросы'
        )
        exercises_tg_bot.tags.add(*get_tags('Базы данных', 'ORM', 'API-запросы', 'Мультизадачность', 'Telegram-боты'))

        bungaa_portfolio, _ = Project.objects.get_or_create(
            name = 'BungaaPortfolio',
            link = 'https://github.com/BungaaFACE/BungaaPortfolio',
            description = '''Текущий сайт, сайт-визитка. Написано веб-приложение максимально просто с целью показать информацию обо мне и моих проектах, а никак не в целях показать сложные технические решения.''',
            stack = 'Django, SQLite3, Javascript, CSS, HTML, CI/CD, gunicorn, nginx, docker, docker-compose'
        )
        bungaa_portfolio.tags.add(*get_tags('Web-разработка', 'ORM', 'Deployment'))
        bungaa_portfolio.save()

        repo_coppier, _ = Project.objects.get_or_create(
            name = 'repo-coppier',
            link = 'https://github.com/BungaaFACE/repo-coppier',
            description = '''Приложение написано в целях зеркалирования репозиториев с одной платформы на другую в автоматическом режиме.
В моем случае приложение используется для клонирования репозитериев github -> gitlab, т.к. удобен интерфейс github, а CI/CD gitlab.
Можно легко использовать для периодического пайплайна или для использования в Crontab.
Легко масштабируем, достаточно добавить class для сервиса репозиториев с нужными функциями (на основе класса с ABC, так что пропустить что-то сложно) и добавить сервис в поддерживаемые сервисы (SUPPORTED_SERVICES['git-service-name'] = your_client_class)
- Создание зеркала репозитория на другом ресурсе
- Проверка даты последнего коммита - зеркалирование репозиториев только с изменениями
- Если в репозитории-зеркале произошли изменения - включение force-push
- Простая интеграция новых сервисов на основе абстрактного класса
Может понадобиться, если сервис любимый сервис репозиториев не gitlab, а использовать gitlab cicd удобнее
''',
            stack = 'ООП, requests, git, ci/cd'
        )
        repo_coppier.tags.add(*get_tags('API-запросы', 'Deployment', 'Автоматизация'))
        repo_coppier.save()

        npmhelper, _ = Project.objects.get_or_create(
            name = 'NginxProxyManagerHelper',
            link = 'https://github.com/BungaaFACE/NginxProxyManagerHelper',
            description = '''NginxProxyManagerHelper - cli-интерфейс для Nginx-Proxy-Manager. Сделан для автоматизации добавления proxy/stream с помощью gitlab runner.
Посылает API-запросы к бэкенду NginxProxyManager, фактически cli замена для GUI NginxProxyManager
Функции:
- Создание proxy/stream
- Проверка proxy/stream с таким же forward host:port и при необходимости его удаление
''',
            stack = 'ООП, requests, ci/cd'
        )
        npmhelper.tags.add(*get_tags('API-запросы', 'Deployment', 'Автоматизация'))
        npmhelper.save()

        sudoku_solver, _ = Project.objects.get_or_create(
            name = 'BungaaSudokuSolver',
            link = 'https://github.com/BungaaFACE/BungaaSudokuSolver',
            description = '''BungaaSudokuSolver - приложение, которое позволяет автоматизированно решить судоку. На вход можно подать фотографию или матрицу. 
Сначала приложение пытается решить игру логически, используя известные методы решения судоку. Если логического решения нет - решение находится брутфорсом. Довольно интересный проект.
Функции:
- Чтение поля судоку с фотографии или с матрицы
- Логическое решение судоку
- Если логически судоку не заполнить - решение находится брутфорсом
''',
            stack = 'cv2, numpy, EasyOCR, ООП'
        )
        sudoku_solver.tags.add(*get_tags('Работа с изображениями', 'Автоматизация'))
        sudoku_solver.save()

        