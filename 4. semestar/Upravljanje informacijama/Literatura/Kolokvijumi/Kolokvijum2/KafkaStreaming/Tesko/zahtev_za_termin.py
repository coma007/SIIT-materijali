from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))

zahtevi = [
        {
            "id_zahteva": "LXA25",
            "broj_sale": 2
        },
        {
            "id_zahteva": "MLT11",
            "broj_sale": 3
        },
        {
            "id_zahteva": "FTY58",
            "broj_sale": 4
        },
        {
            "id_zahteva": "LPO01",
            "broj_sale": 3
        }
]

for zahtev in zahtevi:
    producer.send('zahtevi_za_termine', value = zahtev)
    producer.flush()
