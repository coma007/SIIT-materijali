# Napisati Dockerfile za generisanje typon slike. Slika treba da sadrzi sve pakete
# potrebne za instalaciju i koriscenje typon alata za vezbanje kucanja dostupne na
# GitHub repozitorijumu: https://github.com/ihsuy/Typon
# Listing potrebnih paketa i uputstvo za koriscenje alata su navedeni u README 
# datoteci repozitorijuma. Izgraditi typon sliku i na osnovu nje napraviti 
# Docker kontejner. Kontejner pokrenuti u interaktivnom rezimu i pokrenuti
# typon izvrsnu datoteku.
#
# Izgradnja slike: docker build . -t typon
# Izgradnja i pokretanje kontejnera u interaktivnom rezimu: docker run -it typon


FROM ubuntu
RUN apt-get update && apt-get install -y libncurses5-dev libncursesw5-dev
RUN apt-get install -y g++ git make
WORKDIR /home
RUN git clone https://github.com/ihsuy/Typon.git typon
WORKDIR /home/typon
RUN mv Typon/* .
RUN rmdir Typon
RUN make