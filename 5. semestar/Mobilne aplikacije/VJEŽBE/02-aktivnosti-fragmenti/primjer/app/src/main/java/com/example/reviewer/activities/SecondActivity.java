package com.example.reviewer.activities;

import static android.widget.Toast.LENGTH_SHORT;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.fragment.app.FragmentTransaction;
import androidx.fragment.app.FragmentTransitionImpl;

import com.example.reviewer.R;
import com.example.reviewer.fragments.Fragment1;
import com.example.reviewer.fragments.Fragment2;
import com.example.reviewer.tools.FragmentTransition;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = findViewById(R.id.floatingActionButton);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });

        /*
        * Fragmenti ne mogu da postoje samostalno, njih lepimo na aktivnosti.
        * Pogledati detalje ovih metoda.
        * */
        FragmentTransition.to(Fragment1.newInstance(), this, false, R.id.upView);
        FragmentTransition.to(Fragment2.newInstance("FTN"), this, false, R.id.downView);
    }

    /*
     * Metoda onBackPressed se poziva svaki put kada korisnik
     * klikne BACK u Toolbar-u aplikacije ili isto dugme koje se
     * fizicki nalazi na uredjaju.
     * */
    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Toast.makeText(this, "onBackPressed()", LENGTH_SHORT).show();
    }
}
