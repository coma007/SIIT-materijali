/*
 * Napisati program koji klonira trenutni proces, i zatim:
 *
 * Originalni proces treba svaki sekund da ispise poruku "Prosao je
 * jedan sekund." pomocu sistemskog poziva alarm() i signala SIGALRM.
 *
 * Pomocu signala SIGCHLD, treba detektovati kraj izvrsavanja kopije
 * procesa i ispisati poruku "Kopija procesa je zavrsila sa radom.".
 *
 * Kopija procesa samo treba da ceka 5 sekundi.
 *
 * Kada korisnik pritisne kombinaciju tastera Ctrl+C (signal SIGINT),
 * treba ispisati poruku "Pritisnuli ste Ctrl+C, program zavrsava sa
 * radom.", i zatim prekinuti originalni proces.
 */

#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

void sighandler(int signum)
{
    static const char poruka1[] = "Prosao je jedan sekund.\n";
    static const char poruka2[] = "Kopija procesa je zavrsila sa radom.\n";
    static const char poruka3[] = "Pritisnuli ste Ctrl+C, program zavrsava sa radom.\n";
    
    switch (signum)
    {
    case SIGALRM:
	write(STDOUT_FILENO, poruka1, sizeof(poruka1) - 1);
	alarm(1);
	break;
	
    case SIGCHLD:
	wait(NULL); /* Bez ovoga ostao bi zombi proces */
	write(STDOUT_FILENO, poruka2, sizeof(poruka2) - 1);
	break;

    case SIGINT:
	write(STDOUT_FILENO, poruka3, sizeof(poruka3) - 1);
	exit(0);
	break;
    }
}

int main(void)
{
    int pid = fork();

    if (pid > 0)
    {
	signal(SIGALRM, sighandler);
	signal(SIGCHLD, sighandler);
	signal(SIGINT, sighandler);
	alarm(1);

	/* Koristimo select() bez parametara kao beskonacno cekanje */
	for (;;) select(0, NULL, NULL, NULL, NULL);
    }
    else if (pid == 0)
    {
	sleep(5);
    }

    return 0;
}
