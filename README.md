fastapi_blog

Блог с использованием Fast Api
___
**Стэк технологий**
___
+ :rocket: Framework: FAST API
+ ORM: SQLAlchemy2.0
+ Migration: Alembic
+ Pydantic
+ :scroll: Poetry
+ :ship: Docker
+ :snake: Python 3.11
___
Перед запуском проекта необходимо создать сеть
```
sudo docker network create sirius_network
```
Для запуска проекта на локальном ПК используется следующая команда
```
sudo docker-compose up --build
```
___
Тест и разработка ведется на
```
OS : Arch Linux x86_64 
Kernel : 6.6.8-arch1-1
```
___
При запуске проекта разворачиваются контейнеры и соответствующие им образы со следующими именами:

|Имя контейнера        |Описание|
|----------------------|--------|
|prometheus            |Система мониторинга предназначенная для сбора и анализа метрических данных о работе приложений и инфраструктуры|
|grafana               |Открытое ПО для визуализации данных и мониторинга. Предоставляет гибкие инструменты для создания интерактивных и информативных дашбордов|
|web                   |Контейнер с основным проектом|
|fastapi_blog-console-1|Консоль приложения|
|fastapi_blog-kafka-1  |Распределенная система потоковой обработки и сообщений|
|web_db                |Контейнер с БД|
|fastapi_blog-minio-1  |Объектное хранилище данных с открытым исходным кодом, разработанное для обеспечения хранения и управления большими объемами данных в виде объектов|
|redis                 |Высокопроизводительная система управления базами данных, использующая в памяти хранение данных и работающая по принципу ключ-значение|
___
*Для просмотра контейнеров:*
```
sudo docker container ls
```

*Для просмотра образов:*
```
sudo docker image ls
```
*Для того чтобы просмотреть имеющиеся volume:*
```
sudo docker volume ls
```
*Для того чтобы очистить БД необходимо удалить volume:*
```
sudo docker volume rm [volume_name]
```
___
**После запуска проекта доступны:**

|Название     |URL  |
|-------------|-----|
|Документация | http://0.0.0.0:8000/swagger|
|Метрика      | http://0.0.0.0:8000/metrics|
|Prometheus   | http://0.0.0.0:9090|
|Redpanda     | http://0.0.0.0:8080|
|MinIO        | http://0.0.0.0:9001/login|
|Grafana      | http://0.0.0.0:3000/login|

- [X] Настройка docker
- [X] Настройка миграций
- [X] Настройка моделей
**Эндпоинты**
- [ ] Регистрация пользователя
- [ ] Login
- [ ] Logout
- [ ] Создание поста
- [ ] Редактирование поста
- [ ] Комментирование поста
