import faust

app = faust.App('primerApp', broker = 'kafka://localhost:9092')

class Transakcija(faust.Record):
    tip_kartice: str
    kolicina: int
    
topic = app.topic('primer2Topic', value_type=Transakcija)

prvo_vrijeme = {}

@app.agent(topic)
async def orders_agent(transakcije: faust.Stream):
    async for transakcija in transakcije:
        if transakcija.tip_kartice in prvo_vrijeme:
            prvo_vrijeme[transakcija.tip_kartice]+=transakcija.kolicina
        else:
            prvo_vrijeme[transakcija.tip_kartice]=transakcija.kolicina
        print(prvo_vrijeme)
