// TODO 5:  Instancirati jedan hotel i dve osobe.
//			Rezervisati sobu za svaku osobu.
//			Osloboditi obe sobe.
//
//			Logovati sve akcije.
var hotel = new modeli.Hotel(new modeli.HotelAdresa('Srbija', 'Novi Sad', 'Puskinova', 16), 'Hotel Prvi', [1, 2, 3]);
var petar = new modeli.Osoba('Petar', 'Petrovic', new modeli.OsobaAdresa('Bulevar Oslobodjenja', 10, 5));
var mitar = new modeli.Osoba('Mitar', 'Miric', new modeli.OsobaAdresa('Bulevar Oslobodjenja', 10, 6));

petar.rezervisi(hotel, 4); // Error
console.log('Losa rezervacija, za Petra: ' + hotel);
petar.rezervisi(hotel, 1); // Success
console.log('Dobra rezervacija, za Petra: ' + hotel);

mitar.rezervisi(hotel, 3);
console.log('Dobra rezervacija, za Mitra: ' + hotel);

petar.oslobodi();
console.log('Petar oslobodio sobu: ' + hotel);
mitar.oslobodi();
console.log('Mitar oslobodio sobu: ' + hotel)
