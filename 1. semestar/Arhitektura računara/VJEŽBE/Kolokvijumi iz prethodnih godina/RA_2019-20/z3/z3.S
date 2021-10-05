#autor: milica

.section .data

prompt1: .ascii "Unesite logicki izraz: \0"
len1 = .- prompt1
prompt2: .ascii "Rezultat: \0"
len2 = .- prompt2
err1: .ascii "Greska kod operanda.\n\0"
len4 = .- err1
err2: .ascii "Greska kod operacije.\n\0"
len3 = .- err2
newline: .ascii "\n\0"

log: .fill 101, 1, 42     # 100 ef i ENTER

brojac: .word 0
operation: .ascii "&\0"

rezultat: .byte 0

rezultat_str: .fill 9, 1, 42  # 8 cifara i ENTER
len_max: .long 9

greska: .byte 0

.section .text
.global main

main:

	movl $4, %eax         # ispis1
	movl $1, %ebx
	leal prompt1, %ecx
	movl $len1, %edx
	int $0x80

	movl $3, %eax         # unos logickog izraza
	movl $0, %ebx
	leal log, %ecx
	movl $101, %edx
	int $0x80

	movl %ecx, %edi       # adresa log

	xorl %ecx, %ecx       # sistem

	xorl %esi, %esi       # pokazivac

prepoznaj_broj:

	xorl %eax, %eax       # trebace kasnije sigurno
	xorl %ebx, %ebx

	movb 1(%edi,%esi,1), %bl
	cmpb $'x', %bl
	jne str_dec_to_inter

	addl $2, %esi

str_hex_to_inter:

	movb $16, %bh

	movb (%edi, %esi,1), %bl
    cmpb $' ', %bl
	je operacija
	cmpb $10, %bl
	je operacija

	cmpb $'f', %bl
	ja greska_operand

	cmpb $'a', %bl
	jb veliko

	subb $'a'-'A', %bl

veliko:

	cmpb $'A', %bl
	jb dalje_hex

	subb $7, %bl

dalje_hex:

	subb $'0', %bl
	
	cmpb $0x0, %bl
	jl greska_operand
	cmpb $0xf, %bl
	jg greska_operand

	mulb %bh
	andb %ah, %ah
	jnz greska_operand
	addb %bl, %al
	jc greska_operand

	incl %esi

	jmp str_hex_to_inter

str_dec_to_inter:

	movb $10, %bh

	movb (%edi, %esi,1), %bl
    cmpb $' ', %bl
	je operacija
	cmpb $10, %bl
	je operacija

	subb $'0', %bl
	
	cmpb $0, %bl
	jl greska_operand
	cmpb $9, %bl
	jg greska_operand

	mulb %bh
	andb %ah, %ah
	jnz greska_operand
	addb %bl, %al
	jc greska_operand

	incl %esi

	jmp str_dec_to_inter

operacija:

	movb %al, %cl

	movb rezultat, %al

	movb operation, %bh
	cmpb $'<', %bh
	je lijevo
    cmpb $'>', %bh
	je desno
	cmpb $'^', %bh
	je ksor

	movb %cl, rezultat
	jmp prepoznaj_operacija


lijevo:

	rolb %cl, %al
	movb %al, rezultat

	cmpb $10, %bl
	je oct

	jmp prepoznaj_operacija

desno:

	rorb %cl, %al
	movb %al, rezultat

	cmpb $10, %bl
	je oct

	jmp prepoznaj_operacija

ksor:

	xorb %cl, %al
	movb %al, rezultat

	cmpb $10, %bl
	je oct
    
prepoznaj_operacija:

	xorl %ebx, %ebx

	incl %esi
	
	movb (%edi, %esi,1), %bl
	cmpb $'<', %bl
	je zapamti
    cmpb $'>', %bl
	je zapamti
	cmpb $'^', %bl
	je zapamti

	jmp greska_operacija

zapamti:
	
	movw %bx, operation

	addl $2, %esi
	jmp prepoznaj_broj

greska_operand:

	movl $4, %eax         # greska1
	movl $1, %ebx
	leal err1, %ecx
	movl $len4, %edx
	int $0x80

	jmp greska_upisi

greska_operacija:

	movl $4, %eax         # greska2
	movl $1, %ebx
	leal err2, %ecx
	movl $len3, %edx
	int $0x80

greska_upisi:

	incl greska
	
	movl $1, %eax
	movl greska, %ebx
	int $0x80

oct:

	movb $8, %bl
	movb rezultat, %al
	xorl %esi, %esi

pretvori:

	xorb %ah, %ah

	xorl %edx, %edx
	divb %bl
	addb $'0', %ah
	movb %ah, rezultat_str(,%esi,1)
	incl %esi # next adresa
	andb %al, %al
	jnz pretvori

	movb $0, rezultat_str(,%esi,1)

	movl %esi, len_max
 
	decl %esi        # kraj str
	xorl %edi, %edi  # pocetak str

obrni:

	cmpl %edi, %esi
	jbe kraj

	movb rezultat_str(,%edi,1), %al
	movb rezultat_str(,%esi,1), %ah
	movb %al, rezultat_str(,%esi,1)
	movb %ah, rezultat_str(,%edi,1)

 	decl %esi
	incl %edi

	jmp obrni

kraj:
	
	movl $4, %eax         # ispis2
	movl $1, %ebx
	leal prompt2, %ecx
	movl $len2, %edx
	int $0x80

	movl $4, %eax         # rezultat
	movl $1, %ebx
	leal rezultat_str, %ecx
	movl len_max, %edx
	int $0x80

	movl $1, %eax
	movl greska, %ebx
	int $0x80
