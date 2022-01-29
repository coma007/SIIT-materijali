# Organizacija podataka
## Softversko inženjerstvo i informacione tehnologije
### Organizacija datoteka u programskom jeziku Pajton
#### Preduslovi za pokretanje
- python 3.7+ [preuzmi](https://www.python.org/downloads/)
- tekst editor po želji

#### Uputstvo za pokretanje
- preuzeti (ili klonirati) repozitorijum
- otvoriti komandnu liniju (terminal, gitbash, powershell ili nešto četvrto) 
- pokrenuti `main.py` skript pomoću komande `python main.py`

#### Opis primera
Rad sa slogovima implementiran je korišćenjem bibloteke [struct](https://docs.python.org/3/library/struct.html) koja nudi rad sa strukturama slično programskom jeziku C.
U primeru se koristi **slog** sa sledećim obeležjima: 
- *id* - ceo broj, 
- *name* - string dužine 10, 
- *q* - realan broj i 
- *status* - ceo broj. 

Nazivi ovih atributa su definisani u `constrants.py`. 
Odmah posle liste atributa definisan je format pakovanja bajtova: i - integer, 10s - string dužine 10, d - double. 
Svaka promena atributa povlači primenu ovog formatnog stringa. 
Spisak karaktera za formatiranje svih primitivnih tipova podataka je [ovde](https://docs.python.org/3/library/struct.html#format-characters).

Umesto ručnog učitavanja, podaci se čitaju iz posebne tekstualne datoteke data/in.txt u upisuju u binarnu datoteku.
Trenutno podržani tipovi organizacija datoteka su:
- serijska, 
- sekvencijalna i 
- rasuta sa serijskom zonom prekoračenja.

Izbor organizacije se vrši tako što se u `main.py` otkomentariše kreiranje željene organizacije datoteke, dok ostale dve ostanu pod komentarom.
U `binary_file.py` definisana je apstraktna klasa `BinaryFile` koja se posle nasleđuje i konkretizuje `serial_file.py`, `sequential_file.py` i `hash_file.py`.
Pakovanje struktura u niz bajtova i obrnuta operacije implementirane su u `record.py`.