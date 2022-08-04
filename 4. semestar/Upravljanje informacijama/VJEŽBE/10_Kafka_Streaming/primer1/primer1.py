import faust

# PRE POKRETANJA PRIMERA TREBA
# 1. Pokrenuti docker compose
# 2. 'Uci' u kontejner gde je pokrenut kafka broker: docker exec -it broker bash 
# 3. Kreirati primer1Topic: /bin/kafka-topics --create --bootstrap-server localhost:9092 -replication-factor 1 --partitions 1 --topic primer1Topic
# 4. Ako ste vec pokrtali faust worker-a, potrebno je da ga ugasite (Ctrl-C) pre nego sto pokrenete novog
# POKRETANJE PRIMERA
# 1. U terminalu se pozicionirate u direktorijum gde se nalazi ovaj python fajl
# 2. Faust 'workera' pokrecemo sa komandom: faust -A naziv_worker-a worker -l info
# naziv_worker-a zameniti nazivom python fajla bez .py ekstenzije (sto bi u ovom primeru bilo 'primer1')
app = faust.App('primerApp', broker = 'kafka://localhost:9092')
topic = app.topic('primer1Topic')

@app.agent(topic)
async def orders_agent(transakcije: faust.Stream):
    async for transakcija in transakcije:
        print(transakcija)
