# REST servisi za blogEntries i comments + AngularJS klijent (REST pozivi)

Aplikacija je jednostavan REST back end i AngularJS klijent blog

## API

* `GET api/blogEntries/` - preuzimanje svih zapisi sa bloga
* `GET api/blogEntries/:id` - prezumanje blog zapis za zadati id
* `POST api/blogEntries/` - postavljanje novog blog zapisa
* `PUT api/blogEntries/:id` - izmena blog zapisa za zadati id
* `DELETE api/blogEntries/:id` - brisanje zapisa za zadati id
* `POST api/comments/blogEntries/:id` - dodavanje komentara za id blog zapisa
* `DELETE api/comments/:id` - brisanje komentara za zadati id

## Struktura aplikacije

U folderu `app/model` nalaze se modeli - blogEntry i comment.

U root folderu se nalazi `app.js`.

U folderu `client` nalazi se Angular klijent

## Pokretanje aplikacije

1. pokrenuti `npm install` (pre prvog pokretanja aplikacije)
2. pokrenuti MongoDB: `mongod --dbpath <putanja do db foldera>`
3. pokretati primere pomoću `node app.js`
