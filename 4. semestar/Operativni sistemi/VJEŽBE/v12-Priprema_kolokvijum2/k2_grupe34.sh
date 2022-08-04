#!/bin/bash
#
# Napisati bash skriptu koja omogucava rad sa tekstualnim datotekama
# koji sadrze reci.  Skripta treba da podrzava tri opcije za rad:
# generate, sort i combine.
#
# Opcija se nalazi u promenljivi okruzenja K2_OPT.  Ukoliko ova
# promenljiva okruzenja nije data, morate traziti od korisnika da
# unese opciju preko terminala pomocu `read' komande.  Komanda `read'
# jednostavno ucitava jedan red ulaza u promenljivu ciji je naziv dat
# kao parametar.
#
# Opcija `generate' treba da generise 100 tekstualnih datoteka sa 100
# nasumicnih reci u njima, svaka rec u zasebnoj liniji.  Generisanje
# jedne datoteke se radi pomocu `shuf' komande (videti napomenu 1) i
# datom datotekom `words' koja sadrzi sve reci engleskog jezika.
#
# Sve datoteke treba staviti u direktorijum cija je putanja data u
# promenljivoj okruzenja K2_DIR.  Ukoliko ova promenljiva nije data,
# potrebno je traziti od korisnika da je unese isto kao i kod K2_OPT.
#
# Imena datoteka treba da budu words1.lst, words2.lst, i tako dalje,
# sve do words100.lst.  Skripta mora da proveri da li ima prava da
# kreira datoteke u datom direktorijumu, i da obavesti korisnika
# ukoliko to nije slucaj.
#
# Opcija `sort' treba da sortira redove svih datoteka ciji je nastavak
# `.lst' u direktorijumu $K2_DIR.  Za sortiranje se koristi komanda
# sort (videti napomenu 2).  Obratite paznju da se rezultat sortiranja
# smesta u istu datoteku koja je ulaz.
#
# Opcija `combine' treba da konkatenira (spoji) sve datoteke ciji je
# nastavak `.lst' u direktorijumu $K2_DIR, i zatim da rezultujucu
# datoteku sortira i otkloni iz nje sve duplikate.  Otklanjanje
# duplikata se moze uraditi pomocu komande `uniq' (videti napomenu 3).
# Rezultujucu datoteku treba staviti u trenutni direktorijum i nazvati
# `combined.lst'.
#
# Napomena 1: shuf -n broj_redova naziv_datoteke
# Napomena 2: sort -o izlazna_datoteka ulazna_datoteka.
# Napomena 3: uniq ulazna_datoteka izlazna_datoteka
#

if [[ -z "$K2_OPT" ]]
then
        read -p "K2_OPT=" K2_OPT
fi
if [[ -z "$K2_DIR" ]]
then
        read -p "K2_DIR=" K2_DIR
fi
if ! [[ -d "$K2_DIR" ]]
then
        echo "$K2_DIR nije direktorijum"
        exit 1
fi
case "$K2_OPT" in
generate)
        cd $K2_DIR
        for ((i=1; i<=100; i++))
                do
                shuf -n 100 /usr/share/dict/words > "words$i.lst"
                done
;;
sort)
        cd $K2_DIR
        for dat in *.lst
                do 
		sort -o "$dat" "$dat"
                done
;;
combine) cd $K2_DIR
        for dat in  *.lst
                do
                cat $dat >> "aggr.lst"
                done
        sort -o "aggr.lst" "aggr.lst"
        uniq "aggr.lst" "combined.lst":
;;
*) echo "Pogresan izbor"; exit 1
esac


