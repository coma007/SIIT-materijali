from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'))

producer.send('primer1Topic', value ={'tip_kartice': 'MasterCard', 'kolicina': 12345})
producer.send('primer1Topic', value ={'tip_kartice': 'MasterCard', 'kolicina': 12345})
producer.send('primer1Topic', value ={'tip_kartice': 'Visa', 'kolicina': 12345})
producer.send('primer1Topic', value ={'tip_kartice': 'Visa', 'kolicina': 12345})
producer.send('primer1Topic', value ={'tip_kartice': 'AmericanExpress', 'kolicina': 12345})
producer.flush()
