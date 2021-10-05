# Potprogram za konverziju iz označenog oktalnog stringa u vrednost
# Imenko Prezimić ra1234

# unsigned int oct_str_float_to_inter(char* str, unsigned int* greska);
.section .text
.globl oct_str_float_to_inter
oct_str_float_to_inter:
    pushl %ebp
    movl %esp, %ebp
    subl $8, %esp
    pushl %ebx
    pushl %edi
    movl $8, -4(%ebp)   #baza
    movl $100000000, -8(%ebp)   #skaliranje
    movl $0, %edi       #greška
    xorl %ecx, %ecx
    movl 8(%ebp), %ebx
    cmpb $0, (%ebx)     #prazan string?
    je o2i_greska
o2i_null:
    cmpb $0, 1(%ebx)     #nađi kraj stringa
    je o2i_cifra
    incl %ebx
    jmp o2i_null
o2i_cifra:
    xorl %eax, %eax
    movb (%ebx), %al
    cmpb $'.', %al
    je o2i_kraj
    subb $'0', %al
    js o2i_greska
    cmpl -4(%ebp), %eax
    jae o2i_greska
    mull -8(%ebp)
    addl %ecx, %eax
    divl -4(%ebp)
    movl %eax, %ecx
    decl %ebx
    jmp o2i_cifra
o2i_greska:
    incl %edi
o2i_kraj:
    movl 12(%ebp), %ebx
    movl %edi, (%ebx)
    movl %ecx, %eax
    popl %edi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret

