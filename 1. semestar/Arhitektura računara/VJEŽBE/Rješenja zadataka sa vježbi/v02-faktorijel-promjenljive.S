# Računanje faktorijela, pr čemu se za množenje
# koristi množenje pomoću sabiranja
# Imenko Prezimić ra1234

.section .data
n:  .long 6
f:  .long 1
greska: .byte 0

.section .text
.globl main
main:
    cmpl $1, n
    jbe kraj
    movl n, %eax
    movl f, %ebx
# Množenje pomoću sabiranja - Ulaz: eax, ebx
mnozi:
    movl $0, %ecx
mnozi_petlja:
    cmpl $0, %eax
    je fakt_petlja
    addl %ebx, %ecx
    jc prekoracenje
    decl %eax
    jmp mnozi_petlja
# Množenje pomoću sabiranja - Izlaz: ecx
fakt_petlja:
    movl %ecx, f
    decl n
    jmp main
prekoracenje:
    incb greska
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

