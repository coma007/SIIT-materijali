# Sumiranje intervala niza
# Imenko Prezimić ra1234

.section .data
NELEM  = 10
niz:   .long 1,2,3,4,5,6,7,8,9,10
suma:  .long 0
ind1:  .long 2
ind2:  .long 6

.section .text
.globl main
main:
    movl ind1, %esi #kreće se od indeksa ind1
    movl $0, %eax
petlja:
    addl niz(,%esi,4), %eax
    incl %esi
    cmpl ind2, %esi
    jle petlja      #završava se sa indeksom ind2
kraj:
    movl %eax, suma
    movl $1, %eax
    movl $0, %ebx
    int $0x80

