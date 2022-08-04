import faust
import datetime

app = faust.App('primerApp', broker = 'kafka://localhost:9092')

class Transakcija(faust.Record):
    broj_kartice: int
    kolicina: int

topic = app.topic('zadatak1Topic', value_type=Transakcija)

prvo_vrijeme = {}
brojac_minut = {}
blokirane = []
slanje_transakcija = []

@app.agent(topic)
async def orders_agent(transakcije: faust.Stream):
    global prvo_vrijeme
    async for transakcija in transakcije:
        datum = datetime.datetime.now()
        if transakcija.broj_kartice in blokirane:
            continue
        if transakcija.broj_kartice in prvo_vrijeme:
            if prvo_vrijeme[transakcija.broj_kartice] + datetime.timedelta(minutes=1) > datum:
                brojac_minut[transakcija.broj_kartice] += 1
                if brojac_minut[transakcija.broj_kartice] >= 5:
                    blokirane.append(transakcija.broj_kartice)
                else:
                    slanje_transakcija.append(f"br: {transakcija.broj_kartice}  kol: {transakcija.kolicina} dat: {datum}")
            else:
                prvo_vrijeme[transakcija.broj_kartice] = datum
                brojac_minut[transakcija.broj_kartice] = 0
        else:
            prvo_vrijeme[transakcija.broj_kartice] = datum
            brojac_minut[transakcija.broj_kartice] = 0

outgoing_topic = app.topic('zadatak1Topic_aggregated', value_type=Transakcija)

@app.timer(interval=5.0)
async def send_aggregated_data():
    global blokirane
    print('Sending Agregated Data')
    await outgoing_topic.send(value=blokirane)
    # slanje_transakcija = []
