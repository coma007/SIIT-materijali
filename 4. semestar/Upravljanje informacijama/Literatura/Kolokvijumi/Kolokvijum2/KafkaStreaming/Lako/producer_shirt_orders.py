import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))

tshirt_brands = ["Nike", "Adidas", "Polo", "Uniqlo"]
tshirt_size = ["XL", "L", "M", "S"]

for _ in range(100):
    producer.send('orders', value = {
        'brand': random.choice(tshirt_brands),
        'size': random.choice(tshirt_size)
    })
    producer.flush()
