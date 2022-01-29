window.onload = () => { /* ovo ne mora kada je skripta na dnu */
    /* skripta na vrhu se prilikom renderovanja zbuni jer joj nisu poznati id-evi */
    /* moze i funkcija eventlistener */

    let hideBtn = document.getElementById("hideButton");
    let kockica = document.getElementById("glavnaKocka");
    let showBtn = document.getElementById("showButton");
    let toggleBtn = document.getElementById("classButton");
    let addBtn = document.getElementById("textButton");
    let alertBtn = document.getElementById("alertButton");
    let consoleBtn = document.getElementById("consoleButton");
    let createBtn = document.getElementById("createButton")

    hideBtn.addEventListener("click", function (e) {
        kockica.style.display = "none";
    })

    showBtn.addEventListener("click", function (e) {
        kockica.style.display = "block";
    })

    toggleBtn.addEventListener("click", function (e) {
        kockica.classList.toggle("velikaCrvenaKocka");
    })

    addBtn.addEventListener("click", function (e) {
        kockica.innerText = "Text";
    })

    alertBtn.addEventListener("click", function (e) {
        alert("Alert text");
    })

    consoleBtn.addEventListener("click", function (e) {
        console.log("Some console text");
        console.warn("Warning");
        console.error("Error text");
        console.table(["user 1 data", "user 2 data"]);
    })

    createBtn.addEventListener("click", function (e) {
        let body = document.getElementsByTagName("body")[0];
        let novakockica = document.createElement("div");
        novakockica.classList.add("kockica");
        document.body.appendChild(novakockica);
        // console.table(["user 1 data", "user 2 data"]);
    })

    console.log(hideBtn);

};