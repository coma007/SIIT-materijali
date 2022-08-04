import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))

moguci_tipovi_kartica = ['MasterCard', 'Visa', 'Dina', 'American Express']

while True:
    n = int(input("Koliko transakcija zelite da generisete: "))
    for _ in range(n):
        producer.send('primer3Topic', value = {
            'tip_kartice': random.choice(moguci_tipovi_kartica),
            'kolicina': random.randint(100,10000)
        })
    producer.flush()