from rdflib import Graph, URIRef, Literal
from pyfuseki import FusekiUpdate

g = Graph()

#g.add(('<http://byHand/subject1>', '<http://byHand/hasName>', 'Adam'))
g.add((URIRef('http://byHand/subject1'), URIRef('http://byHand/hasName'), Literal('Adam')))
fuseki = FusekiUpdate('http://localhost:3030', 'byHand')
fuseki.insert_graph(g)
