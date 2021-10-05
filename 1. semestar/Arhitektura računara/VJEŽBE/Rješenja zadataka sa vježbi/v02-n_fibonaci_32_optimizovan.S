# Pronalaženje n-tog fibonačijevog broja
# Imenko Prezimić ra1234

# Optimizovana verzija - koristi samo f1 i f2
# i direktno umanjuje n

.section .data
n:  .long 8
f:  .long 0
greska: .byte 0

.section .text
.globl main
main:
    movl $1, %eax   #f1
    movl %eax, %ebx #f2
petlja:
    cmpl $2, n
    jbe kraj
    addl %eax, %ebx
    jc prekoracenje
    xchgl %eax, %ebx
    decl n
    jmp petlja
prekoracenje:
    incb greska
kraj:
    movl %eax, f
    movl $1, %eax
    movl $0, %ebx
    int $0x80

