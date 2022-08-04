/*
 * Napisati program koji sifruje datoteku ROT13 algoritmom pomocu
 * sistemskih poziva.
 *
 * ROT13 algoritam pretvara zamenjuje slova A-M sa slovima N-Z, i
 * obrnuto. Drugacije gledano, na redni broj slova (izmedju 0 i 25) se
 * dodaje broj 13, a zatim se uzima ostatak pri deljenju sa 26 kako bi
 * se dobio novi redni broj. Karakteri koji nisu velika ili mala slova
 * ostaju nepromenjeni.
 *
 * Program treba da otvori datoteku ciji je naziv dat u parametru
 * komandne linije, i da mapira celokupan sadrzaj te datoteke u
 * memoriju pomocu sistemskog poziva mmap(). Zatim se ROT13 algoritam
 * primenjuje nad nizom koji predstavlja sadrzaj cele datoteke.
 */

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
    if (argc < 2) return 1;
    
    int fd = open(argv[1], O_RDWR);
    if (fd < 0) return 1;

    /* Koristimo fstat() kako bismo nasli velicinu datoteke */
    struct stat info;
    if (fstat(fd, &info) < 0)
    {
	close(fd);
	return 1;
    }

    /* Mapiramo celu datoteku u memoriju naseg procesa */
    char *sadrzaj = mmap(NULL, info.st_size, PROT_WRITE, MAP_SHARED, fd, 0);
    if (!sadrzaj)
    {
	close(fd);
	return 1;
    }

    for (int i = 0; i < info.st_size; i++)
    {
	if (sadrzaj[i] >= 'a' && sadrzaj[i] <= 'z')
	    sadrzaj[i] = 'a' + (sadrzaj[i] - 'a' + 13) % 26;
	else if (sadrzaj[i] >= 'A' && sadrzaj[i] <= 'Z')
	    sadrzaj[i] = 'A' + (sadrzaj[i] - 'A' + 13) % 26;
    }

    /* Uklanjamo mapiranje i samim tim azuriramo datoteku */
    munmap(sadrzaj, info.st_size);
    close(fd);
    return 0;
}
