#autor: Milica

.section .data

poruka1: .ascii "Unesite prvi string: \0"
len1 = . - poruka1
poruka2: .ascii "Unesite drugi string: \0"
len2 = . - poruka2

prvi_string: .fill 40, 1, 0
len_prvi: .long 40

drugi_string: .fill 40, 1, 0
len_drugi: .long 40

razlika: .long 0

ispis1: .ascii "Prvi string ima vise malih slova nego drugi.\n\0"
len3 = . - ispis1
ispis2: .ascii "Drugi string ima vise malih slova od prvog.\n\0"
len4 = . - ispis2
ispis3: .ascii "Oba stringa imaju isti broj malih slova.\n\0"
len5 = . - ispis3

.section .text
.global main

main:

	movl $4, %eax
	movl $1, %ebx
	leal poruka1, %ecx   
	movl $len1, %edx
	int $0x80

	movl $3, %eax
	movl $0, %ebx
	leal prvi_string, %ecx   
	movl len_prvi, %edx
	int $0x80
	movl %eax, len_prvi

	movl $4, %eax
	movl $1, %ebx
	leal poruka2, %ecx   
	movl $len2, %edx
	int $0x80

	movl $3, %eax
	movl $0, %ebx
	leal drugi_string, %ecx   
	movl len_drugi, %edx
	int $0x80
	movl %eax, len_drugi

	xorl %esi, %esi
	
	xorl %eax, %eax	  # brojac_prvi
	xorl %ebx, %ebx	  # brojac_drugi
	xorl %edx, %edx   # 

prebroj_prvi:

	movb prvi_string(,%esi,1), %dl

	cmpb $'a', %dl
	jb dalje_prvi

	cmpb $'z', %dl
	ja dalje_prvi

	incl %eax

dalje_prvi:

	incl %esi
	cmpl len_prvi, %esi
	jb prebroj_prvi

	xorl %esi, %esi

prebroj_drugi:

	movb drugi_string(,%esi,1), %dl

	cmpb $'a', %dl
	jb dalje_drugi

	cmpb $'z', %dl
	ja dalje_drugi

	incl %ebx

dalje_drugi:

	incl %esi
	cmpl len_drugi, %esi
	jb prebroj_drugi

	cmpl %eax, %ebx
	ja drugi
	jb prvi

	movl $0, razlika
	
	movl $4, %eax
	movl $1, %ebx
	leal ispis3, %ecx   
	movl $len5, %edx
	int $0x80

	jmp kraj

prvi:

	subl %ebx, %eax
	movl %eax, razlika

	movl $4, %eax
	movl $1, %ebx
	leal ispis1, %ecx   
	movl $len3, %edx
	int $0x80

	jmp kraj

drugi:

	subl %eax, %ebx
	movl %ebx, razlika

	movl $4, %eax
	movl $1, %ebx
	leal ispis2, %ecx   
	movl $len4, %edx
	int $0x80

kraj:

	movl $1, %eax
	movl razlika, %ebx
	int $0x80


	
