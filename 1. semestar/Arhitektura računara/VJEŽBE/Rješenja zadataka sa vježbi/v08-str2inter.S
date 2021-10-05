# Potprogram za konverziju iz označenog stringa u vrednost
# Imenko Prezimić ra1234

#int str_to_inter(char* str, unsigned int* greska, unsigned int baza)
.section .text
.globl str_to_inter
str_to_inter:
    pushl %ebp
    movl %esp, %ebp
    subl $4, %esp
    pushl %ebx
    pushl %edi
    movl $1, -4(%ebp)   #negacija
    movl $0, %edi       #greška
    cmpl $2, 16(%ebp)   #provera validnosti baze
    jl s2i_greska3
    cmpl $36, 16(%ebp)
    jg s2i_greska3
    xorl %eax, %eax
    xorl %ecx, %ecx
    movl 8(%ebp), %ebx
    cmpb $0, (%ebx)     #prazan string?
    je s2i_greska2
    cmpb $'+', (%ebx)   #predznak?
    je s2i_znak1
    cmpb $'-', (%ebx)   #predznak?
    jne s2i_cifra
    negl -4(%ebp)
s2i_znak1:
    incl %ebx           #preskoči predznak
s2i_cifra:
    movb (%ebx), %cl
    andb %cl, %cl
    jz s2i_znak2
    subb $'0', %cl
    js s2i_greska2      #znak manji od '0'?
    cmpb $10, %cl       #cifra '0'-'9'?
    jl s2i_cifra2
    subb $'A'-'9'-1, %cl
    js s2i_greska2      #znak između '9' i 'A'?
    cmpb $36, %cl       #cifra 'A'-'Z'?
    jl s2i_cifra2
    subb $'a'-'A', %cl  #cifra 'a'-'z'?
    js s2i_greska2      #znak između 'Z' i 'a'?
s2i_cifra2:
    cmpl 16(%ebp), %ecx
    jae s2i_greska2     #cifra >= baza?
    mull 16(%ebp)
    jc s2i_greska1
    addl %ecx, %eax
    jc s2i_greska1
    incl %ebx
    jmp s2i_cifra
s2i_znak2:
    andl %eax, %eax
    js s2i_greska1  #ako je neoznačeni broj veći od 0x7fffffff
    imull -4(%ebp)
    jmp s2i_kraj
s2i_greska3:
    incl %edi
s2i_greska2:
    incl %edi
s2i_greska1:
    incl %edi
s2i_kraj:
    movl 12(%ebp), %ebx
    movl %edi, (%ebx)
    popl %edi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret

# potprogram ne radi dobro za jednu vrednost u svakoj bazi. koju?
