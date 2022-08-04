-- Selektovati nazive kupaca koji se nalaze u Novom Sadu sortirane po rastucem redosledu:
select NAZKUP from Kupac where MESTKUP = 'Novi Sad' order by NAZKUP asc;

-- Selektovati brojeve faktura koje su realizovane tokom 2010 godine:
select BRFAK from Faktura where DATUM between '1-jan-2010' and '31-dec-2010';

-- Za svaku evidentiranu fakturu ispisati njen broj i naziv kupca kome je roba fakturisana:
select Faktura.BRFAK, Kupac.NAZKUP from Faktura, Kupac where Faktura.IDKUP = Kupac.IDKUP;

-- Prikazati brojeve faktura koje su kupili neki od kupaca sa oznakama K1 ili K2 sortirane u opadajucem redosledu:
select Faktura.BRFAK, Kupac.IDKUP from Faktura, Kupac where Faktura.IDKUP = Kupac.IDKUP and Faktura.IDKUP in ('K1', 'K2') order by Faktura.BRFAK desc;

-- Izlistati identifikacionu oznaku i nazive arikala cija je cena izmedju 15 i 450.
-- Rezultat sortirati u rastucem redosledu identifikacionih oznaka i opadajucem redosledu naziva:
select Artikal.IDART, Artikal.NAZART from Artikal where Artikal.JCENA between 15 and 450 order by Artikal.IDART asc, Artikal.NAZART desc;

--Za svaki artikal izlistati njegov naziv i ukupnu kolicinu datog artikla na svim fakturama:
select Artikal.NAZART, sum(Stavka.KOL) from Artikal, Stavka where Artikal.IDART = Stavka.IDART group by Artikal.IDART, Artikal.NAZART;

-- Za svakog kupca izlistati njegov naziv i nazive artikala koje je kupovao:
select Kupac.NAZKUP, Artikal.NAZART from Kupac, Artikal, Faktura, Stavka where Kupac.IDKUP = Faktura.IDKUP and Faktura.BRFAK = Stavka.BRFAK and Artikal.IDART = Stavka.IDART;

-- Za svaku stavku fakture pod oznakom 'F4' izlistati redni broj stavke i njenu cenu po komadu.
-- U rezultat ukljuciti samo stavke ciji nazivi(artikala) sadrze slovo 'a':
select Stavka.RBRST, Artikal.JCENA from Stavka, Artikal where Stavka.IDART = Artikal.IDART and Stavka.BRFAK = 'F4' and Artikal.NAZART like '%a%';
select Stavka.RBRST, Artikal.JCENA from Stavka natural join Artikal where Stavka.BRFAK = 'F4' and Artikal.NAZART like '%a%';

-- Ispisati broj fakture i naziv savkog artikla na fakturi. U rezultat ukljuciti samo fakture
-- ciji su kupci imali vise od 20000 ukupne fakturisane robe. Rezultat sortirati po opadajucem
-- redosledu broja fakture:
select Faktura.BRFAK, Artikal.NAZART
from Faktura, Artikal, Stavka, Kupac
where Kupac.IDKUP = Faktura.IDKUP
and Artikal.IDART = Stavka.IDART
and Faktura.BRFAK = Stavka.BRFAK
and Faktura.IDKUP in (select Faktura.IDKUP from Faktura, Stavka where Faktura.BRFAK = Stavka.BRFAK group by Faktura.BRFAK, Faktura.IDKUP having sum(Stavka.CENA) >20000)
order by Faktura.BRFAK asc;

-- Prikazati nazive kupca i ukupan broj faktura koje su im fakturisane. Ukoliko kupac nema
-- fakture ispisati 0:
select Kupac.NAZKUP, count(Faktura.BRFAK) from Kupac left outer join Faktura on Kupac.IDKUP = Faktura.IDKUP group by Kupac.NAZKUP;

-- Kreirati pogled 'TopArtikli' koji sadrzi identifikacione brojeve artikala i nazive za one
-- cija je ukupna prodata kolicina veca od prosecne kolicine na nivou svih stavki faktura:
CREATE OR REPLACE VIEW TopArtikli ("Identifikacioni broj", "Naziv") AS
SELECT Artikal.IDART, Artikal.NAZART
FROM Artikal, Stavka
WHERE Artikal.IDART = Stavka.IDART
GROUP BY Artikal.IDART, Artikal.NAZART
HAVING SUM(Stavka.KOL)>(SELECT AVG(Stavka.KOL) FROM Stavka);
select * from TopArtikli;

-- Kreirati tabelu 'Popust':
-- popust({idpop,nazpop,datumPocetka,datumZavrsetka,idart},{idpop})
-- popust[idart] C artikal[idart]
-- Obelezja idpop, datumPocetka, datumZavrsetka, idart ne smeju imati null vrednosti.
CREATE TABLE Popust(
	IDPOP varchar(2) NOT NULL,
	NAZPOP varchar(20),
	DATUMPOCETKA date NOT NULL,
	DATUMZAVRSETKA date NOT NULL,
	IDART varchar(2) NOT NULL,
	CONSTRAINT popust_PK PRIMARY KEY (IDPOP),
	CONSTRAINT popust_FK FOREIGN KEY (IDART) REFERENCES Artikal (IDART)
);

-- Obrisati sve stavke sa faktura ciji su kupci iz Novog Sada.
select * from Stavka where Stavka.IDART;
DELETE FROM Stavka
WHERE BRFAK in (select Faktura.BRFAK from Faktura where Faktura.IDKUP in (select Kupac.IDKUP from Kupac where Kupac.MESTKUP = 'Novi Sad'));