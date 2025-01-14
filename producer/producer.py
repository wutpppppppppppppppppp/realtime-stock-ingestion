import logging
import random
import time
import json
from kafka import KafkaProducer

logging.basicConfig(level=logging.DEBUG)

try:
    # Connect to the Kafka broker using the Docker container hostname
    producer = KafkaProducer(
        bootstrap_servers='broker:9092',
        api_version=(0, 10, 2),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print("Kafka producer created successfully.")
except Exception as e:
    print(f"Error creating Kafka producer: {e}")
    exit(1)

while True:
    try:
        stock_data = {
            'symbol': random.choice(['AAPL', 'GOOG', 'MSFT', 'AMZN']),
            'price': round(random.uniform(100, 1500), 2),
            'timestamp': time.time()
        }
        print("Stock data created:", stock_data)
        producer.send('stock_prices', stock_data)
        print(f"Sent: {stock_data}")
        time.sleep(1)
    except Exception as e:
        print(f"Error sending message: {e}")
