# Množenje pomoću sabiranja
# Imenko Prezimić ra1234

# Optimizovana varijanta
# Uvek manji broj puta sabira veći broj

.section .data
.section .text
.globl main
main:
    movl $5, %eax    # a
    movl $3, %ebx    # b
    movl $0, %ecx    # r
    cmpl %eax, %ebx  # b ? a
    ja uporedi       # ako je b > a, skoči
    xchgl %eax, %ebx # u suprotnom, zameni vrednosti a i b
uporedi:
    cmpl $0, %eax    # a == 0
    je kraj
    addl %ebx, %ecx  # r += b
    subl $1, %eax    # a -= 1
    jmp uporedi

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

