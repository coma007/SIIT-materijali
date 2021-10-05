# Potprogram za konverziju iz označenog oktalnog stringa u vrednost
# Imenko Prezimić ra1234

# int oct_str_to_inter(char* str, unsigned int* greska)
.section .text
.globl oct_str_to_inter
oct_str_to_inter:
    pushl %ebp
    movl %esp, %ebp
    subl $8, %esp
    pushl %ebx
    pushl %edi
    movl $8, -4(%ebp)   #baza
    movl $1, -8(%ebp)   #negacija
    movl $0, %edi       #greška
    xorl %eax, %eax
    xorl %ecx, %ecx
    movl 8(%ebp), %ebx
    cmpb $0, (%ebx)     #prazan string?
    je o2i_greska1
    cmpb $'+', (%ebx)   #predznak?
    je o2i_znak1
    cmpb $'-', (%ebx)   #predznak?
    jne o2i_cifra
    negl -8(%ebp)
o2i_znak1:
    incl %ebx           #preskoči predznak
o2i_cifra:
    movb (%ebx), %cl
    andb %cl, %cl
    jz o2i_znak2
    subb $'0', %cl
    js o2i_greska1
    cmpl -4(%ebp), %ecx
    jae o2i_greska1
    mull -4(%ebp)
    jc o2i_greska2
    addl %ecx, %eax
    jc o2i_greska2
    incl %ebx
    jmp o2i_cifra
o2i_znak2:
    andl %eax, %eax
    js o2i_greska2  #ako je neoznačeni broj veći od 0x7fffffff
    imull -8(%ebp)
    jmp o2i_kraj
o2i_greska2:
    incl %edi
o2i_greska1:
    incl %edi
o2i_kraj:
    movl 12(%ebp), %ebx
    movl %edi, (%ebx)
    popl %edi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret

# potprogram ne radi dobro za jednu vrednost. koju?
