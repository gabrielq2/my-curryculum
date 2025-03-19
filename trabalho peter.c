#include<stdio.h>

int main() {
    int a, v;
    int tabela1[128], tabela2[128], tabela3[128], tabela4[128];
    int tabela5[128], tabela6[128], tabela7[128];
    int resultados[128];

    printf("Insira a quantidade de variáveis (até 7)= ");
    scanf("%d", &v);

    if (v < 1 || v > 7) {
        printf("Quantidade de variáveis inválida. Por favor, insira um valor entre 1 e 7.\n");
        return 1;
    }

    for (a = 0; a < (1 << v); a++) {
        tabela1[a] = a % 2;
        tabela2[a] = (a / 2) % 2;
        tabela3[a] = (a / 4) % 2;
        tabela4[a] = (a / 8) % 2;
        tabela5[a] = (a / 16) % 2;
        tabela6[a] = (a / 32) % 2;
        tabela7[a] = (a / 64) % 2;
    }

    for (int n = 0; n < (1 << v); n++) {
        do {
            int n1;
            printf("Insira qual o valor desejado (0 ou 1) para a linha %d= ", n);
            scanf("%d", &n1);
            resultados[n] = n1;
            if (resultados[n] != 0 && resultados[n] != 1) {
                printf("O valor precisa ser estritamente 0 ou 1.\n");
            }
        } while (resultados[n] != 0 && resultados[n] != 1);
    }
    printf("\n");
    printf("Índice |");
    for (int i = 0; i < v; i++) {
        printf(" %c |", 'A' + i);
    }
    printf(" Y\n");

    printf("--------");
    for (int i = 0; i < v; i++) {
        printf("-----");
    }
    printf("----\n");
    
    for (a = 0; a < (1 << v); a++) {
        printf("%6d |", a);
        if (v >= 1) printf(" %d |", tabela1[a]);
        if (v >= 2) printf(" %d |", tabela2[a]);
        if (v >= 3) printf(" %d |", tabela3[a]);
        if (v >= 4) printf(" %d |", tabela4[a]);
        if (v >= 5) printf(" %d |", tabela5[a]);
        if (v >= 6) printf(" %d |", tabela6[a]);
        if (v >= 7) printf(" %d |", tabela7[a]);
        printf(" %d\n", resultados[a]);
    }
    printf("\n");

    char pergunta;
    do {
        printf("Gostaria de ver mintermo ou maxtermo (y ou n)= ");
        scanf(" %c", &pergunta); 
        
        if (pergunta == 'y') {
            int resp;
            printf("Gostaria de ver mintermo, maxtermo ou os dois (1 mintermo, 2 maxtermo, 3 ambos)= ");
            scanf("%d", &resp);
            if(resp == 3){
                pergunta = 'n';
            }

            if (resp == 1 || resp == 3) {
                printf("Mintermos= ");
                for (a = 0; a < (1 << v); a++) {
                    if (resultados[a] == 1) {
                        printf("\nM%d = ", a);
                        for (int i = 0; i < v; i++) {
                            if ((a & (1 << i)) != 0) {
                                printf("%c.", 'A' + i);
                            } else {
                                printf("~%c.", 'A' + i);
                            }
                        }
                        printf("\b "); 
                    }
                }
            }

            if (resp == 2 || resp == 3) {
                printf("\nMaxtermos=\n");
                for (a = 0; a < (1 << v); a++) {
                    if (resultados[a] == 0) {
                        printf("M%d: (", a);
                        for (int i = 0; i < v; i++) {
                            if ((a & (1 << i)) == 0) {
                                printf("%c+", 'A' + i);
                            } else {
                                printf("~%c+", 'A' + i);
                            }
                        }
                        printf("\b)\n"); 
                    }
                }
            }

            if (resp < 1 || resp > 3) {
                printf("Número inválido.\n");
            }
        }
        
    } while (pergunta != 'n' );

    return 0;
}
