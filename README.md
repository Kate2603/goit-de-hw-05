# goit-de-hw-05

Кроки для запуску

## 1 У першому терміналі запустіть Zookeeper

- В терміналі ПК

cd C:\kafka\kafka_2.12-3.8.0\bin\windows
.\zookeeper-server-start.bat ..\..\config\zookeeper.properties

## 2 У другому терміналі запустіть Kafka сервер

cd C:\kafka\kafka_2.12-3.8.0\bin\windows
.\kafka-topics.bat --list --bootstrap-server localhost:9092

## 3 Створіть топіки

cd C:\kafka\kafka_2.12-3.8.0\bin\windows
.\kafka-topics.bat --create --topic alex_building_sensors --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
.\kafka-topics.bat --create --topic alex_temperature_alerts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
.\kafka-topics.bat --create --topic alex_humidity_alerts --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

## 4 Запустіть продюсера

- Відкрийте новий термінал ВС Коду і запустіть sensor_producer.py:

python sensor_producer.py

## 5 Запустіть споживача для сповіщень

- Відкрийте ще один термінал і запустіть alert_consumer.py:

python alert_consumer.py

## 6 Запустіть споживача для даних з датчиків

-Відкрийте ще один термінал і запустіть alert_consumer.py:

python alert_consumer.py

## 7 Запустіть споживача для даних з датчиків

- Відкрийте ще один термінал і запустіть sensor_consumer.py:

python sensor_consumer.py

Перевірте топіки:

## Виконайте команду для переліку топіків, щоб переконатися, що вони існують

- В терміналі ПК

cd C:\kafka\kafka_2.12-3.8.0\bin\windows
.\kafka-topics.bat --list --bootstrap-server localhost:9092

### Перевірка роботи

Переконайтеся, що всі три скрипти працюють:

- sensor_producer.py повинен надсилати дані до топіка your_name_building_sensors кожні 5 секунд.

- sensor_consumer.py повинен отримувати дані з топіка your_name_building_sensors і перевіряти умови для температури та вологості.

- alert_consumer.py повинен отримувати сповіщення з топіків your_name_temperature_alerts і your_name_humidity_alerts.
