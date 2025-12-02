#include <stdio.h>

int main() {
    int a; // primo numero
    int b; // secondo numero
    int mul; // il prodotto tra i due numeri

    printf("Inserisci il primo numero: ");
    scanf("%d",&a);

    printf("Inserisci il secondo numero: ");
    scanf("%d",&b);

    mul = a*b;

    printf("Il prodotto è: %d", mul);

    return 0;
    
}
