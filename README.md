# Тестовое задание

Сделать базовое API с методом uploadText,
принимающее переменную txt.
Сделать страницу, в которой находится
поле, содержимое которого можно
передать через AJAX на API.
В админке сделать возможность удалить
выбранные полученные данные.
Сделать вторую страницу, которая
через API метод getText получает список
хранимых строк и отображает его.
Результат залить в гит.

# Минимальные требования для деплоя проекта
1) ОС: linux Ubuntu/Debian
2) Налличие предустановленного python3.5 и virtualenv

# Деплой
1) Спулить проект ```git clone https://github.com/ckcnik/kvadra.git```
2) Создать конфиг-файл из семпла ```kvadra/settings.sample.py```
3) Запустить скрипт ```sh build_env.sh```. Дождаться установки всех пакетов.
4) Активировать виртуальное окружение ```source env/bin/activate```
5) Запустить миграции ```python manage.py migrate```
6) Создать суперпользователя ```python manage.py createsuperuser```
6) Запустить проект ```python manage.py runserver 8000```
7) Открыть в броузере урлу http://127.0.0.1:8000/

# Руководство пользователя
1) Страница с формой находится тут http://127.0.0.1:8000/
2) Список текстов находится тут - http://127.0.0.1:8000/list/
3) Админка тут - http://127.0.0.1:8000/admin/
