#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

int encode(char* izvorni, char* ciljni, char* enkodovati);

int main() {
    int r,g=0;
    char izvorni[50]={0}, ciljni[50]={0}, enkodovati[50]={0}, buffer[50]={0};

    printf("Unesite izvorne znakove: ");
    fgets(buffer,50,stdin);
    sscanf(buffer,"%[^\n]s",izvorni);

    printf("Unesite ciljne znakove: ");
    fgets(buffer,50,stdin);
    sscanf(buffer,"%[^\n]s",ciljni);

	printf("Unesite string za enkodovanje: ");
    fgets(buffer,50,stdin);
    sscanf(buffer,"%[^\n]s",enkodovati);

    r = encode(izvorni, ciljni, enkodovati);
    printf("\nString nakod enkodovanja : %s",enkodovati);
    printf("\nPovratna vrednost: %d\n",r);

    #ifdef LEVEL42
    printf("\nRUNPP_REG_ERR:%d\n",RUNPP_REG_ERR);
    #endif
    return g;
}

