# Potprogram za iterativno računanje fibonačijevih brojeva
# Povratna vrednost potprograma je greška (0 - nema greške)
# Imenko Prezimić ra1234

.section .text
.globl fibonaci
#int fibonaci(int n, int* rez)
fibonaci:
    pushl %ebp
    movl %esp, %ebp
    subl $4, %esp       #lokalna promenljiva za grešku
    movl $0, -4(%ebp)   #postavljamo grešku na 0

    movl $1, %eax   #f1
    movl %eax, %ecx #f2
fib_petlja:
    cmpl $2, 8(%ebp)
    jbe fib_kraj
    addl %eax, %ecx
    jc fib_greska
    xchgl %eax, %ecx
    decl 8(%ebp)
    jmp fib_petlja
fib_greska:
    incl -4(%ebp)
fib_kraj:
    movl 12(%ebp), %ecx #adresa rezultata
    movl %eax, (%ecx)   #upis rezultata
    movl -4(%ebp), %eax #greška je povratna vrednost
    movl %ebp, %esp
    popl %ebp
    ret

