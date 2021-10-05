# Množenje pomoću sabiranja, dvostruka preciznost
# Imenko Prezimić ra1234

.section .data
a:  .quad 0x10
b:  .quad 0x10000000
r:  .quad 0 #rezultat treba da bude 0x00000001 00000000
greska: .byte 0

.section .text
.globl main
main:
    movl b, %eax
    movl b+4, %ebx
mnozi:
    cmpl $0, a
    jne mnozi2
    cmpl $0, a+4
    je kraj
mnozi2:
    addl %eax, r
    adcl %ebx, r+4
    jc prekoracenje
    subl $1, a
    sbbl $0, a+4
    jmp mnozi
prekoracenje:
    incb greska
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

