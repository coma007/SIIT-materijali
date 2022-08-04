import textwrap

# Dodatni napredni bonus zadatak: Pogledajte sadrza csv fajla SalesJan2009. Treba da se za svaku drzavu nadje najskuplja transakcija za svaku od kreditnih kartica:
# Primer resenja:
# Amerika - [visa-1200,Mastercard-3420,dina-1234,amex-3452]
# Srbija - [visa-1111, mastercard-2341,dina-1167]


# Pomocna funkcija za pretvaranje hash mape (dict) u listu parova. Trebace vam u map_implementatipon funkciji
def dict_to_list_of_tuples(dicty):
    list_of_tuples = []

    # Ako imate python 3 umesto dict.iteritems() treba da stavite dict.items()
    for key, value in dicty.items():
        list_of_tuples.append((key, value))

    return list_of_tuples


# Treba da vrati list key-value parova (u pythonu to moze biti lista tuple-ova)
# Data argument ce biti string 
def map_function_implementation(data):
    items = data.split(" ")
    word_count = {}
    for item in items:
        if item in word_count.keys():
            word_count[item] += 1
        else:
            word_count[item] = 1
    word_count_tuple = dict_to_list_of_tuples(word_count)
    return word_count_tuple
    

def shuffle_implementation(data):
    data.sort(key=lambda x: x[0])
    pass


#  Uzima listu key-value parova, treva ba vrati listu key-value parova
def reduce_function_implementation(items):
    shuffle_implementation(items)
    total_count = {}
    for item in items:
        if item[0] in total_count.keys():
            total_count[item[0]] += item[1]
        else:
            total_count[item[0]] = item[1]
    total_count_tuple = dict_to_list_of_tuples(total_count)
    return total_count_tuple

def check_redudance(first, second):
    first_last = first[:-1][0]
    second_first = second[0][0]
    while first_last == second_first:
        # TODO
        continue
    return first, second

if __name__ == "__main__":
    with open("./data/dq.txt") as f:
        data = f.read()

    # Podela fajla na 4 manje delove koji ce se 'paralelno' obradjivati
    data_chunks = textwrap.wrap(data, len(data)//4)

    returned_data = []
    for chunk in data_chunks:
        ret_word_count = map_function_implementation(chunk)
        #  Spajamo sve sto nam vrati svaka 'instanca' map funkcije u jednu list
        returned_data.extend(map_function_implementation(chunk))
    
    final_result = reduce_function_implementation(returned_data)
    print(len(returned_data))
    print(len(final_result))

    # Sta ako hocemo da pokrenemo 2 instance reduce funkcije.
    # Hint: nece. Sto, i kako prepraviti kod da vrati pravilan rezultat
    # Kod ispod otkomentarisati kad uradite map i reduce funkcije

    # treba se pogledati da li je medja first i second half istog ključa
    first_half = returned_data[:len(returned_data)//2]
    second_half = returned_data[len(returned_data)//2:]
    first_half, second_half = check_redudance(first_half, second_half)

    final_result = reduce_function_implementation(first_half)
    final_result.extend(reduce_function_implementation(second_half))
    print(len(final_result))
#
