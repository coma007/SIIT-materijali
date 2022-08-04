import faust

class TShirt(faust.Record):
    brand: str
    size: str

app = faust.App('myapp', broker='kafka://localhost')
tshirts_recieve_topic = app.topic('orders', key_type=str, value_type=TShirt)
tshirts_send_topic = app.topic('orders_count', key_type=str, value_type=TShirt)

tshirt_data = {}

@app.agent(tshirts_recieve_topic)
async def process_order(orders: faust.Stream):
    global tshirt_data
    async for order in orders:
        brand, size = order.brand.strip().upper(), order.size.strip().upper()
        if brand in tshirt_data:
            tshirt_data[brand] += 1
        else:
            tshirt_data[brand] = 1
        if size in tshirt_data:
            tshirt_data[size] += 1
        else:
            tshirt_data[size] = 1


async def send_counts():
    global tshirt_data
    for key in tshirt_data:
        await tshirts_send_topic.send(value={
            "type": key,
            "count": tshirt_data[key]
            }
        )
