# Infrastructure as Code (IaC)

## Uvod
Održavanje aplikacija koje se sastoje iz velikog broja manjih komponenti ume da postane nezgodno.
Ručno podešavanje resursa kroz konzolu cloud provajdera je dosta zamorno i zavisi od UI-a koji je često promenljiv.
Ručni deployment složene aplikacije može postati vremenski zahtevan posao.
Dodatno, ponavljanje deploymenta u novom okruženju, recimo za testiranje, kao i reprodukcija greške postaje blizu nemogućoj kako aplikacija raste.
Iz tog razloga, svaki cloud provajder ima svoj vid servisa za upravljanje infrastrukturom.
AWS-ovo rešenje je AWS CloudFormation, Google-ov je Google Deployment Manager, Azure-ov je Azure Resource Manager.
Umesto klikova kroz nezgodan UI koji se teško reprodukuju, navedena rešenja omogućavaju definisanje resursa upotrebom deklarativnog jezika kroz kod.
Ovaj koncept se naziva Infrastructure as Code. Kroz deklarativan kod zapisan YAML/JSON sintaksom, kreira se infrastruktura.
Na ovaj način, postupak je dosta manje vremenski zahtevan i uvek je isti. Izuzetno je jednostavno ponoviti deployment u novom okruženju.
Dodatno, kako je infrastruktura definisana kroz kod, može se postaviti na repozitorijum i verzionisati. Ovo dodatno doprinosi pronalaženju i otklanjanju greške.

## AWS CloudFormation
CloudFormation je osnovni vid rukovanja infrastrukturom u okviru AWS Cloud-a. Svi jezici koje ćemo pominjati naknadno se prvo prevode u CloudFormation da bi mogli da se izvrše nad AWS Cloud-om. Slično prevođenju TypeScript-a u JavaScript kako bi kod mogao da se izvrši u pretraživaču.

CloudFormation omogućava definisanje svih potrebnih resursa deklarativno kroz YAML ili JSON kod. Na osnovu koda, CloudFormation kreira sve resurse, u odgovarajućem redosledu sa tačno definisanom i prosleđenom konfiguracijom.

Dodatne prednosti koje dolaze uz upotrebu CloudFormation-a podrazumevaju:
- bolje rukovanje novcem:
    - kreiranje development resursa svakog radnog dana u 8 i brisanje u 17 časova
    - procena potrošnje na osnovu CloudFormation templejta
- reusability:
    - kreiranje templejta koji se mogu upotrebiti za više aplikacija
- gotova rešenja:
    - veliki broj postojećih templejta
    - velika aktivna zajednica

### Kako CloudFormation radi?
- Templejt se upload-uje u S3 bucket.
- Servis čita templejt i kreira sve potrebne resurse = **stack**.
- Nakon svake izmene templejta, isti se mora ponovo upload-ovati.
- Nakon upload-a, stack se ažurira dodatnim resursima (ne kreira se od nule). Ova promena naziva se **change set**.

| ![alt Kreiranje inicijalne infrastrukture](/slike/create-stack-diagram.png "Kreiranje inicijalne infrastrukture") |
|:--:|
| **Kreiranje inicijalne infrastrukture** |

| ![alt Izmena postojece infrastrukture](/slike/update-stack-diagram.png "Izmena postojece infrastrukture") |
|:--:|
| **Izmena postojece infrastrukture** |

CloudFormation ima komplikovanu sintaksu za koju je potrebno određeno vreme kako bi se savladala.
Više detalja na linku: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html


## AWS Serverless Application Model
AWS Serverless Application Model (AWS SAM) je framework koji olakšava kreiranje kompleksnih CloudFormation templejta za rad sa serverless aplikacijama.
Dosta nov alat kojem raste popularnost kao delu AWS servisa. Nudi mogućnost lokalnog testiranja i debagovanje Lambda funkcija kao i API Gateway-a uz upotrebu Docker-a. Takođe, nudi značajno pojednostavljenje pisanja IAM polisa.
Podržane su sve konfiguracije koje su dostupne i u okviru CloudFormation-a.

## Serverless Framework
Serverless Framework je JavaScript framework i za instalaciju zahteva prethodno instaliran Node i NPM.  
Dosta zreo framework sa velikim brojem korisnika, dobrom dokumentacijom i pratećim primerima. Podržava više različitih cloud provajdera.  
Nudi slične mogućnosti AWS SAM-u. Dobra diskusija o prednostima i manama jednog i drugog framework-a može se naći na sledećem linku: https://awsbites.com/66-aws-sam-v-serverless-framework/  
Serverless ima dosta jednostavniju sintaksu i sažetiji je. Zbog toga je zgodniji za male i srednje projekte, kao i za početnike.  
Nudi mogućnost lokalnog testiranja Lambda funkcija koja ne zahteva Docker okruženje. Ne nudi mogućnost testiranja uz upotrebu API Gateway-a.
Iz tog razloga, kao i zbog svoje zrelosti i dobre integracije sa LocalStack-om, preporuka je upotreba ovog framework-a za predmetni projekat. Za studente koji rade direktno sa AWS-om, preporuka je Serverless framework ili SAM.  
U slučaju dodatnih konfiguracija koje možda nisu dostupne direktno kroz Serverless framework, uvek je moguće dopuniti generisani CloudFormation templejt.

Preporuka je instalirati Serverless globalno kako bi bio dostupan i van određenog Node projekta.
Instalacija:

    npm install --global serverless


Za upotrebu Serverless framework-a nad AWS nalogom, potrebno je podesiti kredencijale. Kredencijali omogućuju Serverless-u da upravlja resursima u ime korisnika (kreira infrastrukturu, menja je i briše). U okviru AWS naloga generisati Access key za korisnika u IAM (Identity and Management) servisu. Preuzeti kreirani javni i tajni ključ i podesiti ga upotrebom sledeće komande:

    serverless config credentials --provider aws --key [KLJUC] --secret [TAJNI_KLJUC]

Serverless Framework dolazi uz ugrađeni skup primera koji se mogu kreirati direktno kroz CLI alat.
Za odabir i kreiranje primera potrebno je pozvati sledeću komandu:

    serverless

Nakon poziva, pojavljuje se interaktivni meni koji omogućava kreiranje različitih projekata.  
Serverless projekat je direktorijum u kome se nalazi YAML fajl koji definiše infrastrukturu (resurse i funkcije) u okviru aplikacije.  
Svaki primer, pored YAML templejta, sadrži source kod kao i README koji dodatno olakšava snalaženje.  
Svi primeri su dostupni na sledecem linku: https://www.serverless.com/examples. Dodatno, svaki primer se nalazi javno dostupan na GitHub repozitorijumu.

Korisne komande se nalaze u sledećem fajlu [serverless-komande.txt](/serverless-komande.txt).

## AWS CDK
AWS CDK je imperativni način definisanja infrastrukture. Upotreba "pravog" koda za definisanje potrebnih resursa u okviru aplikacije. Neki od podržanih jezika su Python, TypeScript, JavaScript, Java, C# i Go.  
Dosta zgodno za korisnike koji dolaze iz sfere programiranja, kao i za timove koji imaju dosta iskustva sa nekim programskim jezikom.  
Glavna prednost upotrebe programskog jezika za definisanje strukture jeste upotreba svih prednosti IDE-a za odabrani programski jezik (sintaksa, autocomplete, dokumentacija).  
Druga bitna prednost jeste veliko pojednostavljenje kreiranja dosta sličnih resursa, upotreba petlji, if-ova i drugih jezičkih konstrukta, kao što je i apstrakcija.  
Dobar članak o poređenju AWS CDK i Serverless Framework-a možete pročitati na sledećem linku: https://www.alexdebrie.com/posts/serverless-framework-vs-cdk/ 


## AWS Application Composer
AWS Application Composer je AWS alat koji pruža mogućnost grafičkog dizajniranja serverless aplikacija. Predstavlja najjednostavniji pristup kreiranju AWS serverless aplikacija.  

Za potrebe izrade predmetnog projekta, dozvoljena je upotreba Application Composer-a, ali na odbrani će biti potrebno objasniti svaku komponentu kao i mapiranje na CloudFormation, SAM ili Serverless templejt.  
Neophodno je da postoji neki IaC templejt ili kod u okviru GitHub repozitorijuma koji se može upotrebiti za kreiranje stack-a i koji umete objasniti.
