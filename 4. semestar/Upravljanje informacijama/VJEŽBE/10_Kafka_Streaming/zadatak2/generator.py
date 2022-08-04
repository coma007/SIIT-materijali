import random
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))


producer.send('zadatak2generated',
              value={'id': 1,
                     'query_type': "SELECT"})
producer.send('zadatak2generated',
              value={'id': 1,
                     'query_type': "SELECT"})
producer.send('zadatak2generated',
              value={'id': 2,
                     'query_type': "INSERT"})
producer.send('zadatak2generated',
              value={'id': 3,
                     'query_type': "DELETE"})
producer.send('zadatak2generated',
              value={'id': 2,
                     'query_type': "DELETE"})
producer.send('zadatak2generated',
              value={'id': 2,
                     'query_type': "UPDATE"})
print("Sending query")
producer.flush()
