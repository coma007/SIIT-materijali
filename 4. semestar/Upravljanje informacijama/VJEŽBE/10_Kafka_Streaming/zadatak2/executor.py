from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer('zadatak2execute',
                         group_id='executor',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))


for message in consumer:
    producer.send("zadatak2executed", value={
        "id": message.value["id"],
        "query_type": message.value["query_type"],
        "result": "Heh"
    })
    print("Executing query")
    producer.flush()
