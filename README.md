# Link-shortener
 URL-адреса могут быть очень длинными и неудобными для пользователя. Здесь может пригодиться сокращатель URL. Средство сокращения URL-адресов сокращает количество символов в URL-адресе, облегчая его чтение, запоминание и распространение.
 
 ## Cтек технологий

- проект написан на Python3.10 с использованием веб-фреймворка Flask
- база данных - SQLlite
- система управления версиями - git

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
    git clone https://github.com/Evgenia789/link-shortener.git
```
```
    cd link-shortener
```
Cоздать и активировать виртуальное окружение:
```
    python -m venv env
```
```
    source venv/Scripts/activate
```
```
    python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
    pip install -r requirements.txt
```
Запустить проект:
```
    python3 manage.py runserver
```
____
Ваш проект запустился на http://127.0.0.1:5000/link_shortener 
