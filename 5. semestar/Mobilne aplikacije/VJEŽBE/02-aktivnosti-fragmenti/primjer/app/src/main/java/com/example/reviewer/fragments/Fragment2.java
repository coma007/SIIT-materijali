package com.example.reviewer.fragments;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.reviewer.R;

/*
 * Da bi napravili Fragment, potrebno je da napravite klasu koja nasledjuje
 * klasu Fragment. Za razliku od aktivnosti, fragmente ne moramo da
 * specificiramo unutar Manifest file-a. Za rasliku od aktivnosti,
 * fragmenti ne mogu da postoje nezavniso. Nji vezemo za neku aktivnost.
 * Time postizemo lakse izmenjiv interface i mogucnost da iskoristimo
 * celokupan ekran pogotovo u landscap-e rezimu.
 * */
public class Fragment2 extends Fragment {
    /*
     * Da bi napravili Fragment, treba da izbegavamo direktan poziv konstruktora
     * Za to mozemo iskoristiti staticku metodu koja to moze da uradi za nas.
     * Ako je potrebno da fragmentu prosledimo nekakve parametre, to mozemo da uradimo
     * koristeci dodatne parametre opisane klasom Bundle.
     * */
    public static Fragment2 newInstance(String someParam) {
        Bundle args = new Bundle();
        args.putString("SOME_PARAM_KEY", someParam);

        Fragment2 fragment = new Fragment2();
        fragment.setArguments(args);
        return fragment;
    }
    /*
     * Kao i aktivnost i fragment ima specificnu metodu za postavljanje layout-a fragment-a.
     * Zivotni ciklus fragmenta je vezan za zivnoti ciklus aktivnosti.
     * Parametre koje smo prosledili u metodi newInstance koristeci Bundle, kasnije mozemo
     * da dobijemo nazad koristeci metodu getArguments.
     * */
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.mysecondfragment_layout, container, false);

        Bundle bundle = getArguments();
        if (bundle != null){
            String param = bundle.getString("SOME_PARAM_KEY", "DEFAULT");
            TextView textView = view.findViewById(R.id.textView2);
            textView.setText(param);
        }

        return view;
    }

    @Override
    public void onActivityCreated(Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        Toast.makeText(getActivity(), "onActivityCreated()", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        Toast.makeText(getActivity(), "onAttach()", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        Toast.makeText(getActivity(), "onDestroyView()", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onDetach() {
        super.onDetach();
        Toast.makeText(getActivity(), "onDeatach()", Toast.LENGTH_SHORT).show();
    }
}
