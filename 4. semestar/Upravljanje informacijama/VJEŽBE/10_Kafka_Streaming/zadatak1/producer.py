import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))

while True:
    n = int(input("Koliko transakcija zelite da generisete: "))
    for _ in range(n):
        producer.send('zadatak1Topic', value = {
            'broj_kartice': random.randint(10000000000010, 10000000000020),
            'kolicina': random.randint(100,10000)
        })
    producer.flush()
