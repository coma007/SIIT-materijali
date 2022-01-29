# autor: Milica Sladakovic INDEX sv18-2020
# T12

.section .data

unos: .ascii "Unesite string: \0"
len1 = . - unos
ispis: .ascii "Promenjen string je: \0"
len2 = . - ispis

len_max = 21                    # 20 korisnih + 1 za ENTER
string: .fill len_max, 1, 42    # mjesto za string koji se unosi

.section .text
.global main

main:

	xorl %esi, %esi            # brojac karaktera u stringu

	movl $4, %eax              # ispis prve poruke
	movl $1, %ebx
	leal unos, %ecx
	movl $len1, %edx
	int $0x80

	movl $3, %eax              # unos stringa
	movl $0, %ebx
	leal string, %ecx
	movl $len_max, %edx
	int $0x80

	cmpl $1, %eax              # ukoliko je prazan string
	je kraj

	movl $string, %ecx

	jmp smjena
	
smjena:

	movb (%ecx, %esi,1), %bl   # karakter n
	cmpb $'\n', %bl
	je kraj                    # ako je kraj stringa
	movb 1(%ecx, %esi,1), %dl  # karakter n+1
	cmpb $'\n', %dl
	je kraj                    # ako je kraj stringa

	xchgb %bl, %dl             # zamijeni karaktere
	movb %bl, (%ecx, %esi, 1)  # prepisi
	movb %dl, 1(%ecx, %esi, 1)

	addl $2, %esi              # idemo na nova dva karaktera
	jmp smjena

kraj:

	movl %eax, %esi            # duzina stringa, jer ce %eax kasnije biti zauzeto

	movl $4, %eax              # ispis poruke
	movl $1, %ebx
	leal ispis, %ecx
	movl $len2, %edx
	int $0x80

	movl $4, %eax              # ispis stringa
	movl $1, %ebx
	leal string, %ecx
	movl %esi, %edx
	int $0x80

	movl $1, %eax              # sistemski poziv za kraj programa
	movl $0, %ebx
	int $0x80
