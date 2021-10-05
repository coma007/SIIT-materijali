# Pronalaženje n-tog fibonačijevog broja
# Imenko Prezimić ra1234

.section .data
n:  .long 8
f:  .long 0
greska: .byte 0

.section .text
.globl main
main:
    movl $1, %eax   #f1
    movl $1, %ebx   #f2
    movl $2, %ecx   #i
petlja:
    cmpl n, %ecx
    jae kraj
    movl %eax, %edx
    addl %ebx, %edx
    jc prekoracenje
    movl %ebx, %eax
    movl %edx, %ebx
    addl $1, %ecx
    jmp petlja
prekoracenje:
    incb greska
kraj:
    movl %ebx, f
    movl $1, %eax
    movl $0, %ebx
    int $0x80

