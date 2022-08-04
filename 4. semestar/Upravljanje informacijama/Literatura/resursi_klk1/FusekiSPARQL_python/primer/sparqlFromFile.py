import requests
import pprint
import os

dir_path=os.fsencode('./data/sparql')
for i, filename in enumerate(sorted(os.listdir(dir_path))):
    with open(os.path.join(dir_path,filename)) as file:
        query = file.read()
        
        print("QUERY "+str(i+1))
        result = requests.post('http://localhost:3030/dataset/sparql', 
            params={'query': query})
        result = result.json()['results']['bindings']

        pprint.pprint(result)

