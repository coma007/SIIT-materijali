/*
	Selekcija HTML elemenata na osnovu njihovog ID-a. Ovo ce nam dati
	referencu na sam HTML element kojim mozemo da manipulisemo u realnom vremenu.
	Ukoliko imamo potrebu da neki HTML element selektujemo vise puta
	u istom JS fajlu, dobra je praksa selektovati ga jednom i rezultat
	spremiti u promenljivu koju kasnije mozemo koristiti umesto da svaki
	put prolazimo kroz ceo proces selekcije elemenata.
*/
var kockica = document.getElementById('glavnaKocka');

// Klik na dugme ciji je id 'hideButton'
var hideButton = document.getElementById('hideButton');
hideButton.addEventListener('click', function(e) {
	// 'style' atribut nam daje pristup CSS pravilima vezanim za element
	// U ovom primeru sakrivamo element tako sto cemo mu podestiti 'display: none'
	kockica.style.display = 'none';
});

var showButton = document.getElementById('showButton');
showButton.addEventListener('click', function(e) {
	// Prikazivanje elemenata se radi vracanjem njihovog CSS atributa 'display' na podrazumevanu vrednost
	kockica.style.display = 'block';
});

var classButton = document.getElementById('classButton');
classButton.addEventListener('click', function(e) {
	// 'classList' atribut nam daje pristup listi CSS klasa vezanih za HTML element
	kockica.classList.toggle('velikaCrvenaKocka');
});

var textButton = document.getElementById('textButton');
textButton.addEventListener('click', function(e) {
	// Pomocu 'innerText' atributa mozemo menjati tekstualni sadrzaj HTML elemenata
	// Pored ovoga, postoji i verzija 'innerHTML' koja nam omogucava da dodamo HTML kod u element
	kockica.innerText = 'Ćao!';
});

var createButton = document.getElementById('createButton');
createButton.addEventListener('click', function(e) {
	// Kreiranje HTML elemenata se vrsi funcijom 'createElement'
	// Ovo ce kreirati novi HTML element u memoriji koji onda kasnije mozemo ubaciti na zeljeno mesto na stranici
	var novaKockica = document.createElement('div');
	// Funkcija 'createElement' ce nam vratiti referencu na novokreirani element sa kojom mozemo manipulisati
	// na isti nacin kao i da smo selektovali postojeci element sa stranice
	novaKockica.id = 'novaKockica';
	novaKockica.classList.add('kockica');
	// Dodavanje elemenata u vec postojece elemente se vrsi funkcijom `appendChild`
	document.body.appendChild(novaKockica);
});

var alertButton = document.getElementById('alertButton');
alertButton.addEventListener('click', function(e) {
	// Funkcija alert() prikazuje pop-up prozor sa prosledjenom porukom
	// NAPOMENA: Prikazivanje alert prozora zaustavlja izvrsavanje trenutnog koda dok se prozor ne zatvori
	alert('Kliknuli ste na dugme!');
});

var consoleButton = document.getElementById('consoleButton');
consoleButton.addEventListener('click', function(e) {
	// Funkcija console.log() ispisuje prosledjenu poruku u konzoli browsera
	// Postoje i varijante error(), warn(), info(), table()
	console.log('Kliknuli ste na dugme');
	console.error('Primer error funcije za ispis');
	console.warn('Primer warn funkcije za ispis.');
	console.table(["RS 1/2018 Petar Petrovic", "RS 2/2018 Jovana Jovanovic"])
});