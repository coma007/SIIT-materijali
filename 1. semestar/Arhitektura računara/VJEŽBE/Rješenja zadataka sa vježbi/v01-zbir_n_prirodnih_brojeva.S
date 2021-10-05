# Zbir prvih n prirodnih brojeva
# Imenko Prezimić ra1234

# Ulaz programa predstavlja vrednost u ecx registru
# Rezultat se na kraju nalazi u eax registru

.section .data
.section .text
.global main
main:
    movl $0, %eax    # zbir = 0
    movl $10, %ecx   # i = n
uporedi:
    cmpl $0, %ecx    # i==0 -> kraj
    je kraj
    addl %ecx, %eax  # zbir += i
    subl $1, %ecx    # i-= 1
    jmp uporedi

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

