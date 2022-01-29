let  loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function(e) {
    e.preventDefault(); /* event listener na submit ->
    po defaultu forma se salje na action adresu
    mi sad ne zelimo to vec zelimo da preuzmemo podatke i 
    provjerimo ih a zatim da ih dobavimo sa servera i 
    provjerimo poklapanje */

    let username = document.getElementById('txtUsername').value.trim();
    let password = document.getElementById('txtPassword').value.trim();

    if (username == "" || password == "") {
        alert("Morate unijeti sve podatke za prijavu.");
    } 
    else { /* AJAX - asinhronost java xml */
        let request = new XMLHttpRequest();
        /* PRVO DEF STA SE DESAVA KAD ZAHTJEV STIGNE PA ONDA SALJEMO ZAHTJEV */
        /* def event listener u promjeni stanja */

        let loggedUser = '';

        request.onreadystatechange = function (){
            if(this.readyState==4 /* stigao odgovor */) {
                if(this.status==200 /* http status OK */) {

                    console.log(request);
                    let users = JSON.parse(request.responseText);
                    console.log(users);

                    for(let i=0; i<users.length; i++) {
                        let user = users[i];

                        if (user.email == username && user.username == password) {
                            loggedUser = user;
                            break;
                        }
                    }

                    
                    if (loggedUser=='') {
                        alert("Nisu ispravni login podaci"); 
                    }
                    else {
                        alert("Uspjesno ste ulogovani");
                        window.location.replace("index.html?user=" + loggedUser.name);
                    }
                }
            }
        }
        let url = loginForm.getAttribute("action");
        console.log(url);
        request.open("GET", url); /* tip zahtjeva GET PUT POST DELETE, putanja */
        request.send();
    }

    console.log(username);
});