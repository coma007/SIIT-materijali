# Potprogram za postavljanje pariteta 16-bitnog broja
# Imenko Prezimić ra1234

#int SetParity(unsigned short int* v)
.section .text
.globl SetParity
SetParity:
    pushl %ebp
    movl %esp, %ebp
    movl 8(%ebp), %ecx
    andw $0x7fff, (%ecx)#postavljanje najvišeg bita na 0 (on se 
                        #ne posmatra prilikom određivanja pariteta)
    movw $1, %dx        #inicijalna maska
    xorl %eax, %eax     #brojač bita
parity_petlja:
    testw %dx, (%ecx)
    jz parity_dalje
    incl %eax
parity_dalje:
    shlw $1, %dx        #sledeća bit pozicija
    jnc parity_petlja
    andl $1, %eax
    pushl %eax
    shlw $1, (%ecx)     #postavljanje najnižeg bita
    shrl $1, %eax       #registra eax (brojač bita)
    rcrw $1, (%ecx)     #u najviši bit 16-bitne promenljive
    popl %eax
parity_kraj:
    movl %ebp, %esp
    popl %ebp
    ret

