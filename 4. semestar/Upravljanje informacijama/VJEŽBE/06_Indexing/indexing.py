import pickle
import os
import time
import nltk

#TODO 1 kreirati one term index (kljuc je rec, a vrednost je lista dokumenata koji sadrze tu rec)
#TODO 2 iskoristiti stemmer (pogledajte porter stemmer iz paketa nltk)
#TODO 3 izbaciti 'stopword' termina iz indexa. imate u data folderu listu svih stop izraza
#TODO 4 Ubaciti i 'score' pored naziva dokumenta (za pocetak moze biti samo broj koliko puta se dati termin pojavljuje u dokumentu)
#TODO bonus 1, Napraviti neki malo 'pametniji' score (TF ili TF/IDF)
#TODO dodatni napredni bonus max ++ napraviti index sa izrazima od 2 reci, pored ovog one_term_indexa
def index_file(file, one_term_index):

    text = file.read()
    #file_path=file.name

def create_indexes(path_to_docs):
    dir = os.fsencode(path_to_docs)
    one_term_index = {}

    start_time = time.time()
    for file in os.listdir(dir):
        file = open(os.path.join(dir,file),"r")
        index_file(file, one_term_index)
    
    total_time = time.time()-start_time
    print("Index created in " + str(total_time) + " seconds")

    serialization_file = open("./serialized/one_term_index","wb")
    pickle.dump(one_term_index,serialization_file)

if __name__ == "__main__":
    create_indexes("./data/20_dokumenata")