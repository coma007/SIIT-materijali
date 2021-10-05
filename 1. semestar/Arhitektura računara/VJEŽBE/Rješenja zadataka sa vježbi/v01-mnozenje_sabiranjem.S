# Množenje pomoću sabiranja
# Imenko Prezimić ra1234

# Ulaz programa predstavljaju vrednosti u eax i ebx registrima
# Rezultat se na kraju nalazi u ecx registru

.section .data
.section .text
.global main
main:
    movl $5, %eax    # a
    movl $3, %ebx    # b
    movl $0, %ecx    # r
uporedi:
    cmpl $0, %eax    # a ? 0
    je kraj          # ako je a == 0, skoči
    addl %ebx, %ecx  # r += b
    subl $1, %eax    # a -= 1
    jmp uporedi

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

