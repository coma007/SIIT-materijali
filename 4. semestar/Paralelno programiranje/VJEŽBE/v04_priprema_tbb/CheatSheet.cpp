#include <iostream>
#include "tbb\parallel_for.h"
#include "tbb\parallel_sort.h"
#include "tbb\parallel_reduce.h"
#include "tbb\tbb.h"
#include <algorithm>
#define N 100
using namespace tbb;

/*
 
    PARALELNI FOR:
    Zahteva parametrizovani konstruktor i operator() const
    
*/

class ParallelForClass
{
private:
    float* const my_a;
public:
    // Ovde ce se izvrsiti iteriranje, parametar range sluzi da definise raspon
    // OBAVEZNO mora biti const -> ne mozemo pamtiti nista unutar ovog objekta, sve se gubi zbog kopija
    void operator() (const blocked_range<size_t>& range) const; 

    // OBAVEZAN konstruktor
    ParallelForClass(float a[]) : my_a(a) {}; 
};

void ParallelForClass::operator()(const blocked_range<size_t>& range) const
{
    float* a = my_a;
    // range ima istu sintaksu kao iteratori stl biblioteke
    for (size_t i = range.begin(); i != range.end(); i++)
    {
        // Izvrsiti sta treba nad elementima podniza
        a[i] = 2 * a[i + 1];
    }
}

void parallelForExample()
{
    float a[N];
    float a_check[N];

    for (int i = 0; i < N; i++)
    {
        a[i] = sin((float)i);
    }

    // kreiranje provere
    for (int i = 0; i < N - 1; i++)
    {
        a_check[i] = 2 * a[i + 1];
    }
    a_check[N - 1] = a[N - 1];


    ParallelForClass objekat(a);
    // prvi parametar je range, drugi instanca klase a treci je ili auto_partitioner() ili gran_size koji oznacava
    // za koliko elemenata se kreira nova nit (grain_size = 5 znaci na svakih 5 elem.)
    parallel_for(blocked_range<size_t>(0, N - 1), objekat, auto_partitioner());


    for (int i = 0; i < N; i++)
    {
        if (a_check[i] != a[i])
        {
            std::cout << "Greska! " << a_check[i] << " != " << a[i] << " " << i << std::endl;
        }
    }
}



/*
 
	PARALELNI REDUKTOR:
    Zahteva split konstruktor, obican konstruktor, join i operator()

*/
class ParallelReductorClass
{
private:
    float* my_a; 
public:
    float sum; 

	// Ne moze biti const posto se mora pamtiti medjurezultat
    void operator()(const blocked_range<size_t>& r);

    // Razdvajajuci konstruktor -> isto kao konstruktor kopije samo ima i split argument
    ParallelReductorClass(ParallelReductorClass& x, split) : my_a(x.my_a), sum(0) {}

    // Funkcija spajanja
    void join(const ParallelReductorClass& y) { sum += y.sum; }

    // Konstruktor
    ParallelReductorClass(float a[]) : my_a(a), sum(0) {}
};

void ParallelReductorClass::operator()(const blocked_range<size_t>& r)
{ 
    float* a = my_a;
    for (size_t i = r.begin(); i != r.end(); ++i)
        sum += a[i];
}

void parallelReductorExample()
{
    float a[N];
    float a_check[N];
    float sum = 0;
    for (int i = 0; i < N; i++)
    {
        a[i] = sin((float)i);
        sum += a[i];
    }


    ParallelReductorClass objekat(a);
    // prvi parametar je range, drugi instanca klase a treci je ili auto_partitioner() ili gran_size koji oznacava
    // za koliko elemenata se kreira nova nit (grain_size = 5 znaci na svakih 5 elem.)
    parallel_reduce(blocked_range<size_t>(0, N), objekat, auto_partitioner());

    if (objekat.sum != sum)
    {
        std::cout << "Greska! " << sum << " != " << objekat.sum << std::endl;
    }
}

/*

    PARALELNO SORTIRANJE

*/

void parallelSortExample()
{
    float a[N];
    float a_check[N];
    for (int i = 0; i < N; i++)
    {
        a[i] = sin((float)i);
        a_check[i] = a[i];
    }

    std::sort(a_check, a_check + N, std::greater<float>());

    // parametri su pocetak niza, kraj niza i funkcija po kojoj se elementi porede (opciono)
    parallel_sort(a, a + N, std::greater<float>());

    for (int i = 0; i < N; i++)
    {
        if (a_check[i] != a[i])
        {
            std::cout << "Greska! " << a_check[i] << " != " << a[i] << " " << i << std::endl;
        }
    }
}


int main()
{
    
    parallelForExample();
    parallelReductorExample();
    parallelSortExample();


}

