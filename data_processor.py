from confluent_kafka import Consumer, KafkaError, Producer
import json

# Налаштування споживача
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'sensor-group',
    'auto.offset.reset': 'earliest'
})

# Підписка на топік
consumer.subscribe(['building_sensors_alex'])

# Налаштування продюсера
producer = Producer({'bootstrap.servers': 'localhost:9092'})

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
    sensor_id = data['sensor_id']
    temperature = data['temperature']
    humidity = data['humidity']
    timestamp = data['timestamp']

    # Фільтрація даних
    if temperature > 40 or humidity > 80 or humidity < 20:
        print(f"Filtered data: {data}")

        # Відправка сповіщення про температуру
        if temperature > 40:
            alert_message = {
                'sensor_id': sensor_id,
                'timestamp': timestamp,
                'temperature': temperature,
                'message': 'Temperature alert: exceeds 40°C'
            }
            producer.produce('temperature_alerts_alex', json.dumps(alert_message).encode('utf-8'))
            print(f"Temperature alert sent: {alert_message}")

        # Відправка сповіщення про вологість
        if humidity > 80 or humidity < 20:
            alert_message = {
                'sensor_id': sensor_id,
                'timestamp': timestamp,
                'humidity': humidity,
                'message': 'Humidity alert: out of range'
            }
            producer.produce('humidity_alerts_alex', json.dumps(alert_message).encode('utf-8'))
            print(f"Humidity alert sent: {alert_message}")

    # Відправка всіх повідомлень
    producer.flush()