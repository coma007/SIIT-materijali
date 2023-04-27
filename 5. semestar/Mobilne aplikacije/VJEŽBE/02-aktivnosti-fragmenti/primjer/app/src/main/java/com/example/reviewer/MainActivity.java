package com.example.reviewer;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.example.reviewer.activities.SecondActivity;

/*
 * Aktivnost pravimo tako sto napravimo klasu koja nasledjuje AppCompatActivity klasu.
 * Nasledjivanjem ove klase, dobijamo metode zivotnog ciklusa Aktivnosti.
 * */
public class MainActivity extends AppCompatActivity {
    /*
     * Unutar onCreate metode, postavljamo izgled nase aktivnosti koristeci setContentView
     * U ovoj metodi mozemo dobaviti sve view-e (widget-e, komponente interface-a).
     * Moramo voditi racuna, ovde se ne sme nalaziti kod koji ce blokirati prelazak aktivnosti
     * u naredne metode! To znaci da izvrsavanje dugackih operacija treba izbegavati ovde.
     * */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.i("MainActivity", "MainActivity.onCreate()");
        /*
         * Toast klasa se koristi za prikazivanje obavestenja za odredjeni vremenski interval. Posle nekog vremena nestaje.
         * Ne blokira interakciju korisnika
         * */
        Toast.makeText(this, "onCreate()",Toast.LENGTH_SHORT).show();

        /*
         * Koristeci metodu findViewById, mozemo dobaviti tacnu komponentu interface-a preko
         * njenog jedinstvenog id-a (vise o tome kasnije). Na komponente mozemo dodavati razne
         * akcije listenere na slican nacin kako se to radi u drugi programskim jezicima.
         * */
        Button button = findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                /*
                 * Intent je glavna klasa unutar Android-a za pokretanje ili prelazak na druge delove
                 * vase aplikacije. Da bi pokrenuli drugu aktivnost imamo dve opcije
                 * Prva opcija je eksplicitan intent, gde moramo da kazemo sa koje aktivnosti prelazimo na koju aktivnost:
                 *
                 * NPR:
                 * sa MainActivity.this prelazimo na SecondActivity.class
                 *
                 * NAPOMENA: NE KORISTITI KONSTRUKTOR PRILIKOM KREIRANJA AKTIVNOSTI!!
                 */
                Intent intent = new Intent(MainActivity.this, SecondActivity.class);

                /*
                 * Pozivom startActivity metode, saljemo poruku Android-u da on za nas pokrene drugu aktivnost,
                 * nakon cega korisnik biva prebacen na novu aktivnost.
                 **/
                startActivity(intent);
            }
        });

        Button open_google = findViewById(R.id.button2);
        open_google.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                /*
                 * Drugi nacin da se pokrene neka aktivnost jeste implicitan intent.
                 * Razlika od prethodnog jeste u tome sto ovde ne kazemo na koju aktvnost zelimo da predjeno
                 * nego specificiramo parametre, pa ce nam Android ponuditi sve moguce opcije od kojih mi izaberemo
                 * onu koja nam je najbolja (u slucaju da imamo vise apliacija koje mogu da obve isti posao), ili
                 * ce pokrenuti podrazumevanu (ako je takva postavljena ili ako nema drugih aplikacija koje
                 * zadovojlvaju taj kriterijum).
                 *
                 * NPR:
                 * Ako korisnik ima instalirano vise browser-a na uredjaju, a hocemo da otvorimo http://www.google.com,
                 * Android ce nam ponuditi sve pretrazivace koji mogu da zavrse tu akciju. Ako imamo samo jedan instaliran
                 * onda ce pokrenuti taj jedan jedini.
                 * */
                Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.google.com"));
                startActivity(i);

            }
        });
    }

    /*
     * onStart se poziva kada se aktivnost pokrece, nakon nje poziva se onResume
     * i aktivnost je vidljiva..
     * */
    @Override
    protected void onStart() {
        super.onStart();
        Toast.makeText(this, "onStart()", Toast.LENGTH_SHORT).show();
    }
    /*
     * onResume se poziva kada je aktivnost u fokusu i korisnik je u interakciji sa
     * aktivnosti.
     * */
    @Override
    protected void onResume() {
        super.onResume();
        Toast.makeText(this, "onResume()",Toast.LENGTH_SHORT).show();
    }

    /*
     * onPause se poziva kada je aktivnost delimicno prekrivena.
     * */
    @Override
    protected void onPause() {
        super.onPause();
        Toast.makeText(this, "onPause()",Toast.LENGTH_SHORT).show();
    }

    /*
     * onPause se poziva kada je aktivnost u potpunosti prekrivena.
     * */
    @Override
    protected void onStop() {
        super.onStop();
        Toast.makeText(this, "onStop()",Toast.LENGTH_SHORT).show();
    }

}