import requests
import pprint

query = """SELECT ?s WHERE 
    {?s ?o "London"}"""

result = requests.post('http://localhost:3030/dataset/sparql', 
    params={'query': query})
result = result.json()['results']['bindings']

pprint.pprint(result)