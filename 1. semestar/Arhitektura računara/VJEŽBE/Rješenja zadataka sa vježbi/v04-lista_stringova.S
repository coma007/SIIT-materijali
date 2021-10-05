# Obrnuti ispis niza stringova
# Imenko Prezimić ra1234

.section .data
str_len = 20    # dužina jednog stringa
str_num = 10    # broj stringova
strings:  .fill str_len*str_num,1,42    # prostor za sve stringove
currentn: .long 0                       # indeks tekućeg stringa
currents: .long 0                       # adresa tekućeg stringa
str_lens: .fill str_num,4,0             # dužina za svaki string
str_unos: .ascii "Unesite string:\0"
str_unos_len = . - str_unos
str_ispis: .ascii "\nObrnuti redosled:\n\0"
str_ispis_len = . - str_ispis

.section .text
.globl main
main:
    # unos stringova
    movl $0, currentn
    movl $strings, %eax
    movl %eax, currents
petlja1:
    movl $4, %eax       # ispis poruke
    movl $1, %ebx
    movl $str_unos, %ecx
    movl $str_unos_len, %edx
    int $0x80
    movl $3, %eax       # unos stringa
    movl $0, %ebx
    movl currents, %ecx
    movl $str_len, %edx
    int $0x80
    movl currentn, %esi
    movl %eax,str_lens(,%esi,4) # čuvanje dužine stringa
    addl $str_len, currents     # adresa sledećeg stringa
    incl currentn
    cmpl $str_num, currentn     # da li su svi uneti?
    jl petlja1

    #ispis stringova
    movl $4, %eax       # ispis poruke
    movl $1, %ebx
    movl $str_ispis, %ecx
    movl $str_ispis_len, %edx
    int $0x80
    decl currentn
    subl $str_len, currents # adresa poslednjeg stringa
petlja2:
    movl $4, %eax           # ispis stringa
    movl $1, %ebx
    movl currents, %ecx     # adresa tekućeg stringa
    movl currentn, %edx     # dužina tekućeg stringa
    movl str_lens(,%edx,4), %edx
    int $0x80   # zgodno je što je \n deo stringa, pa će ispis biti u posebnim redovima
    subl $str_len, currents # adresa prethodnog stringa
    decl currentn
    jns petlja2
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
