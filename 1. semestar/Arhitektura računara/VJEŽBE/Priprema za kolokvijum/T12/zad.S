# MIlica Sladakovic INDEX SV 18/2020
# priprema T12
# ----------------------------------

.section .data

#NELEM = 6
#niz: .quad 12, -4, 5, 7, 14, 6

#NELEM = 7
#niz: .quad -2, 12, -4, 5, 7, 14, -1

NELEM = 6
niz: .quad 0x0000e001FFFFFFFF, 0x00000001FFFFFFFF, 0x80000001FFFFFFFF, 0x20000001FFFFFFFF, 0xFFFFFFFFFFFFFFFD, 0x7FFFFFFFFFFFFFFF

#NELEM = 3
#niz: .quad -12, -5, -137

#NELEM = 0
#niz: .quad 

najblizi_indeks: .long 0
greska: .long 0

.section .text
.globl main

main:

	xorl %esi, %esi
	cmpl $NELEM, %esi
	jge pogresio
	
	movl $niz, %eax
	movl 4(%eax, %esi, 8), %ebx 	# visi dijelovi _ clan niza
	movl (%eax, %esi, 8), %eax		# nizi dijelovi _ clan niza

	movl %eax, %ecx					# nizi dijelovi _ razlika
	movl %ebx, %edx					# visi dijelovi _ razlika

	cmpl $0, %ebx
	jge dalje

negiraj_prvi:

	notl %edx
	notl %ecx
	addl $1, %ecx
	adcl $0, %edx
	jc pogresio

dalje:

	cmpl $NELEM, %esi
	je kraj

	incl %esi
	movl $niz, %eax
	movl 4(%eax, %esi, 8), %ebx 
	movl (%eax, %esi, 8), %eax

provjeri_negaciju:

	cmpl $0, %ebx
	jge uporedi_vise

	notl %ebx
	notl %eax
	addl $1, %eax
	adcl $0, %ebx

uporedi_vise:

	cmpl %ebx, %edx
	jb dalje
	ja premjesti

	cmpl %eax, %ecx 
	jbe dalje

premjesti:

	movl %eax, %ecx
	movl %ebx, %edx

	movl %esi, najblizi_indeks

	jmp dalje


pogresio:

	incl greska


kraj:

	movl $1, %eax
	movl greska, %ebx
	int $0x80


