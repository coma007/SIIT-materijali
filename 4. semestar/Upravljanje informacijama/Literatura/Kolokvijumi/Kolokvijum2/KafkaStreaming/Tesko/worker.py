import faust

class Request(faust.Record):
    id_zahteva : str
    broj_sale : str

class Answer(faust.Record):
    id_zahteva : str
    zahtev_odobren : str

app = faust.App("ambulance-app", broker='kafka://localhost')

incoming_requests = app.topic("zahtevi_za_termine", value_type=Request)
outgoing_requests = app.topic("odgovori_na_zahteve", value_type=Answer)

outgoing_service_uprava = app.topic("zahtjevi_obrada_uprava", value_type=Request)
outgoing_service_hirurski = app.topic("zahtjevi_obrada_hirurski", value_type=Request)
outgoing_service_odrzavanje = app.topic("zahtjevi_obrada_odrzavanje", value_type=Request)
incoming_service_uprava = app.topic("obrada_odgovori_uprava", value_type=Answer)
incoming_service_hirurski = app.topic("obrada_odgovori_hirurski", value_type=Answer)
incoming_service_odrzavanje = app.topic("obrada_odgovori_odrzavanje", value_type=Answer)

@app.agent(incoming_requests)
async def recieve_requests(requests: faust.Stream):
    async for request in requests:
        print("Request sent to uprava!")
        await outgoing_service_uprava.send(value=request)
        print("Request sent to hirurski!")
        await outgoing_service_hirurski.send(value=request)
        print("Request sent to odrzavanje!")
        await outgoing_service_odrzavanje.send(value=request)


zahtjevi = {}


@app.agent(incoming_service_uprava)
async def recieve_answers(answers: faust.Stream):
    async for answer in answers:
        print("Answer recieved from uprava !")
        procces_answer(answer)

@app.agent(incoming_service_hirurski)
async def recieve_answers(answers: faust.Stream):
    async for answer in answers:
        print("Answer recieved from hirurski!")
        procces_answer(answer)

@app.agent(incoming_service_odrzavanje)
async def recieve_answers(answers: faust.Stream):
    async for answer in answers:
        print("Answer recieved from odrzavanje !")
        procces_answer(answer)


def procces_answer(answer):
    global zahtjevi
    if answer.id_zahteva not in zahtjevi:
        zahtjevi[answer.id_zahteva] = [answer.zahtev_odobren]
    else:
        zahtjevi[answer.id_zahteva].append(answer.zahtev_odobren)


async def send_answers():
    for zahtjev in zahtjevi:
        print("Answer sent !")
        if zahtjevi[zahtjev] == [True, True, True]:
            odobren = True
        else:
            odobren = False
        await outgoing_requests.send(value={
            "id_zahteva": zahtjev,
            "zahtev_odobren": odobren
        })
