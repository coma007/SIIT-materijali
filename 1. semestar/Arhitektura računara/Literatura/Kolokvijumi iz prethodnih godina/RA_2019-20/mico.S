#autor: Milos Marjanovic INDEX ra172-2019
.section .data

prompt_1: .ascii "Unesite string: \0"
	prompt_1_len= . - prompt_1

prompt_2: .ascii "Enkodovan string: \0"
	prompt_2_len= . - prompt_2

	str_max=51
	str:	.fill str_max,1,0

.section .text
.globl main
main:
	xorl %eax, %eax		#ovdje cuvamo broj

	movl $4, %eax		#ispise poruku da se unese string
	movl $1, %ebx
	leal prompt_1, %ecx
	movl $prompt_1_len, %edx
	int $0x80
	
	movl $3, %eax		#unesemo string
	movl $0, %ebx
	leal str, %ecx
	movl $str_max, %edx
	int $0x80

	leal str, %eax		#smejesti adresu stringa u eax 
	jmp Cezarovo_kodiranje
Cezarovo_kodiranje_znak:
	incl %eax
Cezarovo_kodiranje:
	cmpb $0, (%eax)		#provjerava da li je kraj
	je kraj
	cmpb $65, (%eax)
	jl Cezarovo_kodiranje_znak	#ako je karakteru vrijednost manja od 65 sigurno nije niti malo niti veliko slovo
	cmpb $68, (%eax)
	jl kodiraj26
	cmpb $122, (%eax)
	ja Cezarovo_kodiranje_znak
	cmpb $96, (%eax)
	ja kodiraj
	cmpb $91, (%eax)
	jl kodiraj
	jmp Cezarovo_kodiranje_znak
kodiraj:
	cmpb $91, (%eax)
	jl preskoci
	cmpb $100, (%eax)
	jl kodiraj26
preskoci:
	subb $3, (%eax)
	incl  %eax
	jmp Cezarovo_kodiranje
kodiraj26:
	subb $3, (%eax)
	addb $26, (%eax)
	incl %eax
	jmp Cezarovo_kodiranje
kraj:
	
	movl $4, %eax
	movl $1, %ebx
	leal prompt_2, %ecx
	movl $prompt_2_len, %edx
	int $0x80

	movl $4, %eax
	movl $1, %ebx
	leal str, %ecx
	movl $str_max, %edx
	int $0x80

	movl $1,  %eax
	movl $0, %ebx
	int $0x80
--------------------------------------------------------------------------------------------------------------------------------------------

#autor: Milos Marjanovic INDEX ra172-2019
#int encode(char* izvorni, char* ciljni, char* enkodovati);

.section .text
.globl encode

encode:
	pushl %ebp
	movl %esp, %ebp
	pushl %esi
	pushl %ebx
	pushl %edi
	movl 16(%ebp), %eax	#string
	movl 12(%ebp), %ecx	#ciljna slova
	movl 8(%ebp), %edx	#prvobitna (izvorna) slova

	xorl %esi, %esi 	#brojac
	xorl %edi, %edi
	xorl %ebx, %ebx		#temp
	jmp exchange
sljedeci:
	incl %eax
	subl %esi, %edx
	subl %esi, %ecx
	xorl %esi, %esi
exchange:
	cmpb $0, (%eax)	#provjerava da li je kraj stringa
	je kraj
	cmpb $0, (%edx)	#provjerava da li smo uporedili sa svim izvornim slovima
	je sljedeci
	movb (%edx), %bl
	cmpb (%eax), %bl
	je zamjena
	incl %edx	
	incl %ecx
	incl %esi
	jmp exchange
zamjena:
	movb (%ecx), %bl
	movb %bl, (%eax)
	incl %eax
	subl %esi, %edx
	subl %esi, %ecx
	xorl %esi, %esi
	incl %edi
	jmp exchange

kraj:
	xorl %eax, %eax
	movl %edi, %eax
	popl %edi
	popl %ebx
	popl %esi
	movl %ebp, %esp
	popl %ebp
	ret
------------------------------------------------------------------------------------------------------------------------------------------

#autor: Milos Marjanovic INDEX ra172-2019

.section .data
	prompt1: .ascii "Unesite logicki izraz: \0"
	prompt_1_len= . - prompt1

	max_izraz=101
	izraz:	.fill max_izraz,1,0
	
	prompt2: .ascii "Rezultat: \0"
	prompt_2_len= . - prompt2

	err1: .ascii "Greska kod operanda.\n\0"
	err1_len= . - err1

	err2: .ascii "Greska kod operacije.\n\0"
	err2_len= . - err2
	newline: .ascii "\n\0"
	
	operand1:	.long 0
	operand2:	.long 0
	broj_nula:	.long 0	
	prvi_operand:	.long 0
	koja_operacija:	.long 0
	
	rjesenje:	.fill max_izraz,1,0
.section .text
.globl main
main:
	movl $4, %eax		#ispise poruku da se unese string
	movl $1, %ebx
	leal prompt1, %ecx
	movl $prompt_1_len, %edx
	int $0x80

	movl $3, %eax		#unesemo string
	movl $0, %ebx
	leal izraz, %ecx
	movl $max_izraz, %edx
	int $0x80

	leal izraz, %esi
	jmp petlja
prije_petlje:
	cmpb $60, (%esi)
	je operacija
	cmpb $62, (%esi)
	je operacija
	cmpb $94, (%esi)
	je operacija
petlja:
	movl $0, broj_nula
	cmpb $0, (%esi)
	je prije_konverzija_oktalni
	cmpb $32, (%esi)
	je operacija
	cmpb $'\n', (%esi)
	je operacija
	cmpl $1, broj_nula
	je dekadni
	cmpb $48, (%esi)
	je provjera_nula
dekadni:
	xorl %eax, %eax
	xorl %ebx, %ebx
	movl $10, %ecx	#baza dekadnog
	movl $0, broj_nula
dek_konverzija:
	cmpb $'\n', (%esi)	#kraj
	je kraj_dek_konverzije
	cmpb $32, (%esi)
	je kraj_dek_konverzije
	cmpb $48, (%esi)
	jl greska_operand
	cmpb $57, (%esi)
	ja greska_operand
	movb (%esi), %bl
	andb %bl, %bl
	jz kraj_dek_konverzije	#zavrsili sa operandom
	subb $'0', %bl
	mull %ecx
	addl %ebx, %eax
	incl %esi
	jmp dek_konverzija
kraj_dek_konverzije:
	cmpl $0, prvi_operand
	jne preskoci_operand
	movl %eax, operand1
	xorl %eax, %eax
	xorl %ebx, %ebx
	incl prvi_operand
	jmp petlja
preskoci_operand:
	movl %eax, operand2
	xorl %eax, %eax
	xorl %ebx, %ebx
	jmp petlja
	
provjera_nula:
	incl broj_nula
	incl %esi
	cmpb $120, (%esi)
	je prije_hex_konverzije
	cmpb $88, (%esi)
	je prije_hex_konverzije
	jmp petlja
prije_hex_konverzije:
	incl %esi
	xorl %eax, %eax
	xorl %ebx, %ebx
	movl $16, %ecx	#baza hex
heks_konverzija:
	cmpb $'\n', (%esi)	#kraj
	je kraj_dek_konverzije
	cmpb $32, (%esi)
	je kraj_dek_konverzije	
	movb (%esi), %bl	#znak u donjih osam bita %ebx
	cmpb $48, (%esi)	#u ovim uporedjivanjima saznajemo da li su
	jl greska_operand	#znakovi koji pripadaju heksadecimalnom brojnom sistemu
	cmpb $58, (%esi)
	jl petlja_brojevi		
	cmpb $102, (%esi)	#mala slova od a do f
	ja greska_operand
	cmpb $96, (%esi)
	ja petlja_mala_slova
	cmpb $70, (%esi)	#velika slova od A do F
	ja greska_operand
	cmpb $64, (%esi)
	ja petlja_slova
petlja_brojevi:
	subb $'0', %bl
	mull %ecx
	addl %ebx, %eax
	incl %esi
	jmp heks_konverzija
petlja_slova:
	subb $'7', %bl		#55 oduzmemo od znakova A do F da dobijemo njihove interne vrijednosti
	mull %ecx
	addl %ebx, %eax
	incl %esi
	incl %edi
	jmp heks_konverzija
petlja_mala_slova:
	subb $'W', %bl		#87 oduzmemo od znakova a do f da dobijemo njihove interne vrijednosti
	mull %ecx
	addl %ebx, %eax
	incl %esi
	incl %edi
	jmp heks_konverzija
zadnji_operand:
	jmp kraj
operacija:
	incl %esi
	cmpl $1, koja_operacija
	je ili
	cmpl $2, koja_operacija
	je lijevo
	cmpl $3, koja_operacija
	je desno
	cmpb $94, (%esi)
	je operacija_ili
	cmpb $60, (%esi)
	je operacija_lijevo
	cmpb $62, (%esi)
	je operacija_desno
	jmp greska_operacija
operacija_ili:
	movl $1, koja_operacija
	addl $2, %esi
	jmp petlja
operacija_lijevo:
	movl $2, koja_operacija
	addl $2, %esi
	jmp petlja
operacija_desno:
	movl $3, koja_operacija
	addl $2, %esi
	jmp petlja
ili:
	movl operand2, %edi
	xorl %edi, operand1
	jmp prije_petlje
lijevo:
	movb operand1, %al
	movb operand2, %cl
	rolb %cl, %al
	jmp ubaci_broj
desno:
	movb operand1, %al
	movb operand2, %cl
	rorb %cl, %al
	jmp ubaci_broj
	
ubaci_broj:
	movl $0, koja_operacija
	movb %dl, operand1
	jmp petlja
	
greska_operand:
	movl $4, %eax		
	movl $1, %ebx
	leal err1, %ecx
	movl $err1_len, %edx
	int $0x80
	
	movl $1,  %eax
	movl $1, %ebx
	int $0x80

greska_operacija:
	movl $4, %eax		
	movl $1, %ebx
	leal err2, %ecx
	movl $err2_len, %edx
	int $0x80
	
	movl $1,  %eax
	movl $1, %ebx
	int $0x80
prije_konverzija_oktalni:
	movl operand1, %eax
	leal rjesenje, %edi
	movl $8, %ebx
konverzija_oktalni:
	xorl %edx, %edx		#neophodan zbog divl
	divl %ebx		#eax / ebx -> eax ostatak u edx
	addb $'0', %dl
	movb %dl, (%edi)
	incl %edi
	andl %eax, %eax
	jnz konverzija_oktalni
	movb $0, (%edi)		#kraj stringa
	decl %edi		#obrtanje stringa
	leal rjesenje, %esi
obrni:
	cmpl %edi, %esi
	jae kraj
	movb (%esi), %ah
	movb (%edi), %al
	movb %al, (%esi)
	movb %ah, (%edi)
	decl %edi
	incl %esi
	jmp obrni
	

kraj:
	movl $4, %eax		
	movl $1, %ebx
	leal prompt2, %ecx
	movl $prompt_2_len, %edx
	int $0x80

	movl $4, %eax		
	movl $1, %ebx
	leal rjesenje, %ecx
	movl $max_izraz, %edx
	int $0x80

PS: Ovaj zadnji nije skroz dobar, ne mogu se sjetiti sta sam sve trebao popraviti da bude skroz tacan.
