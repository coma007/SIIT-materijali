from rdflib import Graph
from pyfuseki import FusekiUpdate

g = Graph()

g.parse('putanja do fajla.nt')
#g.parse('putanja do fajla.rdf')
fuseki = FusekiUpdate('http://localhost:3030', 'dataset');
fuseki.insert_graph(g)
