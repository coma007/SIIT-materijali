# autor: Milica

.section .text
.global kodiraj
# int kodiraj(unsigned int vrednost)

kodiraj:

	pushl %ebp
	movl %esp, %ebp
	subl $12, %esp

	movl $0b1, -4(%ebp)  # maska za n
	movl $0b10, -8(%ebp)  # maska za n+1
	movl $0b10000000000000000000000000000000, -12(%ebp)  # maska za n-1

	pushl %ebx
	pushl %esi
	pushl %edi

	movl 8(%ebp), %eax # vrijednost

pocni:

	testl -4(%ebp), %eax 	# testiraj n
	jz dalje

	testl -8(%ebp), %eax    # testiraj n+1
	jnz dalje

	testl -12(%ebp), %eax   # testiraj n-1 
	jnz dalje

	xorl -4(%ebp), %eax

dalje:

	roll $1, -12(%ebp)
	roll $1, -8(%ebp)
	roll $1, -4(%ebp)
	
	jnc pocni

	xorl %esi, %esi
	xorl %ebx, %ebx        # brojac_donji
	xorl %edx, %edx        # brojac_gornji

prebroj:

	testl -4(%ebp), %eax
	jz novi

	cmpl $16, %esi
	jb dodaj_prvi
	
	cmpl $32, %esi
	jb dodaj_drugi

dodaj_prvi:

	incl %ebx
	jmp novi

dodaj_drugi:

	incl %edx
	
novi:

	incl %esi
	roll $1, -4(%ebp)
	jc uporedi

	jmp prebroj

uporedi:

	cmpl %edx, %ebx
	jb kraj

	roll $16, %eax

kraj:

	popl %esi
	popl %edi
	popl %ebx

	movl %ebp, %esp
	popl %ebp

	ret
