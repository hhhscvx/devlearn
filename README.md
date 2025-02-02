[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/hhhscvx)

## О проекте
**[DevLearn]** Обучающая платформа на `Django`, в которой есть:
- [Авторизация](https://github.com/hhhscvx/devlearn/tree/master/.github/images/login.png)
- [Профили у каждого пользователя](https://github.com/hhhscvx/devlearn/tree/master/.github/images/profile.png)
- Проходить курс можно только авторизовавшись
- [Возможность поступить на курс](https://github.com/hhhscvx/devlearn/tree/master/.github/images/course_detail.png)
- [У каждого курса список уроков](https://github.com/hhhscvx/devlearn/tree/master/.github/images/course_detail.png)
- [Возможность смотреть уроки курса (Youtube API)](https://github.com/hhhscvx/devlearn/tree/master/.github/images/lesson_detail.png)
- [У каждого урока кнопка "Урок пройден"](https://github.com/hhhscvx/devlearn/tree/master/.github/images/lesson_detail.png)
- [Отслеживание процента прохождения курса](https://github.com/hhhscvx/devlearn/tree/master/.github/images/set_review_error.png)
- [Отзывы у курсов, которые можно оставлять после прохождения 80% его уроков](https://github.com/hhhscvx/devlearn/tree/master/.github/images/set_review.png)

## Доработки (TODO)
1. Улучшение профиля пользователя, взаимодействие с ним
2. Возможность стать преподавателем и добавлять курсы
3. Деплой на Nginx & Gunicorn

## Запустить проект
- `docker-compose up --build`

## Технологии, использованные в проекте
1. Backend на `Django`
2. Frontend на `JavaScript` & `HTML` & `CSS`
3. REST API на `Django Rest Framework`
4. База Данных `PostgreSQL` 
5. Система кеширования и брокер сообщений `Redis`
6. Очереди задач `Celery` & `Flower`
7. Контейнеризация `Docker`
8. Бизнес-логика в модуле `services`, а не во `views`

## Изображения функционала:

![img1](.github/images/login.png)
![img2](.github/images/register.png)
![img3](.github/images/courses_list.png)
![img4](.github/images/course_detail.png)
![img5](.github/images/course_reviews.png)
![img6](.github/images/set_review.png)
![img7](.github/images/set_review_error.png)
![img8](.github/images/lesson_detail.png)
![img9](.github/images/lesson_comments.png)
![img10](.github/images/profile.png)
