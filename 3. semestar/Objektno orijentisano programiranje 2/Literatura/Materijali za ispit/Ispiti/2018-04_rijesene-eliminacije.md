# OOP2 - SIIT - ISPIT 14.04.2018.

## ELIMINACIONI DEO

<br>

1. Neka je dat tip A koji definiše virtuelnu metodu `foo` i tip `B` koji nasleđuje tip `A` i definiše istu tu metodu `foo`. Ako imamo sledeći kod `x->foo();` kako treba da bude definisana promenljiva `x` da bi taj kod bio ispravan i da bi se pozvala metoda `foo` iz `B` ?

   ```c++
   a) B* x = new B();
   b) A y;
      B* x = &y;
   c) B y;
      B& x = y;
   d) A* x = new B();
   ```

   ```c++
   Resenje:

   #include <iostream>
   using namespace std;

   class A {
   	public:
   	virtual void foo() { cout << "A virtual void foo()" << endl; }
   };

   class B : public A {
   	public: void foo() { cout << "B void foo()" << endl; }
   };

   int main() {

   	B* x = new B(); // PRVO -> radi
   	x->foo();


   	A  y;           // DRUGO -> ne radi jer ne mozemo da dodelimo pokazivacu na tip izvedene klase adresu objekta roditeljske klase
   	B* x = &y;
   	x->foo();


   	B  y;
   	B& x = y;
   	x->foo();       // TRECE -> radilo bi sa x.foo();


   	A* x = new B(); // CETVRTO -> radi
   	x->foo();


   	return 0;
   }
   ```

2. Ako su date sledeće promenljive i deklaracija funkcije, koji su ispravni pozivi te funkcije?

   ```c++
   std::string x;
   double y;
   void foo(std::string a, const double& b);

   a) foo(x, const&y);
   b) foo(std::string a = x, const double& b = y);
   c) foo(x, y);
   d) foo(x, *y);
   e) foo(x, &y);
   ```

   ```c++
   Resenje:

   #include <iostream>
   std::string x = "Miodrag DJUKA";
   double y = 3.14;

   void foo(std::string a, const double& b)
   {
   	std::cout << a << " " << b << std::endl;
   }

   // Zakomentarisani pozivi nisu ispravni
   int main() {
   	//foo(x, const&y);
   	//foo(std::string a = x, const double& b = y);
   	foo(x, y);
   	//foo(x, *y);
   	//foo(x, &y);
   	return 0;
   }
   ```

3. Napisi telo funkcije ispis, tako da ispisuje na standardan izlaz vrednosti elemenata liste x.

   ```c++
   #include <iostream>
   #include <list>
   void ispis(const std::list<int>& x) { }
   ```

   ```c++
   Resenje:

   #include <iostream>
   #include <list>

   void ispis(const std::list<int>& x)
   {
   	std::list<int>::const_iterator it;
   	for (it = x.begin(); it != x.end(); ++it)
   		std::cout << *it << " ";
   }

   int main()
   {
   	std::list<int> lista(7, 3); // lista sa 7 elemenata vrednosti 3
   	ispis(lista);
   	return 0;
   }
   ```

4. Koje su tvrdnje tacne, a koje ne?

   a) C++ je u potpunosti staticki tipski bezbedan jezik.  
   b) C++ je u potpunosti dinamicki tipski bezbedan jezik.  
   c) C++ podrzava iskljucivo paradigmu objektno orijentisanog programiranja.  
   d) Tip `std::string` je ugradjeni tip u C++ - u.

   **NIJEDNA OD NAVEDENIH TVRDNJI NIJE TACNA**

5. Neka je `A` slozeni tip i `y` promenljiva tog tipa. Ako imamo ovakav ispravan kod `A x(y);` Kako se zove funkcija koja ce na tom mestu biti pozvana?

   a) Podrazumevani konstruktor  
   b) Konstruktor kopije  
   c) Muv konstruktor  
   d) Operator dodele

   **TACAN ODGOVOR JE POD b)**

6. Napisi deklaraciju:

   a) Promenljive tipa STL mape koja preslikava elemente tipa `STL string` u elemente `int` tipa.  
   b) Promenljive korisnicki definisanog tipa, koji se zove `MojTip`.  
   c) Slozenog tipa kojeg cine dva javna polja tipa `float` I jedna privatna funkcija koja prima `STL vector int` - ova I vraca vrednost tipa `int`.

   ```c++
   Resenje:

   //a)
   std::map<std::string, int> mapa;

   //b)
   MojTip x;

   //c)
   class SlozeniTip {
   public:
   	float x;
   	float y;
   private:
   	int funkcija(std::vector<int> v);
   };
   ```

## GLAVNI DEO

1.  Kao kljucne koncepte OOP naveli smo enkapsulaciju, polimorfizam i nasledjivanje. Koja jezicka konstrukcija u C++ nam omogucava polimorfizam ? Ukratko objasniti.

2.  Pitanje u vezi sa mehanizmom izuzetaka, 4 odgovora na zaokruzivanje, ne mogu da se setim sta je tacno bilo ponudjeno.

3.  Za dati isecak koda i svaki zadati prototip funkcije, napisati njen ispravan poziv.

    ```c++
    int i;
    const int& j = i;
    std::vector<int> q;
    // Zatim je bilo ponudjeno 5-6 prototipova funkcija razlicitih kombinacija
    ```

4.  Dopuniti dati kod na zadatom mestu tako da daje izlaz 2,5. Nije dozvoljeno dodavanje ili menjanje datog koda.

    ```c++
    namespace prvo {

    	foo() { cout << "1" << endl; };
    	bar() { cout << "5" << endl; };
    }

    namespace drugo {

    	foo() { cout << "2," << endl; };
    }

    // Ovde dodati kod


    //

    int main() {

    	foo();
    	bar();
    }
    ```

5.  Za dati STL skup preklopiti operator `<<` tako da se pozivom `std::cout << skup;` ispisu svi njegovi elementi.

6.  Navesti bar 3 modifikatora (ili manipulatora) tokovima u C++.

7.  Za dati kod napisati ocekivani izlaz

    ```c++
    	struct Q
    	{
    		virtual void foo(int i) { cout << "0"; };
    	};

    	struct A : Q
    	{
    		virtual void foo(int i) { cout << "1"; };
    	};

    	struct B : Q
    	{
    		void foo(int i) { cout << "2"; };
    	};

    	struct c : Q
    	{
    		void foo(short i) { cout << "3"; };
    	};

    	struct D : Q
    	{
    		void foo(int i) { cout << "4"; };
    	};


    Nakon ovoga je bila data tabela sa 6 isecaka koda u kojima su se kreirali objekti tipa A,B,C,D (sve moguce kombinacije, pokazivaci, reference, new ...) i pozivala se metoda foo. Potrebno je pogoditi ispis.

    ```

8.  Za datu klasu napisati operator dodele, i destruktor. Kopija koja se kreira mora biti duboka kopija. Obezbediti da ne dolazi do curenja memorije. Ispod napisati primer koriscenja operatora dodele.

    ```c++
    class MyType
    {
    	int size;
    	char* buff;

    public:
    	// ovde dodati kod
    }
    ```

9.  Definisana je je template funkcija saberi. Zaokruziti promenljive nad kojima se moze uspesno pozvati funkcija, i ako je moguce, pored napisati primer poziva.

    ```c++
    template<class T>
    T saberi(T x, T y)
    {
    	return x + x - y + y;
    }

    a)	int a; int b;
    b)	std::string a; std::string b;
    c)	int a; float b;
    d)	float a; double b;
    ```

10. Zapoceta je funkcija foo. Ona treba da prima STL skup celobrojnih vrednosti, a nakon izvrsavanja u prosledjenom parametru treba da se nalaze samo parni elementi. Dovrsiti implementaciju funkcije i napisati primer poziva. Dodatno prokomentarisati kako bi kod morao da se izmeni kada bi se umesto skupa koristio STL vektor.

    ```c++
    void foo(
    ```
