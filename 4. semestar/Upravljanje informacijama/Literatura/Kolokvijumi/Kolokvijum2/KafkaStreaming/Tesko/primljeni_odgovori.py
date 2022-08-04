from kafka import KafkaConsumer, KafkaProducer
import json
import time
import random

consumer = KafkaConsumer('odgovori_na_zahteve',
                         group_id='primljeni_odgovori',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
for zahtev in consumer:
    print ("zahtev=%s" % (zahtev.value))
