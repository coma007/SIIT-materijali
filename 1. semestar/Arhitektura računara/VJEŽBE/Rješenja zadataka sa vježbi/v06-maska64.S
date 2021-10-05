# Potprogram za generisanje 64-bitne maske
# Imenko Prezimić ra1234

#unsigned long long maska64(unsigned int n, unsigned int v)
.section .text
.globl maska64
maska64:
    pushl %ebp
    movl %esp, %ebp
    movl 8(%ebp), %ecx
    xorl %edx, %edx     #viši deo maske
    #ako je broj veći od 63 (ili negativan), imaće
    #bar jednu jedinicu na bit pozicijama većim od 5
    #(ovako se može porediti samo zato što je 63=0b111111)
    testl $0b11111111111111111111111111000000, %ecx
    jnz maska_gr
    movl $1, %eax   #inicijalna maska
    #pomeramo samo niži deo maske za (n mod 32) mesta
    andl $0b11111, %ecx #ovo bi bio ostatak kad bi se ecx podelio sa 32
    shll %cl, %eax  #pomeranje nižeg dela maske
    #sličan princip provere opsega kao za n
    testl $0b11111111111111111111111111111110, 12(%ebp)
    jnz maska_gr
    testl $1, 12(%ebp)  #provera da li je v 0 ili 1
    jnz maska_kraj
    notl %eax           #ako je 0, invertuj bite u rezultatu
    notl %edx
    jmp maska_kraj
maska_kraj:
    testl $0b100000, 8(%ebp)   #da li je n bilo veće od 31?
    jz maska_kraj2
    xchgl %eax, %edx           #ako jeste, zameni viši i niži deo
    jmp maska_kraj2
maska_gr:
    xorl %eax, %eax
maska_kraj2:
    movl %ebp, %esp
    popl %ebp
    ret

# Za vežbu se preporučuje realizacija ovog potprograma korišćenjem
# rotiranja, odnosno pomeranja u dvostrukoj preciznosti
