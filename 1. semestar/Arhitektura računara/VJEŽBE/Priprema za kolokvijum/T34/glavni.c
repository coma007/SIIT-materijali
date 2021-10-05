#include <stdio.h>

unsigned int RUNPP_REG_ERR = 0;

void spoji_stringove(char* str, char* drugi, char* rez, int n);

int main() {

    char s[21],s1[3];
	char rez[50] = { };
	int n = 0;

    printf("Unesite string: ");
    scanf("%s",s);

    printf("Unesite drugi string: ");
    scanf("%s",s1);

    printf("Unesite n: ");
    scanf("%d",&n);

    spoji_stringove(s,s1,rez,n);


    printf("String: %s\n",rez);

	return 0;
}

