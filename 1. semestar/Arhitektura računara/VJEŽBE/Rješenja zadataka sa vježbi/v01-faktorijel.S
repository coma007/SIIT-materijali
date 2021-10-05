# Računanje faktorijela, pr čemu se za množenje
# koristi množenje pomoću sabiranja
# Imenko Prezimić ra1234

.section .data
.section .text
.globl main
main:
    movl $6, %esi   # N
    movl $1, %edi   # faktorijel

pocetak:
    cmpl $1, %esi
    jbe kraj
    movl %esi, %eax
    movl %edi, %ebx

# Množenje pomoću sabiranja - Ulaz: eax, ebx
mnozi:
    movl $0, %ecx
mnozi_petlja:
    cmpl $0, %eax
    je fakt_petlja
    addl %ebx, %ecx
    decl %eax
    jmp mnozi_petlja
# Množenje pomoću sabiranja - Izlaz: ecx

fakt_petlja:
    movl %ecx, %edi
    decl %esi
    jmp pocetak

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

