from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('zadatak1Topic_aggregated',
                         group_id='my-group1',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print ("value=%s" % (message.value))
