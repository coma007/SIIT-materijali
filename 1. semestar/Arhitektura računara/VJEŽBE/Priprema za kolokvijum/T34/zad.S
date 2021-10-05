# Milica Sladakovic Sv 18/2020
# void spoji_stringove(char* str, char* drugi, char* rez, int n);

.section .text

.globl spoji_stringove

spoji_stringove:

	pushl %ebp
    movl %esp, %ebp  

	pushl %eax
	pushl %esi
	pushl %edi

	movl 8(%ebp), %ecx # str
	movl 16(%ebp), %eax # rez

kraj_reci:

	cmpb $0, (%ecx)
	je kraj

	movl 12(%ebp), %ebx # drugi

	xorl %esi, %esi

dodji_do_n:

	cmpl 20(%ebp), %esi # poredi n
	je premjesti

	xorl %edx, %edx
	movb (%ecx), %dl
	movb %dl, (%eax)

	incl %esi
	incl %ecx
	incl %eax

	jmp dodji_do_n

premjesti:

	xorl %edx, %edx
	movb (%ebx), %dl
	movb %dl, (%eax)

	incl %eax	
	incl %ebx
	cmpb $0, (%ebx)
	je kraj_reci

	jmp premjesti

kraj:

    movl %ebp, %esp     # brisi sve lokalne promjenljive
	
	popl %edi
	popl %esi
	popl %eax

	movl %ebp, %esp
	popl %ebp

    ret
