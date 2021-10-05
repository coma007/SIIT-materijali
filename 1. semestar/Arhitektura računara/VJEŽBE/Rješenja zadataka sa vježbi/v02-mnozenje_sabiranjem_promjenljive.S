# Množenje pomoću sabiranja
# Imenko Prezimić ra1234

# Koristi promenljive, optimizovana varijanta
# Uvek manji broj puta sabira veći broj

.section .data
a:	.long 123
b:	.long 456
p:	.long 0

.section .text
.globl main
main:
    movl a, %eax
    movl $0, p
    cmpl %eax, b     # b ? a
    jb uporedi       # ako je b < a, skoči
    xchgl %eax, b    # u suprotnom, zameni vrednosti a i b
uporedi:
    cmpl $0, b       # b == 0
    je kraj
    addl %eax, p     # p += a
    subl $1, b       # b -= 1
    jmp uporedi

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

