let photosURL = "https://jsonplaceholder.typicode.com/photos";
console.log("radim");
let request = new XMLHttpRequest();

let overlay = document.getElementById('overlay');
let currentImage;

request.onreadystatechange = function (e) {
    if (this.readyState == 4) {
        if (this.status == 200) {

            console.log("vazi");

            let photos = JSON.parse(request.responseText);

            for (let i = 0; i < 100; i++) {

                let photo = photos[i];
                let photoDiv = document.createElement('div');
                photoDiv.classList.add('previewDiv');

                photoDiv.style.backgroundImage = 'url("' + photo.thumbnailUrl + '")';

                photoDiv.setAttribute("data-imageURL", photo.url);
                photoDiv.setAttribute("data-imageDescription", photo.title);

                photoDiv.addEventListener('click', function (e) {

                    e.stopPropagation();
                    currentImage = this;
                    ShowImage();

                    overlay.style.display = "block";

                });

                let content = document.getElementById('content');
                content.appendChild(photoDiv);
            }
        }
        else {
            alert("Doslo je do greske prilikom ucitavanja slika.")
        }
    }
}

request.open("GET", photosURL);
request.send();

document.body.addEventListener('click', function (e) {
    overlay.style.display = "none";
});

overlay.addEventListener('click', function (e) {
    e.stopPropagation();
})

let leftArrow = document.getElementById("leftArrow");
leftArrow.addEventListener('click', function (e) {

    let previous = currentImage.previousElementSibling;
    if (previous != null) {
        currentImage = previous;
        ShowImage();
    }

});

let rightArrow = document.getElementById("rightArrow");
rightArrow.addEventListener('click', function (e) {

    let next = currentImage.nextElementSibling;
    if (next != null) {
        currentImage = next;
        ShowImage();
    }

});

function ShowImage() {
    let imagePlaceholder = document.getElementById('imagePlaceholder');
        imagePlaceholder.setAttribute("src", currentImage.dataset.imageurl);
        let titlePlaceholder = document.getElementById('titlePlaceholder');
        titlePlaceholder.innerText = currentImage.getAttribute('data-imageDescription');
};

// function listImages(direction="right") {

//     e.stopPropagation();
//     let next = currentImage.nextElementSibling;

//     if (direction == "left") {
//         let previous = currentImage.previousElementSibling;
//     }
// };