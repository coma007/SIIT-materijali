# Potprogram za iterativno računanje fibonačijevih brojeva
# Imenko Prezimić ra1234

.section .text
.globl fibonaci
#int fibonaci(int n)
fibonaci:
    pushl %ebp
    movl %esp, %ebp

    movl $1, %eax   #f1
    movl %eax, %ecx #f2
fib_petlja:
    cmpl $2, 8(%ebp)
    jbe fib_kraj
    addl %eax, %ecx
    xchgl %eax, %ecx
    decl 8(%ebp)
    jmp fib_petlja

fib_kraj:
    movl %ebp, %esp
    popl %ebp
    ret

# Za vežbu, dopuniti potprogram još jednim parametrom:
# int fibonaci(int n, int *g)
# u kome će se nalaziti 0 ako je računanje prošlo kako treba,
# odnosno 1 ako je došlo do greške (prekoračenja)
