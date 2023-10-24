## Kreiranje Serverless "projekta" na osnovu postojećih templejta
    serverless create --template ime_templejta
- Serverless projekat je YAML fajl sa definicijom servisa i potrebne infrastrukture
- Svi postojeći templejti se izlistavaju upotrebom --help parametra

### Opcioni parametri:
    -- name -> ime projekta koji će biti kreiran

## Deployment aplikacije
    serverless deploy
Kreiranje resursa definisanih u okviru YAML fajla, kao i pratećee infrastrukture
- minimalno se kreira S3 bucket u koji ce se okačiti kod funkcija i CloudFormation templejt

### Opcioni parametri:
    --stage -> ime okruženja za deployment (dev - predefinisano, test, prod)
    --region -> region u kom ce aplikacija biti deployed (us-east-1 - predefinisano, eu-central-1)

## Poziv funkcije
    serverless invoke --function ime_funkcije

### Obavezan parametar:
    --function -> ime funkcije koja se poziva
### Opcioni parametri:
    local -> lokalno pozivanje funkcije (serverless framework emulira izvršavanje funkcije)
    --data -> prosleđivanje podataka pri pozivu funkcije (event)
    --path -> prosleđivanje podataka koji su zapisani u fajlu pri pozivu funkcije (event)
    --log -> ispisivanje logova u konzoli (flag nije neophodan u slučaju lokalnog pozivanja)

## Brisanje infrastrukture
    serverless remove

### Opcioni parametri:
    --stage -> ime okruženja u kom se nalazi aplikacija (dev, test, prod)
    --region -> region iz kog će aplikacija biti obrisana

## Priprema za deployment:
    serverless package
Opcioni korak, kreira CloudFormation fajl lokalno, kao i pratece zip-ove koda funkcija

### Opcioni parametri:
    --stage -> ime okruženja za deployment (dev, test, prod)
    --region -> region u kom će aplikacija biti deployed
