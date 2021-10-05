# Milica Sladakovic SV 18/2020

.section .text
.global SaberiMnozi
# int SaberiMnozi(int n, unsigned short *a, unsigned short *b, unsigned short *resenje);

SaberiMnozi:

	pushl %ebp
	movl %esp, %ebp    # cuvanje vrijednosti pokazivaca vrha frejma
	subl $4, %esp      # lokalne promjenljive

	movl $0, -4(%ebp)  # brojac prekoracenja

	pushl %ebx
	pushl %edi
	pushl %esi

	xorl %esi, %esi     # pokazivac na clan niza

sta_da_radi:

	# posto se naknadno (u mnozenju) koriste registri %eax i %ebx
	# svaki put, za svaki slucaj, ponovo u njih prebacujem efektivne adrese

	movl 12(%ebp), %eax # adresa a
	movl 16(%ebp), %ebx # adresa b
	movl 20(%ebp), %ecx # adresa resenje

	xorl %edx, %edx     # anuliranje %edx koji ce se kasnije koristiti za sabiranje/mnozenje

	cmpl %esi, 8(%ebp)
	je kraj	            # kada pokazivac %esi dodje do kraja niza, idi na kraj

	testl $1, %esi      # testiraj parnost maskom $1
	jz parni            # kod neparnih brojeva, u 0b zapisu, najnizi bit je uvijek 1

neparni:

	movw (%eax,%esi,2), %dx
	addw (%ebx,%esi,2), %dx    # u %dx se cuva zbir
    jc kecevi                  # ukoliko dodje do prekoracenja 16bit, flag carry = 1

	movl %edx, (%ecx,%esi,2)   # zbir na odgovarajucu adresu
	incl %esi                  # sljedeci clan niza
	jmp sta_da_radi

parni:

	movw (%eax, %esi,2), %ax   # ovaj mnozi
    movw (%ebx, %esi,2), %bx   # ovim

	mulw %bx                   # mnozenje, rezultat u %dx:%ax
	andw %dx, %dx              # provjerava da li je 0 u %dx
	jnz kecevi                 # ako nije 0, znaci da je doslo do prekoracenja, tj rezultat nije 16bit
	
	movw %ax, %bx              # rezultat u %bx dok se %eax ne sredi
	xorl %eax, %eax            # anulira %eax jer visi dio %eax nije 0
	movw %bx, %ax              # vraca vrijednost rezultata u %ax

	movl %eax, (%ecx, %esi, 2) # proizvod na odgovarajucu adresu
	incl %esi                  # sljedeci clan niza
	jmp sta_da_radi

kecevi:

	xorl %edx, %edx            # anulira %edx

	incl -4(%ebp)              # poveca brojac prekoracenja
	movw $11111, %dx           

	movl %edx, (%ecx,%esi,2)   # vrijednost na odgovarajucu adresu
	incl %esi                  # sljedeci clan niza
	jmp sta_da_radi

kraj:

    movl -4(%ebp), %eax        # povratna vrijednost je brojac prekoracenja

	popl %esi
	popl %edi
	popl %ebx

	movl %ebp, %esp    # brisanje lokalnih promjenljivih
	popl %ebp          # vracanje stare vrijednosti pokazivaca na vrh frejma

	ret
