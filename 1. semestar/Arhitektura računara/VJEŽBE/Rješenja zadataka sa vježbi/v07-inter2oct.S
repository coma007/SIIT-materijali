# Potprogram za konverziju u označeni oktalni string
# Imenko Prezimić ra1234

# unsigned int inter_to_oct_str(int broj, char* str, unsigned int duzina)
.section .text
.globl inter_to_oct_str
inter_to_oct_str:
    pushl %ebp
    movl %esp, %ebp
    subl $4, %esp
    pushl %ebx
    pushl %esi
    pushl %edi
    movl 8(%ebp), %eax      #broj
    movl 12(%ebp), %edi     #str
    movl $8, %ebx           #baza
    movl $0, -4(%ebp)       #greška
    andl %eax, %eax         #da li je broj negativan?
    jns i2o_cifra
    movb $'-', (%edi)       #ako jeste, ubaci minus
    incl %edi
    incl 12(%ebp)           #pomeri pokazivač, da se ne bi obrtao minus
    decl 16(%ebp)           #smanji broj slobodnih mesta
    negl %eax               #komplement 2
i2o_cifra:
    decl 16(%ebp)           #provera preostalog mesta
    cmpl $1, 16(%ebp)       #neophodan je i 1 bajt za NULL
    jl i2o_greska
    xorl %edx, %edx
    divl %ebx
    addb $'0', %dl
    movb %dl, (%edi)
    incl %edi
    andl %eax, %eax
    jnz i2o_cifra
    movb $0, (%edi)
    decl %edi
    movl 12(%ebp), %esi
i2o_obrni:
    cmpl %edi, %esi
    jae i2o_kraj
    movb (%esi), %ah
    movb (%edi), %al
    movb %al, (%esi)
    movb %ah, (%edi)
    decl %edi
    incl %esi
    jmp i2o_obrni
i2o_greska:
    incl -4(%ebp)
i2o_kraj:
    movl -4(%ebp), %eax
    popl %edi
    popl %esi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret

#Izbacivanjem linija 18-24 se dobija neoznačena varijanta potprograma.
