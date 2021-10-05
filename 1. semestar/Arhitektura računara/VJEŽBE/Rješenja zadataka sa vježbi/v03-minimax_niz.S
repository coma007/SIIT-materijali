# Nalaženje minimuma i maksimuma niza
# Imenko Prezimić ra1234

.section .data
NELEM = 10
niz: .long 1,2,3,4,5,6,7,8,9,10
min: .long 0    #ecx za privremeno čuvanje min
max: .long 3    #edx za privremeno čuvanje max

.section .text
.globl main
main:
    movl $niz, %esi     #inicijalna vrednost
    movl (%esi) ,%ecx
    movl niz ,%edx      #može i ovako
petlja:
    cmpl (%esi), %ecx   #min
    jle dalje
    movl (%esi), %ecx
dalje:
    cmpl (%esi), %edx   #max
    jge dalje2
    movl (%esi), %edx
dalje2:
    addl $4, %esi
    cmpl $niz+NELEM*4, %esi
    jl petlja
kraj:
    movl %ecx, min
    movl %edx, max
    movl $1, %eax
    movl $0, %ebx
    int $0x80

