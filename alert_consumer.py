import json
from kafka import KafkaConsumer

# Налаштування споживача для обох топіків
consumer = KafkaConsumer('alex_temperature_alerts',
                         'alex_humidity_alerts',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                         auto_offset_reset='earliest',
                         enable_auto_commit=True)

for message in consumer:
    alert = message.value
    print(f"Received alert: {alert}")