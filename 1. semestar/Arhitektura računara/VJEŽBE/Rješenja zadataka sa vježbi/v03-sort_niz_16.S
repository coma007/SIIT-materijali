# Sort 16-bitnog niza u rastućem redosledu
# Imenko Prezimić ra1234

.section .data
NELEM=10
niz:    .word 5,2,6,88,0,3342,-4,10,22,623

.section .text
.global main

main:
    movl $niz, %ebx     #bazni registar za unutrašnju petlju
    movl $NELEM, %esi   #brojač za spoljašnju petlju
spolja:     #glavna petlja
    decl %esi
    jz kraj_spolja
    movl $NELEM, %edi   #indeks za unutrašnju petlju
unutra:     #unutrašnja petlja
    decl %edi
    jz spolja

    movw (%ebx, %edi, 2), %ax
    movw -2(%ebx, %edi, 2), %dx
    cmpw %dx, %ax  #poređenje sa prethodnikom
    jnl unutra
zameni:            #ako je manji, zameni im mesta
    movw %ax, -2(%ebx, %edi, 2)
    movw %dx, (%ebx, %edi, 2)
    jmp unutra
kraj_spolja:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

