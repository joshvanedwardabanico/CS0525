#include <stdio.h>

int main() {

    float a; //primo numero float
    float b; //secondo numero float
    float media; //la media tra i due numeri float

    printf("Inserisci il primo numero: ");
    scanf("%f",&a);

    printf("Inserisci il secondo numero: ");
    scanf("%f",&b);

    media = (a+b) / 2;

    printf("La media aritmetica è: %.1f", media);

    return 0;
}
