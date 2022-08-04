from pymongo import MongoClient
import json

client = MongoClient('mongodb://root:root@localhost:27017')

db = client['vezbe04']
collection = db['primer01']

# json_data = json.load(open('sample1.json'))

# Upisivanje liste dokumenata
# collection.insert_many(json_data)

# Citanje i ispis svih dokumenata
# cursor = collection.find()
# for doc in cursor:
#     print(doc)

# cursor = collection.find({"firstName": {"$nin": ["Jane", "Joe"]}})
# for doc in cursor:
#    print(doc)
#

print("Query 0: Dobaviti sve dokumente iz kolekcije")
cursor = collection.find()
for doc in cursor:
    print(doc)

print("\nQuery 1: Dobaviti sve muškarce")
cursor = collection.find({"gender": "male"})
for doc in cursor:
    print(doc)

print("\nQuery 2: Dobaviti sve muškarce z Subotice")
cursor = collection.find({"gender": "male", "from": "Subotica"})
for doc in cursor:
    print(doc)

print("\nQuery 3: Dobaviti sve žene koje imaju više od 30 godina")
cursor = collection.find({"gender": "female", "age": {"$gt": 30}})
for doc in cursor:
    print(doc)

print("\nQuery 4: Dobaviti sve žene koje imaju više od 30 godina i manje od 50 godina")
cursor = collection.find({"gender": "female", "age": {"$gt": 30, "$lt": 50}})
for doc in cursor:
    print(doc)

print("\nQuery 5: Dobaviti sve osobe čiji broj počinje sa cifrom 1 i završava se sa cifrom 1")
cursor = collection.find({"number": {"$regex": "^1.*1$"}})
# cursor = collection.find({"$and" : [{"number": {"$regex": "^1"}}, {"number": {"$regex": "1$"}}]})
for doc in cursor:
    print(doc)

print("\nQuery 6: Dobaviti sve osobe koje žive ili u Subotici ili u Novom Sad-u")
cursor = collection.find({"from": {"$in": ["Novi Sad", "Subotica"]}})
for doc in cursor:
    print(doc)

print("\nQuery 7: Koliko ima ljudi koji žive u Subotici")
aggregation = collection.aggregate([{"$group": {"_id": "$from", "number of people": {"$count": {}}}}, {"$match": {"_id": "Subotica"}}])
for doc in aggregation:
    print(doc)

print("\nQuery 8: Prosečan broj godina u zavisnosti od pola osobe")
aggregation = collection.aggregate([{"$group": {"_id": "$gender", "age average": {"$avg": "$age"}}}])
for doc in aggregation:
    print(doc)

print("\nQuery 9: Za svai grad ispisati koliko godina ima najstarija osoba")
aggregation = collection.aggregate([{"$group": {"_id": "$from", "age of oldest": {"$max": "$age"}}}])
for doc in aggregation:
    print(doc)

print("\nQuery 10: Za svaki grad ispisati ime i prezime najstarije osobe")
aggregation = collection.aggregate([{"$group": {"_id": "$from", "age of oldest": {"$max": "$age"}, "firstName": {"$first": "$firstName"}, "lastName": {"$first": "$lastName"}}}])
for doc in aggregation:
    print(doc)
# aggregation = collection.aggregate([{"$sort": {"age": 1}}, {"$group": {"_id": "$from", "firstName": {"$first": "$firstName"}, "lastName": {"$first": "$lastName"}}}])
# for doc in aggregation:
#     print(doc)


print("\n\n")
# aggregation = collection.aggregate([{"$match": {"from": {"$in": ["Subotica", "Los Angeles"]}}}, {"$sort": {"age" : 1}}])
# aggregation = collection.aggregate([{"$group": {"_id": {"gender": "$gender", "city": "$from"}}}])


# aggregation =  collection.aggregate([{"$group":{"_id":"$from"}}])
# aggregation =  collection.aggregate([{"$group":{"_id":"$from", "broj":{"$count":{}}}}])
# aggregation =  collection.aggregate([{"$match":{"from":{"$in":["Subotica","Novi Sad"]}}},
#                                     {"$group":{"_id":"$from", "broj":{"$count":{}}}}])
# aggregation =  collection.aggregate([
#     {"$sort":{"age":-1}},
#     {"$group":{
#         "_id":"$from",
#         "max_god":{"$max":"$age"},
#         "naziv":{"$first":"$firstName"}
#     }}
# # ])
# for doc in aggregation:
#     print(doc)
client.close()
