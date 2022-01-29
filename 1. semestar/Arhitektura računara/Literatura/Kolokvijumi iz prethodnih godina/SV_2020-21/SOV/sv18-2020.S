# autor: Milica Sladakovic INDEX sv-18-2020
# SOV

.section .data

izraz_maks_d = 101
izraz: .fill izraz_maks_d, 1, 42

rezultat_str: .fill izraz_maks_d    # ovde smestiti stringovnu reprezentaciju rezultata i ne menjati naziv promenljive
rezultat: .long 0

# NE MENJATI TEKST PORUKA!
poruka_ulaz: .ascii "Unesite izraz: \0"
len1 = .-poruka_ulaz

poruka_rez: .ascii "Rezultat je: \0"
len_rez = .-poruka_rez

poruka_greska1: .ascii "Unet je prazan izraz!\n\0"
len_gr1 = .-poruka_greska1
poruka_greska2: .ascii "U nekoj od ulaznih vrednosti postoji cifra koja ne pripada brojnoj osnovi!\n\0"
len_gr2 = .-poruka_greska2
poruka_greska3: .ascii "Doslo je do prekoracenja prilikom konverzije nekog od operanada!\n\0"
len_gr3 = .-poruka_greska3
poruka_greska4: .ascii "Doslo je do prekoracenja prilikom sabiranja!\n\0"
len_gr4 = .-poruka_greska4

greska: .byte 0

.section .text
.global main

main:

	pushl $len1           # ispis1
	pushl $poruka_ulaz
	call ispis
	addl $8, %esp

	pushl $izraz_maks_d   # unos izraza
	pushl $izraz
	call upis
	addl $8, %esp

	movl $izraz, %ecx     # adresa stringa
	movl $10, %esi        # BAZA
	
	xorl %eax, %eax       # rezultat
	xorl %ebx, %ebx       # trenutni broj

	movb (%ecx), %bl
	cmpb $'\n', %bl
	je greska1

korak:

	movb (%ecx), %bl  
	cmpb $'+', %bl
	je saberi
	xorl %eax, %eax

str_to_inter:

	movb (%ecx), %bl
	cmpb $' ', %bl
	je nastavi

	cmpb $'\n', %bl
	je rezultat_to_str

	subb $'0', %bl
	
	cmpb $0, %bl       # donja_granica_sistema
	jl greska2
	cmpb $9, %bl       # gornja_granica_sistema
	jg greska2

	mull %esi
	andl %edx, %edx   
	jnz greska3
	addl %ebx, %eax
	jc greska3

	incl %ecx

	jmp str_to_inter

nastavi:

	pushl %eax          # operand se postavlja na stek

	incl %ecx
	jmp korak

saberi:

	popl %eax
	popl %ebx

	addl %ebx, %eax
	jc greska4
	movl %eax, rezultat  

	pushl rezultat      # rezultat postavlja na stek
					 # DOVDE

	movb greska, %bl
	cmpb $4, %bl
	je greska4

	incl %ecx
	xorl %eax, %eax
	movb (%ecx), %bl
	cmpb $'\n', %bl
	je rezultat_to_str
	incl %ecx
	jmp korak

greska1:

	pushl $len_gr1           # greska1
	pushl $poruka_greska1
	call ispis
	addl $8, %esp

	movb greska, %bl
	addb $1, %bl
	movb %bl, greska

	jmp kraj

greska2:

	pushl $len_gr2           # greska2
	pushl $poruka_greska2
	call ispis
	addl $8, %esp

	movb greska, %bl
	addb $2, %bl
	movb %bl, greska

	jmp kraj

greska3:

	pushl $len_gr3           # greska3
	pushl $poruka_greska3
	call ispis
	addl $8, %esp

	movb greska, %bl
	addb $3, %bl
	movb %bl, greska

	jmp kraj

greska4:

	pushl $len_gr4           # greska4
	pushl $poruka_greska4
	call ispis
	addl $8, %esp

	movb greska, %dl
	addb $4, %dl
	movb %dl, greska

	jmp kraj

rezultat_to_str:
	
 	movl rezultat, %eax
	movl $rezultat_str, %ecx

	movl $10, %ebx  # BAZA

pretvori:

	xorl %edx, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%ecx)
	incl %ecx # next adresa
	andl %eax, %eax
	jnz pretvori

	movb $'\n', (%ecx)

	movl %ecx, %edi         # adresa_kraja_stringa

	decl %ecx				 # priprema za obrtanje
	movl $rezultat_str, %esi # adresa_pocetka_stringa

	subl %esi, %edi         
	incl %edi				# duzina_stringa

obrni:

	cmpl %ecx, %esi
	jae ispisi_rezultat     # skok na ispis

	movb (%ecx), %al
	movb (%esi), %ah
	movb %al, (%esi)
	movb %ah, (%ecx)

 	decl %ecx
	incl %esi

	jmp obrni


ispisi_rezultat:

	pushl $len_rez          # poruka rezultata
	pushl $poruka_rez
	call ispis
	addl $8, %esp

	pushl %edi           # rezultat string
	pushl $rezultat_str
	call ispis
	addl $8, %esp

kraj:

	movl $1, %eax
	movl greska, %ebx
	int $0x80


###################################

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

