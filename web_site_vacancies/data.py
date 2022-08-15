# -*- coding: utf-8 -*-
#from appVacancies.models import StartModel

""" Вакансии """
import json

jobs = [

    {"id": "1", "title": "Разработчик на Python", "specialty": "backend", "company": "3", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "skills": "Python, Nginx, Git, Django, Docker, Kubernetes, Высоконагруженные системы", "description": "<p>Офис в центре города с террасой и кальяном, чай, плюшки и виски всегда в наличии. Возможен свободный график работы.</p> <p><b>Минимальные требования это:</b></p> <ul> <li>Иметь опыт коммерческой разработки от 3-х лет</li> <li>Умение писать Unit-тесты на свой код</li> <li>Техническое образование, особенно приветствуем матмех и радиофак</li> <li>Знание Django, Django Rest Framework и Celery</li> <li>Знания в развертывании кластеров</li> <li>Готовность изучать технологии передачи видеоданных</li> </ul> <p><b>Бонусы:</b></p> <ul> <li>Официальное оформление по ТК</li> <li>Офис в центре города</li> <li>Гибкий график</li> <li>Обучение, конференции за счет компании</li> <li>ДМС</li> </ul> <p><b>Будет преимуществом:</b></p> <ul> <li>Опыт работы с Docker</li> <li>Навык написания сервисов на Asyncio</li> <li>Навык использования командной строки Linux/UNIX</li> <li>Умение работать с Git</li> </ul> <p>Зарплата достойная, обсуждается персонально с учетом пожеланий на собеседовании, исходя из уровня компетенций.</p>"},
    {"id": "2", "title": "Разработчик в проект на Django", "specialty": "backend", "company": "6", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "skills": "Python, Django, PostgreSQL", "description": "<p>Мы работаем на рынке веб-разработки уже более 10 лет. Основное направление - заказная разработка веб-сервисов и разработка собственных стартапов.</p> <p><b>Мы подойдем друг другу, если:</b></p> <ul> <li>вы хорошо разбираетесь в Python и Django, опыт работы от 3-х лет, принимали участие как минимум в нескольких проектах, работали в команде.</li> <li>вы хотите работать в компании единомышленников среди Django-разработчиков.</li> <li>вам интересно работать над стартапами, участвовать в жизни их становления</li> <li>вы не любите бюрократию, планерки, митапы, презентации, совещания и пр. вещи, которые отвлекают от работы</li> <li>вы жаворонок, потому что знаете, что утром голова работает лучше и задачи решаются быстрее</li> <li>вы уже знаете, что идеальных ТЗ не бывает</li> <li>вы понимаете, что прежде чем отдать задачу на проверку тестировщику надо самим все хорошо проверить. А если у проекта нет тестировщика (что периодически бывает), то проверить все дважды.</li> <li>вы понимаете, что нужно соблюдать баланс между качеством кода и длительностью разработки</li> <li>вы любите делиться знаниями, не боитесь обращаться за помощью к коллегам</li> <li>вы самостоятельный и ответственный, умеете здраво оценивать свои силы</li> </ul> <p><b>Как у нас все устроено:</b></p> <ul> <li>в качестве мессенджера Slack</li> <li>ведение задач в Gitlab</li> <li>таймтрекинг в Toggl</li> <li>проекты завернуты в Docker</li> <li>CI/CD настроен</li> <li>Тесты пишем редко (только ключевой функционал покрываем при необходимости)</li></ul> <p><b>Что предлагаем:</b></p> <ul> <li>Стабильную удаленную работу</li> <li>Проектную работу/Официальное трудоустройство</li> <li>Почасовую оплату/Оплату за месяц</li> <li>Обсуждаемое количество рабочих часов в месяц (100-200)</li> <li>Регулярные выплаты (2 раза в месяц)</li> <li>Лояльный рабочий график, начало рабочего дня не позже 10 по мск</li> <li>Интересные проекты, сложные задачи, работа с современными технологиями</li> </ul>"},
    {"id": "3", "title": "Middle SWIFT-разработчик", "specialty": "backend", "company": "1",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "skills": "Swift, CoreData, Git, ООП, Базы данных", "description": "<p>Развиваем приложение для изучения китайских слов и иероглифов. Хороши в контенте и дизайне, но не хватает правильного разработчика/разработчиков. Наша цель — сделать лидирующий мировой сервис для изучения китайского языка. В связи с чем ищем на полную или частичную удалённую занятость Senior/Middle iOS разработчика.</p> <p><b>Стек технологий:</b></p> <ul> <li>Swift</li> <li>Combine</li> <li>CoreData</li> <li>UI Constraints</li> <li>Git</li> </ul> <p><b>Что ожидаем от вас:</b></p> <ul> <li>студенты старших курсов и выпускники ВУЗов по Computer Science;</li> <li>понимание принципов ООП;</li> <li>владение английским языком (минимум Intermediate);</li> <li>готовность работать в команде;</li> <li>инициативность;</li> <li>ответственность и умение планировать своё время;</li> <li>умение понимать текущие задачи компании;</li> <li> понимание разницы между делать и сделать</li> </ul> <p>Предлагаем хорошую зарплату по рынку.</p>"},
    {"id": "4", "title": "Мидл программист на Python", "specialty": "backend", "company": "7", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "skills": "Python, Docker, MySQL", "description": " <p><b>Что ждем от кандидата:</b></p> <ul> <li>Опыт разработки на Python от 3 лет, участие в законченном коммерческом проекте, умение его грамотно описать;</li> <li>Django / Flask</li> <li>Опыт работы с 3D моделями и библиотеками для работы с ними (например Open3D) - будет преимуществом;</li> <li>Опыт работы с типовыми библиотеками NumPy, SciPy, OpenCV (trimesh, open3d, pyvista);</li> <li>SQL на базовом уровне;</li> <li>Понимание основных алгоритмов машинного обучения (линейная регрессия, random forest, catboost, нейронные сети и других);</li> <li>Математическое образование, опыт математического моделирования;</li> <li>Опыт работы с инструментами управления проектам.</li> </ul> <p><b>Чем будете заниматься:</b></p> <ul> <li>Оптимизация существующих методов виртуальной примерки обуви и разработка новых;</li> <li>Повышение скорости и точности работы виртуальной примерки обуви (от показателей SLA и выше);</li> <li>Использование библиотек и фреймворков numpy, pandas, scikit-learn, tensorflow, catboost, LightGBM, opencv;</li> <li>Разработка нейросетевых методов настройки виртуальной примерки обуви.</li> </ul> <p><b>Условия:</b></p> <ul> <li>Официальное оформление согласно ТК РФ;</li> <li>Работа с новейшим оборудованием;</li> <li>Возможность загранкомандировок на различные IT-семинары;</li> <li>График работы 5/2 с 9-00 до 18-00 (работа в офисе, не удаленно);</li> <li>Дружный коллектив и современный офис;</li> <li>Возможность дальнейшего карьерного роста.</li> </ul> <p>Окончательный уровень зарплаты обсуждается по итогам собеседования.</p>"},
    {"id": "5", "title": "Грамотный питон разработчик", "specialty": "backend", "company": "8", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "skills": "Python, Django, PostgreSQL, Git", "description": "<p>Наши основные направления: e-commerce, геосервисы, мессенджеры, распознавание образов, автоматизация, телефония и стартапы. Заказчики - крупные финансовые, IT, продуктовые компании России. Ищем опытного фулл-тайм python-разработчика для работы над проектами нашей компании.</p> <p><b>Что ждем от кандидата:</b></p> <ul> <li>Опыт коммерческой разработки на Python/Django от 2-х лет;</li> <li>Знания SQL (Postgres);</li> <li>Опыт написания клиент-серверных приложений;</li> <li>Умение оценивать объем и сроки работ;</li> <li>Git, системы bug tracking.</li> </ul> <p><b>Чем будете заниматься:</b></p> <ul> <li>Участвовать во всём процессе разработки - от проектирования до запуска.</li> <li>Оптимизировать работу приложения.</li> </ul> <p><b>Плюшки:</b></p> <ul> <li>Оклад от 140 000 руб на руки.;</li> <li>Удаленное сотрудничество с выстроенными процессами;</li> <li>Оформление по ТК РФ.</li> <li>Амбициозные проекты, интересные с профессиональной точки зрения задачи;</li> <li>Команда профессионалов.</li> </ul> <p>В отклике обязательно сопроводительное письмо, почему именно вы подходите на эту вакансию.</p>"}

]

""" Компании """

companies = [

    {"id": "1", "title": "workiro", "logo": "logo1.png", "employee_count": "10", "location": "Новосибирск", "description": "Разрабатываем мобильные приложения и сервисы для сферы онлайн-обучения."},
    {"id": "2", "title": "rebelrage", "logo": "logo2.png", "employee_count": "24", "location": "Москва", "description": "Мобильные сервисы, программное обеспечение, веб-сайты, мобильные приложения."},
    {"id": "3", "title": "staffingsmarter", "logo": "logo3.png", "employee_count": "123", "location": "Москва", "description": "Сервис онлайн-наблюдения за процессом сдачи экзамена с искусственным интеллектом"},
    {"id": "4", "title": "evilthreat h", "logo": "logo4.png", "employee_count": "36", "location": "Москва", "description": "Лидирующее в России и Восточной Европе ПО для проведения вебинаров и видео-конференций."},
    {"id": "5", "title": "hirey ", "logo": "logo5.png", "employee_count": "21", "location": "Воронеж", "description": "Телекоммуникационные и платежные сервисы, которые помогают развиваться бизнесам во всем мире."},
    {"id": "6", "title": "swiftattack", "logo": "logo6.png", "employee_count": "79", "location": "Москва", "description": "Разработка сложных веб-сервисов и мобильных приложений"},
    {"id": "7", "title": "troller", "logo": "logo7.png", "employee_count": "230", "location": "Санкт-Петербург", "description": "Мобильное приложение, позволяющее примерить обувь и выбрать идеальную пару всего в 3 клика"},
    {"id": "8", "title": "primalassault", "logo": "logo8.png","employee_count": "13", "location": "Москва", "description": "Реализуем проекты любой сложности в digital-сфере" }

]

""" Категории """

specialties = [

    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"}

]

