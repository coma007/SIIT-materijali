let firebaseUrl = 'https://wd-audio-i-video-94076-default-rtdb.firebaseio.com/videos.json';

let videoPlaylist = document.getElementById('videoPlaylist');
let player = document.getElementById('player');

let request = new XMLHttpRequest();

request.onreadystatechange = function(e) {

    if (this.readyState == 4) {
        if (this.status == 200)
        {
            /* bez ovog JSON.parse bi se dobio samo string, a prakticniji je niz */
            let videos = JSON.parse(this.responseText);
            
            for (let i=0; i<videos.length;i++) {

                /* da je ovdje VAR svaki event listener bi pustao zadnji video, lokalna prom */
                let currentVideo = videos[i];

                let videoLi = document.createElement("li");
                
                let numberSpan = document.createElement("span");
                numberSpan.innerText = i+1;
                numberSpan.classList.add("orderNumber");
                videoLi.appendChild(numberSpan);

                let titleSpan = document.createElement("span");
                titleSpan.innerText = currentVideo.title;
                titleSpan.classList.add("songSpan");
                videoLi.appendChild(titleSpan);

                videoLi.setAttribute("data-url", currentVideo.link);
                
                videoLi.addEventListener("click", function(e) {

                    let titleElement = document.getElementById("titleElement");
                    let title = this.querySelector(".songSpan").innerText;
                    titleElement.innerText = title;

                    let link = this.getAttribute("data-url");
                    player.setAttribute("src", link);
                    player.play();
                })

                videoPlaylist.appendChild(videoLi);
            }
        }

        else {
            alert("An error occured")
        }
    }

} 


request.open("GET", firebaseUrl); /* tip zahtjeva */
request.send(); /* slanje zahtjeva */