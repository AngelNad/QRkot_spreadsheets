# Благотворительный фонд поддержки котиков QRKot
# QRkot_spreadseets

### Описание
Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.<br>

В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.<br>
Интегрирован Google API: есть возможность формирования отчёта в гугл-таблице, чтобы узнать какие проекты быстрее всего закрываются.

### Используемые технологии
+ Python
+ FastAPI
+ SQLAlchemy
+ Pydantic
+ Uvicorn
+ Alembic
+ Google API

### Как запустить проект

Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/AngelNad/QRkot_spreadsheets.git
```
```
cd QRkot_spreadsheets/
```

Установите и активируйте виртуальное окружение:

```
python3 -m venv env
```
```
source env/bin/activate
```

Установите зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Заполнение файла .env
Создайте файл .env с переменными окружения для работы с базой данных со значениями:<br>
```
APP_TITLE=Благотворительный фонд поддержки котиков QRKot
APP_DESCRIPTION=Сервис сбора пожертвований для Благотворительного фонда поддержки котиков
DATABASE_URL=dialect+driver://username:password@host:port/database # расположение базы данных
SECRET=secret_key # секретный ключ приложения
FIRST_SUPERUSER_EMAIL=admin@yandex.ru # email для создания суперюзера
FIRST_SUPERUSER_PASSWORD=admin # пароль для создания суперюзера
# Переменные ниже заполняются из JSON-файла с информацией о вашем сервисном аккаунте Google Cloude Platform
TYPE_ACCOUNT=service_account
PROJECT_ID=...
PRIVATE_KEY_ID=...
PRIVATE_KEY="..."
CLIENT_EMAIL=...
CLIENT_ID=...
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=...
EMAIL=email # ваш личный гугл-аккаунт
```

Выполните миграции:
```
alembic upgrade head
```

Запустите приложение:
```
uvicorn app.main:app --reload
```
_Реализовано автоматическое создание первого суперюзера после запуска._<br>
_Для этого в файле .env указаны необходимые данные._


### Автор:
+ Надежда Осипова - [AngelNad](https://github.com/AngelNad)