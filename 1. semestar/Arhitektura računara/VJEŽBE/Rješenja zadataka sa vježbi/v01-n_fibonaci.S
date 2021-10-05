# Pronalaženje n-tog fibonačijevog broja
# Imenko Prezimić ra1234

.section .data
.section .text
.globl main
main:
    movl $15, %esi  # N
    movl $1, %eax   # f1
    movl $1, %ebx   # f2 (ovde ce na kraju biti i rezultat)
    movl $2, %ecx   # i
petlja:
    cmpl %esi, %ecx
    jae kraj
    movl %eax, %edx
    addl %ebx, %edx
    movl %ebx, %eax
    movl %edx, %ebx
    addl $1, %ecx
    jmp petlja
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

