#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int SaberiMnozi(int n, unsigned short *a, unsigned short *b, unsigned short *resenje);

int main() {
    int i, n, r;
    unsigned short a[50], b[50], resenje[50];

    printf("Broj elemenata: ");
    scanf("%d",&n);

    for (i=0; i<n; i++) {
        printf("Vrednost a[%02d]: ",i);
        scanf("%hu",&a[i]);
    }
    for (i=0; i<n; i++) {
        printf("Vrednost b[%02d]: ",i);
        scanf("%hu",&b[i]);
    }

    printf("\nIzlaz:\n");
    r = SaberiMnozi(n,a,b,resenje);
    for (i=0;i<n;i++) {
        printf("resenje[%d] = %hu\n",i,resenje[i]);
    }
    printf("Povratna vrednost: %d\n",r);

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return 0;
}

