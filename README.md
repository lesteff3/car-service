Это готовый кейс для автодилеров.
--------------------------------------------------------------------------------------------
РАБОЧИЙ ПОТОК :

Клонирование проекта и установка requirements.txt:

git clone https://github.com/lesteff3/car-service.git

sudo pip install -r requirements.txt

Сделать миграций:

python manage.py makemigrations

python manage.py migrate

Создание Admin User:

python manage.py createsuperuser

Запуск приложение

python manage.py runserver
--------------------------------------------------------------------------------------------
После этого вы сможете увидеть мой первый проект.
В данном проекте реализована функция:
          "Регистрация"
          "Личный кабинет Пользователя"
          "Аренда-Автомобиля на прокат"
          "Оставлять отзывы!"
              Welcome!
