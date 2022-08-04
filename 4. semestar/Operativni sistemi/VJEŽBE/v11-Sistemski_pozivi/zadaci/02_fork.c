/*
 * Napisati program koji klonira svoj proces, i zatim:
 *
 * Originalni proces treba da ispisuje slovo A odredjeni broj puta sa
 * pauzom od 2 sekunde izmedju ispisa.
 * Kopija treba da ispisuje slovo B odredjeni broj puta sa pauzom od 2
 * sekunde izmedju ispisa.
 *
 * Ukoliko je PID kopije paran broj, kopija treba da ceka 1 sekund pre
 * nego sto pocne sa ispisima, a u suprotnom, originalni proces treba
 * da ceka 1 sekund pre nego sto pocne sa ispisima.
 */

#include <unistd.h>

#define BROJ_PUTA 5

int main(int argc, char *argv[])
{
    int pid = fork();
    if (pid < 0) return 1;

    /*
     * Ukoliko pid nije nula, onda se radi o prvobitnom procesu, koji
     * treba da ispise A, a u suprotnom radi se o kopiji, koja treba
     * da ispise B.
     */
    char slovo = pid ? 'A' : 'B';

    /*
     * Ukoliko smo u originalnom procesu, cekamo jedan sekund ako je
     * PID klona neparan broj, a ukoliko smo u kopiji, cekamo jedan
     * sekund ako je PID naseg procesa paran broj.
     */
    if ((pid > 0 && (pid % 2) != 0)
	|| (pid == 0 && (getpid() % 2) == 0))
    {
	sleep(1);
    }

    for (int i = 0; i < BROJ_PUTA; i++)
    {
	write(1, &slovo, sizeof(slovo));
	sleep(2);
    }

    return 0;
}
