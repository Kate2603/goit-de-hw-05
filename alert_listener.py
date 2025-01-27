from confluent_kafka import Consumer, KafkaError
import json

# Налаштування споживача
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'alert-group',
    'auto.offset.reset': 'earliest'
})

# Підписка на топіки
consumer.subscribe(['temperature_alerts_alex', 'humidity_alerts_alex'])

while True:
    # Отримання повідомлення
    message = consumer.poll(1.0)
    if message is None:
        continue
    if message.error():
        if message.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Error while consuming: {message.error()}")
            continue

    # Декодування даних
    data = json.loads(message.value().decode('utf-8'))
    print(f"Received alert: {data}")

# Закриття споживача (не досягається в безкінечному циклі, але корисно для завершення)
consumer.close()