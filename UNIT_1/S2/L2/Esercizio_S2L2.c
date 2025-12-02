#include <stdio.h>
int main()
{
    int primo_numero;
    int secondo_numero;
    int moltiplicazione;
    float media;
    printf("Inserire primo numero: ");
    scanf("%d", &primo_numero);
    printf("Inserire secondo numero: ");
    scanf("%d", &secondo_numero);
    moltiplicazione=primo_numero*secondo_numero;
    printf("La moltiplicazione di questi numeri è: %d\n", moltiplicazione);
    media=(primo_numero+secondo_numero)/2.0;
    printf("La media di questi numeri è: %f", media);
    return 0;
}