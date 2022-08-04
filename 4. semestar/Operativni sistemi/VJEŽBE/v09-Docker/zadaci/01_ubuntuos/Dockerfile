# Napisati Dockerfile za generisanje ubuntuos slike. Slika treba da bude bazirana na
# Ubuntu operativnom sistemu. Instalirati azuriranja postojecih paketa i sve pakete
# koji su vam potrebni za pisanje, prevodjenje i izvrsavanje C++ programa (minimalno
# g++ paket). Unutar slike napraviti direktorijum /home/os i u njega prebaciti sve
# materijale vezbi na ovom kursu. Izgraditi ubuntuos slike i na osnovu nje napraviti
# Docker kontejner. Kontejner pokrenuti u interaktivnom rezimu pozicionirati se u 
# neki direktorijum vezbi, iskompajlirati neku od cpp datoteka i izvrsiti prevedeni
# program.
#
# Izgradnja slike: docker build . -t ubuntuos
# Izgradnja i pokretanje kontejnera u interaktivnom rezimu: docker run -it ubuntuos


FROM ubuntu
RUN apt-get update && apt-get upgrade g++ -y
WORKDIR /home
RUN mkdir os
WORKDIR ${WORKDIR}/os
ADD . ${WORKDIR}