import random
import time
import json
from confluent_kafka import Producer

# Налаштування продюсера
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Генерація даних
sensor_id = random.randint(1, 100)  # Випадковий ID датчика

while True:
    temperature = random.randint(25, 45)
    humidity = random.randint(15, 85)
    timestamp = time.time()

    data = {
        'sensor_id': sensor_id,
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity
    }

    # Відправка даних у топік
    producer.produce('building_sensors_alex', json.dumps(data).encode('utf-8'))
    print(f"Sent data: {data}")

    producer.flush()  # Переконайтеся, що всі повідомлення відправлені

    time.sleep(5)  # Затримка між відправленнями