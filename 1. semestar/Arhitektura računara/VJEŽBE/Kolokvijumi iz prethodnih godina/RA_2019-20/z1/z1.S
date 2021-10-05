#autor: Milica

.section .data
prompt_1: .ascii "Unesite string: \0"
len_1 = . - prompt_1

prompt_2: .ascii "Enkodovan string: \0"
len_2 = . - prompt_2

len_max = 50
string: .fill len_max,1,42

nova_duzina: .long 0

.section .text
.global main

main:

	movl $4, %eax
	movl $0, %ebx
	leal prompt_1, %ecx
	movl $len_1, %edx
	int $0x80

	movl $3, %eax
	movl $1, %ebx
	leal string, %ecx
	movl $len_max, %edx
	int $0x80
	movl %eax, nova_duzina
	decl nova_duzina

	xorl %esi, %esi

cezar:

	movb string(,%esi,1), %dl # trenutno slovo

	cmpb $'C', %dl
	jbe provjeri_veliko

	cmpb $'Z', %dl
	jbe slovo

	cmpb $'z', %dl
	ja dalje

	cmpb $'c', %dl
	jbe provjeri_malo

	jmp slovo

provjeri_veliko:

	cmpb $'A', %dl
	jb dalje

	cmpb $'Z', %dl
	ja dalje

	addb $26, %dl
	subb $3, %dl
	jmp dalje

provjeri_malo:

	cmpb $'a', %dl
	jb dalje

	addb $26, %dl
	subb $3, %dl
	jmp dalje
	
slovo:

	subb $3, %dl

dalje:

	movb %dl, string(,%esi,1)
	
	incl %esi

	cmpl nova_duzina, %esi
	jb cezar

ispis:

	incl nova_duzina

	movl $4, %eax
	movl $0, %ebx
	leal prompt_2, %ecx
	movl $len_2, %edx
	int $0x80

	movl $4, %eax
	movl $0, %ebx
	leal string, %ecx
	movl nova_duzina, %edx
	int $0x80


kraj:

	movl $1, %eax
	movl $0, %ebx
	int $0x80

