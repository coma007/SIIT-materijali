# Upcase stringa, indirektno adresiranje
# Imenko Prezimić ra1234

.section .data
poruka1: .ascii "Unesite ime i prezime: \0"
por1_len = . - poruka1
poruka2: .ascii "Vi ste: \0"
por2_len = . - poruka2
imemax = 50
ime: .fill imemax,1,42

.section .text
.globl main
main:
    movl $4, %eax
    movl $1, %ebx
    movl $poruka1, %ecx
    movl $por1_len, %edx
    int $0x80

    movl $3, %eax
    movl $0, %ebx
    movl $ime, %ecx
    movl $imemax, %edx
    int $0x80
    movl %eax, %esi       # dužina unetog stringa

    movl $ime,%eax
upcase:
    cmpb $'a', (%eax)     # provera da li je malo slovo
    jb dalje
    cmpb $'z', (%eax)
    ja dalje
    addb $'A'-'a', (%eax) # ako jeste malo slovo, UPCASE
    # 'A'-'a' je razlika između ASCII kodova za veliko i malo A
dalje:
    incl %eax
    cmpb $10, (%eax)      # kod read poziva, string se završava sa 10
    jne upcase

    movl $4, %eax
    movl $1, %ebx
    leal poruka2, %ecx
    movl $por2_len, %edx
    int $0x80

    movl $4, %eax
    movl $1, %ebx
    movl $ime, %ecx
    movl %esi, %edx       # zapamćena dužina
    int $0x80

kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

