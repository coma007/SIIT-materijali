import pickle

from yaml import serialize

#TODO index je ucitan, na vama je da uzmete jednu rec od korisnika i vratite listu dokumenata koji sadrze tu rec (po mogucnosti sortirano)
#TODO bonus Omogucili napredne logicke izrace (AND OR, NOT)
if __name__ == "__main__":
    serialization_file = open("./serialized/one_term_index", "rb")
    one_term_dict = pickle.load(serialization_file)
    print(one_term_dict)