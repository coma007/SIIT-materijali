# Potprogram za generisanje 32-bitne maske
# Imenko Prezimić ra1234

#unsigned int maska(unsigned int n, unsigned int v)
.section .text
.globl maska
maska:
    pushl %ebp
    movl %esp, %ebp
    movl 8(%ebp), %ecx
    #ako je broj veći od 31 (ili negativan), imaće
    #bar jednu jedinicu na bit pozicijama većim od 4
    #(ovako se može porediti samo zato što je 31=0b11111)
    testl $0b11111111111111111111111111100000, %ecx
    jnz maska_gr
    movl $1, %eax   #inicijalna maska
    shll %cl, %eax  #pomeranje maske za n pozicija
    #sličan princip provere opsega kao za n
    testl $0b11111111111111111111111111111110, 12(%ebp)
    jnz maska_gr
    testl $1, 12(%ebp)  #provera da li je v 0 ili 1
    jnz maska_kraj
    notl %eax           #ako je 0, invertuj bite u rezultatu
    jmp maska_kraj
maska_gr:
    xorl %eax, %eax
maska_kraj:
    movl %ebp, %esp
    popl %ebp
    ret

# Za vežbu se preporučuje realizacija provere opsega
# poređenjem sa donjom i gornjom granicom
