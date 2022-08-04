from kafka import KafkaProducer, KafkaConsumer
import json
import time

consumer = KafkaConsumer('zadatak2generated',
                         group_id='validator',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))

for message in consumer:
    passes = False
    query_type = message.value["query_type"].upper()
    if query_type in ["SELECT", "IMPORT", "UPDATE", "DELETE"]:
        passes = True
    producer.send("zadatak2validated", value={
        "id": message.value["id"],
        "query_type": message.value["query_type"],
        "valid": passes
    })
    producer.flush()
