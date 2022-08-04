from rdflib import Graph
from pyfuseki import FusekiUpdate

g = Graph()

g.parse('./data/rdf/person_metadata.nt')
#g.parse('./data/rdf/person_metadata.rdf')
fuseki = FusekiUpdate('http://localhost:3030', 'dataset')
fuseki.insert_graph(g)
