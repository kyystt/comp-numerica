#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define err 10e(-5)

typedef struct t_polinomio {
    int grau;
    int cap;
    double *coef;
} polinomio;

double eval_pol(polinomio *p, double val)
{
    double res = 0;
    for(int i = 0; i < p->grau; ++i)
    {
        res += pow(val, i) * (*(p->coef + p->grau - i - 1));
    }

    return res;
}

int main(int argc, char** argv)
{
    polinomio p = {0};
    int grau = 0;
    char buffer[4096] = {0};

    while(fgets(buffer, 100, stdin) && strcmp(buffer, "\n") != 0)
    {
        char *trash = NULL;
        double coef = strtod(buffer, &trash);
        if (p.cap == p.grau) {
            if (p.cap == 0) {
                p.cap = 10;
                p.coef = (double *) malloc(sizeof(double) * p.cap);
            } else {
                p.cap *= 2;
                p.coef = (double *) realloc(p.coef, sizeof(p.cap));
            }
        }

        *(p.coef + grau) = coef;
        grau++;

        memset(buffer, 0, sizeof(buffer));
    }

    p.grau = grau;

    printf("Digite o intervalo [a, b] que deseja procurar a raiz: \n");
    double a, b;
    scanf("%lf %lf", &a, &b);

    if (eval_pol(&p, a) * eval_pol(&p, b) > 0)
    {
        fprintf(stdout, "%s\n", "nao tem raizes nesse intervalo");
        exit(0);
    } 
    else if (eval_pol(&p, a) * eval_pol(&p, b) == 0)
    {
        fprintf(stdout, "%s\n", "achamos uma raiz!");
        if (eval_pol(&p, a) == 0) 
        {
            fprintf(stdout, "%s %lf\n", "a raiz eh: ", a);
        }
        else 
        {
            fprintf(stdout, "%s %lf\n", "a raiz eh: ", b);
        }
        exit(0);
    }
    
    return 0;
}