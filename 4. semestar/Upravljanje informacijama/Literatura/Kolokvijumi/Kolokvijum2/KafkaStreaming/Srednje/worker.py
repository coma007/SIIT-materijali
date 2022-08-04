import faust

class TShirt(faust.Record):
    brand : str
    size : str

app = faust.App('shirts-app', broker='kafka://localhost')
incoming_topic = app.topic("tshirt_orders", value_type=TShirt)
outgoing_topic_fullfiled = app.topic("fullfiled", value_type=TShirt)
outgoing_topic_non_fullfiled = app.topic("non_fullfiled", value_type=TShirt)

@app.agent(incoming_topic)
async def recieve_tshirts(tshirts: faust.Stream):
    async for tshirt in tshirts:
        if tshirt.size.strip().upper() == "XXL":
            await outgoing_topic_non_fullfiled.send(value={
                "brand": tshirt.brand,
                "size": tshirt.size
            })
        else:
            await outgoing_topic_fullfiled.send(value={
                "brand": tshirt.brand,
                "size": tshirt.size
            })
