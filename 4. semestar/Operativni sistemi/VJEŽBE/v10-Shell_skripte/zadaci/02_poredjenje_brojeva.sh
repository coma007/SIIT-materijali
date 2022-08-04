#!/bin/bash
#
# Napisati bash skript koji za dva zadata cela broja a i b poredi 
# njihove vrednosti i ispisuje na standardni izlaz u kakvoj su relaciji.
# a i b zadati kao prizvoljne promenljive skripta sa predefinisanim
# vrednostima (npr. a=100 i b=10).
#
# Primer koriscenja:
#   ./02_poredjenje_brojeva.sh


# TODO implementirati

echo "Unesite prvi broj" && read a
echo "Unesite drugi broj" && read b

if [ $a -gt $b ]
	then echo "$a je vece od $b"
elif [ $b -gt $a ]
	then echo "$a je manje od $b"
elif [ $a -eq $b ]
	then echo "$a i $b su jednaki"
else 
	echo "Doslo je do greske"
fi
