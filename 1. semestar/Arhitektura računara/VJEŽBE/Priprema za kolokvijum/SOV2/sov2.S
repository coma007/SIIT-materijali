# milica

.section .data

ispis1: .ascii "Unesite izraz: \0"
len1 = .- ispis1

izraz: .fill 100,1,42

ispis2: .ascii "Sume su jednake.\n\0"
len2 = .- ispis2

ispis3: .ascii "Suma brojeva u opsegu je manja.\n\0"
len3 = .- ispis3

ispis4: .ascii "Suma brojeva izvan opsega je manja.\n\0"
len4 = .- ispis4

ispis_suma: .ascii "Suma: \0"
len5 = .- ispis_suma

donja: .long 0
gornja: .long 0

suma_u: .long 0
suma_izvan: .long 0

manja: .long 0
string: .fill 33,1,42

greska1: .ascii "GRESKA: Prekoracenje prilikom racunanja sume.\n\0"
len6 = .- greska1

greska2: .ascii "GRESKA: Problem prilikom konverzije brojeva.\n\0"
len7 = .- greska2

greska: .long 0

.section .text
.global main

main:

	movl $4, %eax         # ispis1
	movl $1, %ebx
	leal ispis1, %ecx
	movl $len1, %edx
	int $0x80

	movl $3, %eax         # unesi_izraz
	movl $0, %ebx
	leal izraz, %ecx
	movl $100, %edx
	int $0x80

	incl %ecx # preskoci odmah [
	xorl %esi, %esi # pokazivac	
	movl $10, %edi        # baza
	
	xorl %eax, %eax

brojevi:

	xorl %ebx, %ebx
	movb (%ecx), %bl
	cmpb $',', %bl
	je novi_broj

	cmpb $'0', %bl
	jb greska_2
	cmpb $'9', %bl
	ja greska_2

	subb $'0', %bl

	mull %edi
	andl %edx, %edx
	jnz greska_2
	addl %ebx, %eax
	jc greska_2

	incl %ecx

	jmp brojevi

novi_broj:

	incl %ecx
	movb (%ecx), %bl
	cmpb $']', %bl
	je gornja_opseg

	movl gornja, %ebx
	andl %ebx, %ebx
	jnz nelem

	movl %eax, donja
	xorl %eax, %eax

	jmp brojevi

gornja_opseg:

	movl %eax, gornja
	xorl %eax, %eax

	xorl %eax, %eax

	addl $2, %ecx
	jmp brojevi

nelem:
	
	movl donja, %ebx
	cmpl %ebx, %eax
	jb izvan
	
	movl gornja, %ebx
	cmpl %ebx, %eax
	ja izvan

	movl suma_u, %ebx
	addl %eax, %ebx
	jc greska_1
	movl %ebx, suma_u

	movb (%ecx), %bl
	cmpb $'}', %bl
	je uporedi_sume

	xorl %eax, %eax
	jmp brojevi

izvan:

	movl suma_izvan, %ebx
	addl %eax, %ebx
	jc greska_1
	movl %ebx, suma_izvan

	movb (%ecx), %bl
	cmpb $'}', %bl
	je uporedi_sume

	xorl %eax, %eax
	jmp brojevi
	
uporedi_sume:
	
	movl suma_u, %ebx

	cmpl %eax, %ebx
	ja manja_izvan
	jb manja_u
	
	movl %ebx, manja

	movl $4, %eax         # ispis2
	movl $1, %ebx
	leal ispis2, %ecx
	movl $len2, %edx
	int $0x80
	
	jmp hex

manja_izvan:

	movl %eax, manja

	movl $4, %eax         # ispis4
	movl $1, %ebx
	leal ispis4, %ecx
	movl $len4, %edx
	int $0x80

	jmp hex

manja_u:

	movl %ebx, manja

	movl $4, %eax         # ispis3
	movl $1, %ebx
	leal ispis3, %ecx
	movl $len3, %edx
	int $0x80
	
hex:

	movl manja, %eax
	movl $16, %edi
	movl $string, %ecx

	movb $'0', (%ecx)
	incl %ecx
	movb $'x', (%ecx)
	incl %ecx
	
pretvori:

	xorl %edx, %edx
	divl %edi

	cmpb $10, %dl
	jb dalje_pr

	addb $7, %dl

dalje_pr:

	addb $'0', %dl
	movb %dl, (%ecx)
	incl %ecx # next adresa
	andl %eax, %eax
	jnz pretvori

	movb $10, (%ecx)
	movl %ecx, %edi
	incl %edi

	decl %ecx
	movl $string, %esi

	subl %esi, %edi # duzina

	addl $2, %esi

obrni:

	cmpl %ecx, %esi
	jae ispis_sume

	movb (%ecx), %al
	movb (%esi), %ah
	movb %al, (%esi)
	movb %ah, (%ecx)

 	decl %ecx
	incl %esi

	jmp obrni

ispis_sume:

	movl $4, %eax         # ispis5
	movl $1, %ebx
	leal ispis_suma, %ecx
	movl $len5, %edx
	int $0x80

	movl $4, %eax         # suma
	movl $1, %ebx
	leal string, %ecx
	movl %edi, %edx
	int $0x80

	jmp kraj
	
greska_1:

	movl $4, %eax         # greska1
	movl $1, %ebx
	leal greska1, %ecx
	movl $len6, %edx
	int $0x80

	movl $1, %ebx
	movl %ebx, greska
	jmp kraj

greska_2:

	movl $4, %eax         # greska2
	movl $1, %ebx
	leal greska2, %ecx
	movl $len7, %edx
	int $0x80

	movl $1, %ebx
	movl %ebx, greska
	
kraj:

	movl $1, %eax
	movl greska, %ebx
	int $0x80
