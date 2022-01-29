
// URL projekta - Obratiti paznju da je uklonjen znak / sa kraja!
var firebaseUrl = 'https://carsexample-506cf.firebaseio.com';

var carIds = [];
var cars = {};

// GET all
var getButton = document.getElementById('getButton');
getButton.addEventListener('click', function (e) {
    var request = new XMLHttpRequest();

    request.onreadystatechange = function () {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Brisanje prethodnog sadrzaja tabele
                removeTableRows('allCars');
                // Brisanje stare liste id-jeva
                carIds = [];

                cars = JSON.parse(request.responseText);

                // Izvajanje svakog pojedinacnog automobila iteriranjem kroz atribute objekta
                for (var id in cars) {
                    var car = cars[id];
                    console.log(car);
                    appendCarRow('allCars', car);

                    // Dodavanje u niz id-jeva za GET by id zahtev
                    carIds.push(id);
                }
            } else {
                alert('Error occurred. Cars could not be loaded.')
            }
        }
    }

    request.open('GET', firebaseUrl + '/cars.json');
    request.send();
});

// GET by id
var getByIdButton = document.getElementById('getByIdButton');
getByIdButton.addEventListener('click', function (e) {
    var request = new XMLHttpRequest();

    request.onreadystatechange = function () {
        if (this.readyState == 4) {
            if (this.status == 200) {
                removeTableRows('oneCar');

                var car = JSON.parse(request.responseText);
                appendCarRow('oneCar', car);
            } else {
                alert('Error occurred. Car could not be loaded.')
            }
        }
    }

    request.open('GET', firebaseUrl + '/cars/' + carIds[1] + '.json');
    request.send();
});

// PUT
var putButton = document.getElementById('putButton');
putButton.addEventListener('click', function (e) {
    var carId = carIds[1];
    var car = cars[carId];
    car.year = 2020;

    var request = new XMLHttpRequest();
    request.open('PUT', firebaseUrl + '/cars/' + carId + '.json', true);
    request.send(JSON.stringify(car));
});

// DELETE
var deleteButton = document.getElementById('deleteButton');
deleteButton.addEventListener('click', function (e) {
    var request = new XMLHttpRequest();
    request.open('DELETE', firebaseUrl + '/cars/' + carIds[2] + '.json', true);
    request.send();
});

// *********************************************
//               POMOCNE FUNCKIJE
// *********************************************

// Dodaje red u tabelu
function appendCarRow(position, car) {
    var carRow = document.createElement('tr');

    var makeTd = document.createElement('td');
    makeTd.innerText = car.make;
    carRow.appendChild(makeTd);

    var modelTd = document.createElement('td');
    modelTd.innerText = car.model;
    carRow.appendChild(modelTd);

    var yearTd = document.createElement('td');
    yearTd.innerText = car.year;
    carRow.appendChild(yearTd);

    document.getElementById(position).appendChild(carRow);
}

// Brise sve redove iz tabele
function removeTableRows(tBody) {
    var tBody = document.getElementById(tBody);
    while (tBody.firstChild) {
        tBody.removeChild(tBody.lastChild);
    }
}