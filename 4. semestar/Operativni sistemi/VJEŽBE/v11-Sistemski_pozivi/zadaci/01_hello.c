/*
 * Napisati program koji ispise poruku na standardni izlaz upotrebom
 * samo sistemskih poziva.
 *
 * Napomena 1: Deskriptor datoteke za standardni izlaz je uvek 1, a
 * nalazi se i u konstanti STDOUT_FILENO.
 *
 * Napomena 2: U C-u se duzina konstantnog string-a koji je deklarisan
 * sa inicijalizacijom moze dobiti i bez funkcije strlen()-a pomocu
 * sizeof() operatora, na primer:
 *
 * char poruka[] = "Hello, world!\n";
 *
 * Duzina string-a "poruka" (bez NUL karaktera na kraju) se moze
 * dobiti sa sizeof(poruka) - 1.
 */

#include <unistd.h>

int main(void)
{
    static const char poruka[] = "Hello, world!\n";
    write(STDOUT_FILENO, poruka, sizeof(poruka) - 1);
    return 0;
}
