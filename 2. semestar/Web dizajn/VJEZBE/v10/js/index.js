let firebaseUrl = "https://my-web-design-project-67559-default-rtdb.europe-west1.firebasedatabase.app";

getCars();

function getCars(){
    let request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if(this.status == 200){

                removeTableRows("allCars");

                let cars = JSON.parse(this.responseText);
                // console.log(cars);

                for (let id in cars) {
                    let car = cars[id];
                    appendCarRow('allCars', id, car)
                }

            }
            else {
                alert("An error occured")
            }
        }
    }

    request.open('GET', firebaseUrl.concat('/cars.json'));
    request.send();
}

function removeTableRows(tBodyId){

    let tBody = document.getElementById(tBodyId);

    while(tBody.firstChild){

        tBody.removeChild(tBody.lastChild);

    }

}

function appendCarRow(tbodyId, carId, car) {
    let carTr = document.createElement('tr');

    let makeTd = document.createElement('td');
    makeTd.innerText = car.make;
    carTr.appendChild(makeTd);

    let modelTd = document.createElement('td');
    modelTd.innerText = car.model;
    carTr.appendChild(modelTd);

    let yearTd = document.createElement('td');
    yearTd.innerText = car.year;
    carTr.appendChild(yearTd);

    let editBtn = document.createElement("button");
    editBtn.type = "button";
    editBtn.innerText = "Izmjeni"
    editBtn.onclick = showEditPage;
    editBtn.setAttribute('data-carId', carId);

    let editTd = document.createElement('td');
    editTd.appendChild(editBtn);
    carTr.appendChild(editTd);

    let deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.innerText = "Obrisi"
    deleteBtn.onclick = deleteCar;
    deleteBtn.setAttribute('data-carId', carId);

    let deleteTd = document.createElement('td');
    deleteTd.appendChild(deleteBtn);
    carTr.appendChild(deleteTd);

    let tbody = document.getElementById(tbodyId);
    tbody.appendChild(carTr);

}

function showEditPage() {
    
    let clicked = this;
    // console.log(clicked);

    let carId = clicked.getAttribute('data-carId');
    window.location.href = "edit.html?" + carId;


}

function deleteCar() {

    let clicked = this;
    // console.log(clicked);

    let carId = clicked.getAttribute('data-carId');

    let deleteRequest = new XMLHttpRequest();

    deleteRequest.onreadystatechange = function() {
        if (this.readyState == 4) {
            if(this.status == 200){

                getCars()
                

            }
            else {
                alert("An error occured");
            }
        }
    }

    deleteRequest.open('DELETE', firebaseUrl.concat('/cars/', carId, '.json'));
    deleteRequest.send();

}
