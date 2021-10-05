# Potprogram za konverziju iz označenog oktalnog stringa u vrednost
# Imenko Prezimić ra1234

# unsigned int oct_str_to_inter(char* str, unsigned int* greska)
.section .text
.globl oct_str_to_inter
oct_str_to_inter:
    pushl %ebp
    movl %esp, %ebp
    subl $4, %esp
    pushl %ebx
    pushl %edi
    movl $8, -4(%ebp)   #baza
    movl $0, %edi       #greška
    xorl %eax, %eax
    xorl %ecx, %ecx
    movl 8(%ebp), %ebx
    cmpb $0, (%ebx)     #prazan string?
    je o2i_greska1
o2i_cifra:
    movb (%ebx), %cl
    andb %cl, %cl
    jz o2i_kraj
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

