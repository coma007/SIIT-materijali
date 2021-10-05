#autor: Milica
#int encode(char* izvorni, char* ciljni, char* enkodovati);

.section .data

.section .text
.global encode

encode:

	pushl %ebp
	movl %esp, %ebp
	subl $4, %esp

	pushl %ebx
	pushl %esi
	pushl %edi

	movl 8(%ebp), %eax
	movl 12(%ebp), %ebx
	movl 16(%ebp), %ecx

	xorl %esi, %esi
	movl %esi, -4(%ebp)

enkod:

	xorl %edi, %edi

	movb (%eax,%esi,1), %dh
	movb (%ebx,%esi,1), %dl

akcija:

	cmpb (%ecx,%edi,1), %dh
	jne dalje

	movb %dl, (%ecx,%edi,1)
	incl -4(%ebp)

dalje:

	incl %edi
	cmpb $0, (%ecx,%edi,1)
	jne akcija

	incl %esi
	cmpb $0, (%ebx,%esi,1)
	jne enkod


kraj:

	movl -4(%ebp), %eax

	popl %edi
	popl %esi
	popl %ebx

	movl %ebp, %esp

	popl %ebp

	ret
