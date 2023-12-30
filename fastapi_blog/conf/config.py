from typing import List

from pydantic_settings import BaseSettings # pydantic_settings


class Settings(BaseSettings): # наследуется от BaseSettings
    BIND_IP: str
    BIND_PORT: int
    DB_URL: str #URL для подключения к базе данных, используемой приложением

    JWT_SECRET_SALT: str #секретная строка, используемая для генерации JWT-токенов, которые используются для аутентификации пользователей

    KAFKA_BOOTSTRAP_SERVERS: List[str] #список адресов Kafka-брокеров, которые будут использоваться для отправки и получения сообщений

    KAFKA_TOPIC: str #название топика Kafka, в который будут отправляться сообщения


settings = Settings() #экземпляр класса Settings, который содержит значения конфигурационных параметров

# Конфигурация проекта определяет, какие параметры сборки и компилятора используются при сборке проекта.
# набор параметров и настроек, определяющих работу программного обеспечения или системы.
# если приложение запускается в режиме разработки (dev), то значения параметров могут быть настроены для локальной разработки, а если в продакшене (prod) - для более высокой надежности и производительности.