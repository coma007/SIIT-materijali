# Pronalaženje n-tog fibonačijevog broja, dvostruka preciznost
# Imenko Prezimić ra1234

.section .data
n:  .long 50
f:  .quad 0
greska: .byte 0

.section .text
.globl main
main:
    movl $1, %eax   #f1
    movl $0, %ebx
    movl $1, %ecx   #f2
    movl $0, %edx
petlja:
    cmpl $2, n
    jbe kraj
    addl %eax, %ecx
    adcl %ebx, %edx
    jc prekoracenje
    xchgl %eax, %ecx
    xchgl %ebx, %edx
    decl n
    jmp petlja
prekoracenje:
    incb greska
kraj:
    movl %eax, f
    movl %ebx, f+4
    movl $1, %eax
    movl $0, %ebx
    int $0x80

