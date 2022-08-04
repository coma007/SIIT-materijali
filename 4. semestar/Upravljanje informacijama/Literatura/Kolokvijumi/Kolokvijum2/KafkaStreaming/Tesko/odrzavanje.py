from kafka import KafkaConsumer, KafkaProducer
import json
import time
import random

consumer = KafkaConsumer('zahtjevi_obrada_odrzavanje',
                         group_id='odrzavanje',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))
for zahtev in consumer:
    print ("zahtev=%s" % (zahtev.value))
    # time.sleep(random.randint(1,5))
    odgovor ={
        "id_zahteva": zahtev.value['id_zahteva'],
        "zahtev_odobren": random.choice([True,True,True,False])
    }
    producer.send('obrada_odgovori_odrzavanje', value = odgovor)
    producer.flush()
