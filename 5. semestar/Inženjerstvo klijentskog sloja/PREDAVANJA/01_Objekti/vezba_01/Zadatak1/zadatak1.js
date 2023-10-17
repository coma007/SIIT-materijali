
// TODO: implementirati funkciju koja proverava duboku jednakost objekata.
function isEqual(obj1, obj2) {

}

var petar = {
  ime: 'Petar',
  prezima: 'Peric',
  startost: 25,
  jezici: ['Srpski', 'Engleski', 'Nemacki'],
  mestoStanovanja: {
    ulica: 'Petrova',
    broj: '1'
  }
};

var petarCopy = {
  ime: 'Petar',
  prezima: 'Peric',
  startost: 25,
  jezici: ['Srpski', 'Engleski', 'Nemacki'],
  mestoStanovanja: {
    ulica: 'Petrova',
    broj: '1'
  }
};

var djura = {
  ime: 'Djura',
  prezime: 'Djuric',
  startost: '5',
  jezici: [],
  mestoStanovanja: {
    ulica: 'Petrova',
    broj: '1'
  },
  otac: petar
};

petar.sin = djura;
petarCopy.sin = djura;

// Za proveru:
console.log('Should be true:', isEqual(petar, petar));
console.log('Should be true:', isEqual(petar, petarCopy));
console.log('Should be false:', isEqual(petar, djura));
