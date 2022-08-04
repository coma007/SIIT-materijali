from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('test',
                         auto_offset_reset='earliest',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print("test")
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))