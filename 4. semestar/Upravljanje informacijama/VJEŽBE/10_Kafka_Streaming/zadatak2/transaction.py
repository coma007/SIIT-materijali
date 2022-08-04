import faust
import datetime

app = faust.App('transaction_worker', broker='kafka://localhost:9092')


class Query(faust.Record):
    id: int
    query_type: str
    valid: bool
    result: str


validated_topic = app.topic('zadatak2validated', value_type=Query)
execute_topic = app.topic('zadatak2execute', value_type=Query)
executed_topic = app.topic('zadatak2executed', value_type=Query)


queries_data = {}


@app.agent(validated_topic)
async def recieve_validation(queries: faust.Stream):
    global queries_data

    async for query in queries:
        if query.id not in queries:
            queries_data[query.id] = {"select": 0, "modify": 0}
        if query.query_type.upper() == "SELECT":
            queries_data[query.id]["select"] += 1
        else:
            if queries_data[query.id]["modify"] == 1:
                print("Blocked query: ", query)
                continue
            else:
                queries_data[query.id]["update"] = 1
        print("Starting query: ", query)
        await execute_topic.send(value=query)


@app.agent(executed_topic)
async def recieve_execution(queries: faust.Stream):
    async for query in queries:
        print("Done query: ", query)
        action = "modify"
        if query.query_type.upper() == "SELECT":
            action = "select"
        queries_data[query.id][action] -= 1
