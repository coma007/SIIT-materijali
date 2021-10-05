#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int kodiraj(unsigned int vrednost);

void printbin(unsigned int x) {
    unsigned int m=0x80000000, s=0;
    while(m) {
        printf("%s%s",m&x ? "1" : "0",++s%8 ? "" : " ");
        m >>= 1;
    }
    printf("\n");
}

int main() {
    unsigned int v, r;
    printf("Vrednost (hex): ");
    scanf("%x",&v);
    printf("Binarno:  ");
    printbin(v);
    
    r = kodiraj(v);
    printf("Rezultat: ");
    printbin(r);
    printf("\n");
    
    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    
    return 0;
}

