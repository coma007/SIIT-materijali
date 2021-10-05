# deljenje pomoću oduzimanja, dvostruka preciznost
# Imenko Prezimić ra1234

.section .data
a:  .quad 12345678
b:  .quad 912
k:  .quad 0
o:  .quad 0
greska: .byte 0

.section .text
.globl main
main:
    movl a, %eax
    movl a+4, %ebx
    cmpl $0, b           #da li je deljenje nulom
    jne deli
    cmpl $0, b+4
    je deljnula
deli:
    cmpl b+4, %ebx       #a ? b
    ja deli2
    jl kraj
    cmpl b, %eax
    jl kraj
deli2:
    subl b, %eax        # a -= b
    sbbl b+4, %ebx
    addl $1, k          # k += 1
    adcl $0, k+4
    jmp deli
deljnula:
    incb greska
kraj:
    movl %eax, o        # upiši ostatak
    movl %ebx, o+4
    movl $1, %eax
    movl $0, %ebx
    int $0x80

