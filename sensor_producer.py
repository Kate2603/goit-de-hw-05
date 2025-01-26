import json
import random
import time
from kafka import KafkaProducer

# Налаштування продюсера
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


sensor_id = random.randint(1, 100)  # Випадковий ID датчика

while True:
    # Генерація випадкових значень для температури та вологості
    temperature = random.randint(20, 50)  # Діапазон температури від 20 до 50
    humidity = random.randint(10, 90)      # Діапазон вологості від 10 до 90
    data = {
        'sensor_id': sensor_id,
        'timestamp': time.time(),
        'temperature': temperature,
        'humidity': humidity
    }
    
    # Відправка даних до топіка
    producer.send('your_name_building_sensors', value=data)
    print(f"Sent data: {data}")
    
    # Відправляти дані кожні 10 секунд
    time.sleep(10)  # Змінено на 10 секунд