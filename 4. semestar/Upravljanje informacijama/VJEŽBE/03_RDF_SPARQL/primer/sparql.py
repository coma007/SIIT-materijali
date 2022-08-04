import requests
import pprint


def do_query(query):
    result = requests.post('http://localhost:3030/dataset/sparql',  params={'query': query})
    result = result.json()['results']['bindings']
    pprint.pprint(result)


print("Query 0:")
query = """SELECT ?s WHERE
    {?s ?o "London"}"""
do_query(query)

print("\nQuery 1: Dobaviti osobe zajedno sa hobijem, profesijom i lokacijom te osobe")
query = """
PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/>
SELECT ?person ?profession ?hobby ?city
WHERE {
    ?person pred:profession ?profession .
    ?person pred:hobby ?hobby .
    ?person pred:livesIn ?city .
}
ORDER BY ?person
"""
do_query(query)

print("\nQuery 2: Dobaviti sve osobe koje zive u londonu i medjusobno su u odnosu roditelj-dete")
query = """
PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/> 
SELECT ?person ?relative
WHERE {
    ?person pred:livesIn "London" .
    ?person pred:parentTo|pred:childOf ?relative  .
}
"""
# query = """
# PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/>
# SELECT *
# WHERE {
#     ?person pred:livesIn "London" .
#     { ?person pred:parentTo ?relative  . } UNION { ?person pred:childOf ?relative  . }
# }
# """
do_query(query)

print("\nQuery 3: Dobaviti sve osobe sa njihovim hobijem i omiljenim timom (ako osoba nema omiljeni tim i dalje treba hobi da se ispise)")
query = """
PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/> 
SELECT ?person ?hobby ?team
WHERE {
    ?person pred:hobby ?hobby .
    OPTIONAL {
    ?person pred:favouriteTeam ?team .
    }
}
"""
do_query(query)

print("\nQuery 4: Dobaviti osobe zajedno sa hobijem, profesijom i lokacijom te osobe za gradove koji se zavrsavaju na -on")
query = """
PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/>
SELECT ?person ?profession ?hobby ?city
WHERE {
    ?person pred:profession ?profession .
    ?person pred:hobby ?hobby .
    ?person pred:livesIn ?city .
    FILTER regex(?city, "on$") .
}
"""
do_query(query)

print("\nQuery 5: Dobaviti osobe zajedno sa hobijem, profesijom i lokacijom te osobe za one koje su rodjene prije 90ih")
query = """
PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/>
SELECT ?person ?profession ?hobby ?city ?date
WHERE {
    ?person pred:profession ?profession .
    ?person pred:hobby ?hobby .
    ?person pred:livesIn ?city .
    ?person pred:date ?date .
    FILTER (?date < "1990-01-01"^^<http://www.w3.org/2001/XMLSchema#date>) .
}
"""
do_query(query)

print("\nQuery 6: Dobaviti osobe zajedno sa hobijem, profesijom i lokacijom te osobe za one koje su rodjene prije 90ih i sortirati po datumu")
query = """
PREFIX pred: <http://www.ftn.uns.ac.rs/rdf/examples/predicate/>
SELECT ?person ?profession ?hobby ?city ?date
WHERE {
    ?person pred:profession ?profession .
    ?person pred:hobby ?hobby .
    ?person pred:livesIn ?city .
    ?person pred:date ?date .
    FILTER (?date < "1990-01-01"^^<http://www.w3.org/2001/XMLSchema#date>) .
}
ORDER BY ?date
"""
do_query(query)
