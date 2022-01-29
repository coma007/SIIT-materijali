#autor: milica

.section .data
ispis1:     .ascii "Unseite logicki izraz: \0"
len1 = .- ispis1
ispis2:     .ascii "Rezultat: \0"
len2 = .- ispis2
greska1:    .ascii "Greska kod operanda.\n\0"
len3 = .- greska1
greska2:    .ascii "Greska kod operacije.\n\0"
len4 = .- greska2
newlin:     .ascii "\n\0"

log: .fill 101, 1, 42     # 100 ef i ENTER

brojac: .word 0
operation: .ascii "&\0"

zadnji_znak: .fill 0,1,42

rezultat: .byte 0b11111111

rezultat_str: .fill 9, 1, 42  # 8 cifara i ENTER
len_max: .long 9

greska: .byte 0

.section .text
.global main

main:

	pushl $len1           # ispis1
	pushl $ispis1
	call ispis
	addl $8, %esp

	pushl $101            # unos logickog izraza
	pushl $log
	call upis
	addl $8, %esp

	movl %eax, %edi       # adresa log
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

	xorl %ecx, %ecx

	movb rezultat, %ch

	movb operation, %bh
	cmpb $'&', %bh
	je i
    cmpb $'|', %bh
	je ili
	cmpb $'^', %bh
	je ksor

i:
	andb %al, %ch
	movb %ch, rezultat

	cmpb $10, %bl
	je oct

	jmp prepoznaj_operacija

ili:

	orb %al, %ch
	movb %ch, rezultat

	cmpb $10, %bl
	je oct

	jmp prepoznaj_operacija

ksor:

	xorb %al, %ch
	movb %ch, rezultat

	cmpb $10, %bl
	je oct
    
prepoznaj_operacija:

	xorl %ebx, %ebx

	incl %esi
	
	movb (%edi, %esi,1), %bl
	cmpb $'&', %bl
	je zapamti
    cmpb $'|', %bl
	je zapamti
	cmpb $'^', %bl
	je zapamti

	jmp greska_operacija

zapamti:
	
	movw %bx, operation

	addl $2, %esi
	jmp prepoznaj_broj

oct:

	call inter

	jmp kraj

greska_operand:

	pushl $len3           # greska1
	pushl $greska1
	call ispis
	addl $8, %esp

	jmp greska_upisi

greska_operacija:

	pushl $len4           # greska2
	pushl $greska2
	call ispis
	addl $8, %esp

greska_upisi:

	incl greska
	
	movl $1, %eax
	movl greska, %ebx
	int $0x80


kraj:
	
	pushl $len2         # ispis2
	pushl $ispis2
	call ispis
	addl $8, %esp

	pushl len_max       # ispis_rezultata
	pushl $rezultat_str
	call ispis
	addl $8, %esp

	movl $1, %eax
	movl greska, %ebx
	int $0x80





# vraca NISTA (*adresa, druzina)
# ispis

ispis:

	pushl %ebp
	movl %esp, %ebp

	pushl %ebx

	movl $4, %eax      
	movl $1, %ebx
	movl 8(%ebp), %ecx
	movl 12(%ebp), %edx
	int $0x80

ispis_kraj:

	popl %ebx
	movl %ebp, %esp

	popl %ebp
	ret


# vraca NISTA (*adresa, duzina)
# upis

upis:

	pushl %ebp
	movl %esp, %ebp

	pushl %ebx

	movl $3, %eax      
	movl $0, %ebx
	movl 8(%ebp), %ecx
	movl 12(%ebp), %edx
	int $0x80

	movl %ecx, %eax

upis_kraj:

	popl %ebx
	movl %ebp, %esp

	popl %ebp
	ret


# vraca NISTA
# inter > str

inter:

	pushl %ebp
	movl %esp, %ebp

	pushl %esi
	pushl %ebx
	pushl %edi

	xorl %eax, %eax
	xorl %ebx, %ebx

	movb $8, %bl
	movb rezultat, %al
	xorl %esi, %esi

pretvori:

	xorb %ah, %ah

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
	jbe kraj_inter

	movb rezultat_str(,%edi,1), %al
	movb rezultat_str(,%esi,1), %ah
	movb %al, rezultat_str(,%esi,1)
	movb %ah, rezultat_str(,%edi,1)

 	decl %esi
	incl %edi

	jmp obrni

kraj_inter:

	popl %edi
	popl %ebx
	popl %esi
	
	movl %ebp, %esp
	popl %ebp
	ret

