# Potprogram za konverziju u označeni oktalni string za razlomljene brojeve
# Imenko Prezimić ra1234

# unsigned int inter_to_oct_str_float(int broj, char* str, unsigned int duzina)
.section .text
.globl inter_to_oct_str_float
inter_to_oct_str_float:
    pushl %ebp
    movl %esp, %ebp
    subl $8, %esp
    pushl %ebx
    pushl %esi
    pushl %edi
    movl 8(%ebp), %eax      #broj
    movl 12(%ebp), %edi     #str
    movl $8, %ebx           #baza
    movl $0, -4(%ebp)       #greška
    movl $100000000, -8(%ebp)   #konstanta skaliranja
    andl %eax, %eax         #da li je broj negativan?
    jns i2o_nula
    movb $'-', (%edi)       #ako jeste, ubaci minus
    incl %edi
    decl 16(%ebp)           #smanji broj slobodnih mesta
    negl %eax               #komplement 2
i2o_nula:
    cmpl $4, 16(%ebp)       #greška je samo ako inicijalno nema
    jl i2o_greska           #dovoljno mesta za "0." i jednu cifru
    movb $'0', (%edi)
    movb $'.', 1(%edi)
    addl $2, %edi
    decl 16(%ebp)
i2o_cifra:
    decl 16(%ebp)           #provera preostalog mesta
    cmpl $1, 16(%ebp)       #neophodan je i 1 bajt za NULL
    je i2o_term
    mull %ebx               #množenje bazom
    divl -8(%ebp)           #deljenje konstantom skaliranja
    addb $'0', %al
    movb %al, (%edi)
    incl %edi
    movl %edx, %eax
    andl %eax, %eax
    jnz i2o_cifra
i2o_term:
    movb $0, (%edi)
    jmp i2o_kraj
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

#Izbacivanjem linija 19-24 se dobija neoznačena varijanta potprograma.
