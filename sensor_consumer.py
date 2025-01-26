import json
from kafka import KafkaConsumer, KafkaProducer

# Налаштування споживача
consumer = KafkaConsumer('your_name_building_sensors',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                         auto_offset_reset='earliest',
                         enable_auto_commit=True)

# Налаштування продюсера для сповіщень
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for message in consumer:
    data = message.value
    sensor_id = data['sensor_id']
    temperature = data['temperature']
    humidity = data['humidity']
    
    if temperature > 40:
        alert = {
            'sensor_id': sensor_id,
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': data['timestamp'],
            'message': 'Temperature alert: exceeds 40°C'
        }
        producer.send('your_name_temperature_alerts', value=alert)
        print(f"Temperature alert sent: {alert}")

    if humidity > 80 or humidity < 20:
        alert = {
            'sensor_id': sensor_id,
            'temperature': temperature,
            'humidity': humidity,
            'timestamp': data['timestamp'],
            'message': 'Humidity alert: out of range'
        }
        producer.send('your_name_humidity_alerts', value=alert)
        print(f"Humidity alert sent: {alert}")