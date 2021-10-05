# Uklanjanje razmaka sa početka i kraja stringa
# Imenko Prezimić ra1234

.section .data
s:  .ascii "    Neki tekst    \0"

.section .text
.globl main
main:
    movl $s, %eax
kraj_s:
    cmpb $0, (%eax)
    je razmacik
    incl %eax
    jmp kraj_s
razmacik:
    cmpb $' ', -1(%eax)
    jne izbacik
    decl %eax
    jmp razmacik
izbacik:
    movb $0, (%eax)
razmacip:
    movl $s, %eax  #spoljašnja petlja
    cmpb $' ', (%eax)
    jne kraj
izbacip:
    cmpb $0, (%eax)     #unutrašnja petlja
    je razmacip
    movb 1(%eax), %bl
    movb %bl, (%eax)
    incl %eax
    jmp izbacip
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

