import faust

app = faust.App('primerApp', broker = 'kafka://localhost:9092')

class Transakcija(faust.Record):
    tip_kartice: str
    kolicina: int
    
topic = app.topic('primer3Topic', value_type=Transakcija)

suma_po_tipu = {}

@app.agent(topic)
async def orders_agent(transakcije: faust.Stream):
    global suma_po_tipu
    async for transakcija in transakcije:
        if transakcija.tip_kartice in suma_po_tipu:
            suma_po_tipu[transakcija.tip_kartice]+=transakcija.kolicina
        else:
            suma_po_tipu[transakcija.tip_kartice]=transakcija.kolicina
        print(suma_po_tipu)

outgoing_topic = app.topic('primer3Topic_aggregated', value_type=Transakcija)

@app.timer(interval=5.0)
async def send_aggregated_data():
    global suma_po_tipu
    print('Sending Agregated Data')
    await outgoing_topic.send(value=suma_po_tipu)
    suma_po_tipu = {}
