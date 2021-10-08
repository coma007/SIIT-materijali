let firebaseUrl = 'https://wd-audio-i-video-94076-default-rtdb.firebaseio.com/songs.json';

let audioPlaylist = document.getElementById('audioPlaylist');
let player = document.getElementById('player');

let request = new XMLHttpRequest();

request.onreadystatechange = function () {
    if (this.readyState == 4) { /* stigao odgovor */
        if (this.status == 200) { /* ako nije 200, desila se greska prilikom slanja zahtjeva */
            let songs = JSON.parse(request.responseText);

            for (let i = 0; i < songs.length; i++) {
                let song = songs[i];
                 console.log(song);

                let songLi = document.createElement('li');

                let numberSpan = document.createElement('span');
                numberSpan.classList.add('orderNumber');
                numberSpan.innerText = i + 1;
                songLi.appendChild(numberSpan);

                let artistSpan = document.createElement('span');
                artistSpan.classList.add('artistSpan');
                artistSpan.innerText = song.artist;
                songLi.appendChild(artistSpan);

                let songSpan = document.createElement('span');
                songSpan.classList.add('songSpan');
                songSpan.innerText = song.title;
                songLi.appendChild(songSpan);

                /* data podaci - meta podaci, tj. proslijedjujemo podatke koje inace ne bismo molgi */
                songLi.setAttribute('data-url', song.link);

                songLi.addEventListener('click', function(e) {
                    let artist = this.querySelector('.artistSpan').innerText;
                    let playerArtist = document.getElementById('artistElement');
                    playerArtist.innerText = artist;

                    document.getElementById('titleElement').innerText = this.querySelector('.songSpan').innerText;

                    let url = this.getAttribute('data-url');
                    player.setAttribute('src', url);
                    player.play();
                });

                
                audioPlaylist.appendChild(songLi);
            }

        } else {
            alert('Error happend during request for songs');
        }

    }
}

request.open('GET', firebaseUrl);
request.send();
