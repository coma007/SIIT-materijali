from pymongo import MongoClient
import json

client = MongoClient('mongodb://root:root@localhost:27017')

db = client['vezbe04']
collection = db['primer01']

json_data=json.load(open('data.json'))

#Upisivanje liste dokumenata
collection.insert_many(json_data)

# Citanje i ispis svih dokumenata
cursor = collection.find()
for doc in cursor:
    print(doc)

# Za jednostavne upite (ne agregacije) se koristi ova metoda:
cursor = collection.find("upit")
for doc in cursor:
    print(doc)

# Za agregacije se koristi ova metoda:
aggregation =  collection.aggregate([
	"niz upita koji se izvrsavaju unutar agregacije"
])

for doc in aggregation:
    print(doc)
client.close()
