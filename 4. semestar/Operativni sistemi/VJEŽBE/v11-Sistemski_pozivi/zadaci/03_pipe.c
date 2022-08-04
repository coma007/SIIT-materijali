/*
 * Napisati program koji kreira jednosmerni FIFO kanal za komunikaciju
 * (pipe) i zatim klonira svoj proces.
 *
 * Originalni proces treba da ucita string sa standardnog ulaza
 * (najvise 100 karaktera) i zatim da ga posalje kopiji procesa preko
 * pipe-a.
 *
 * Kopija procesa treba da ucita najvise 100 karatera iz pipe-a i da
 * ih ispise na standardni izlaz.
 *
 * Osim toga, originalni proces mora da saceka da se kopija zavrsi pre
 * nego sto zavrsi sa svojim radom.
 */

#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAX_LENGTH 100

int main(void)
{
    int pipefd[2];
    if (pipe(pipefd) < 0) return errno;
    
    int pid = fork();
    
    if (pid > 0)
    {
	/* Necemo koristiti "read" kraj u ovom procesu */
	close(pipefd[0]); 
	
	char buf[MAX_LENGTH];
	int length = read(STDIN_FILENO, buf, MAX_LENGTH);

	if (length >= 0) write(pipefd[1], buf, length);
	close(pipefd[1]);

	/* Cekamo da se zavrsi drugi proces */
	wait(NULL);
    }
    else if (pid == 0)
    {
	/* Necemo koristiti "write" kraj u ovom procesu */
	close(pipefd[1]); 
	
	char buf[MAX_LENGTH];
	int length = read(pipefd[0], buf, MAX_LENGTH);
	if (length >= 0) write(STDOUT_FILENO, buf, length);
	close(pipefd[0]);
    }

    return 0;
}
