#!/bin/bash
#
# Kompajlirati sve cpp datoteke u okviru zadatog direktorijuma. Direktorijum se zadaje kao
# argument komandne linije. Naziv iskompajlirane izvrsne datoteke treba da odgovara nazivu
# izvorne datoteke bez ekstenzije (npr. za izvornu datoteku helloworld.cpp izvrsna datoteka
# treba da se zove helloworld). Za svaku kompajliranu datoteku na standardni izlaz ispisati
# da li je uspesno iskompalirana ili nije. Izlaz g++ kompajlera preusmeriti u datoteku 
# compile.log. Pre pokusaja kompajliranja proveriti da li je zadat postojeci direktorijum
# kao i da li korisnik koji pokrece skript ima potrebna prava (citanje i pisanje).
#
# Argumenti:
#   $1 - putanja do direktorijuma u kojem se nalaze datoteke za kompajliranje
# 
# Primer poziva:
#   ./06_g++.sh 06_izvorni_kodovi/


# TODO implementirati

dir=$1
if [[ -z $dir ]]; then echo "Nema radnog direktorijuma" 
elif [[ ! -d $dir ]]; then echo "$dir nije direktorijum" ;
elif [[ ! -r $dir ]] || [[ ! -w $dir ]]; then echo "Nemate prava pristupa"; 
else
	cd $dir
	for file in $(ls -a *.cpp)
	do
		g++ $file -o $(basename $file .cpp) -pthread 1>&2 2>compile.log
		success=$?
		if [[ $success -eq 0 ]]; then echo "Kompajlirano: $file"
		else echo "Greska: $file nije kompajlirana"
		fi 
	done
fi
