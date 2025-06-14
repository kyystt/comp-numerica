#define _POSIX_C_SOURCE 2
#define MAX_FACTORIAL 100

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

static int lookup[MAX_FACTORIAL] = {0};
int factorial(int x)
{
    if (x == 0 || x == 1) {
        lookup[x] = 1;
    }

    if (lookup[x] == 0) {
        int fact = x * factorial(x-1);
        lookup[x] = fact;
    }

    return lookup[x];
}

void printUsage(const char *filename)
{
    printf("Usage: %s [-r <number of iterations>]\n", filename);
    printf("\t-r <number of iterations>: set the number of iterations that you want to use in taylor's expansion\n");
}

double minus_sin(double x)
{
    return -1 * sin(x);
}

double minus_cos(double x)
{
    return -1 * cos(x);
}

double (*derivative_cos[])(double) = {cos, minus_sin, minus_cos, sin};
double (*derivative_sin[])(double) = {sin, cos, minus_sin, minus_cos};
double (*derivative_exp[])(double) = {exp, exp, exp, exp};


void taylor(double (*e[])(double), double value, int num_iter)
{
    double res = 0;
    for (int i = 0; i < num_iter; ++i)
    {
        res += ((e[i%4](0) * pow(value, i))/factorial(i));
    }

    fprintf(stdout, "%s %.30lf\n", "The result is (rounded up to 30 decimal places): ", res);
}

void run(int num_iter)
{
    enum AcceptableFunctions{
        COS = 1,
        SIN = 2,
        EXP = 3
    };

    fprintf(stdout, "Select an option: \n1.\tcos(x)\n2.\tsin(x)\n3.\texp(x)\n");
    int func;
    scanf("%d", &func);
    
    fprintf(stdout, "%s\n", "Do you want to approximate to what value?");
    double value;
    scanf("%lf", &value);
    switch (func)
    {
    case COS:
        taylor(derivative_cos, value, num_iter);
        break;
    case SIN:
        taylor(derivative_sin, value, num_iter);
        break;
    case EXP:
        taylor(derivative_exp, value, num_iter);
        break;

    default:
        fprintf(stderr, "%s\n", "available functions: cos, sin, exp");
        exit(1);
    }
}

int main(int argc, char** argv)
{
    int opt;
    int num_iter;
    const char* program_name = argv[0];
    
    if (argc < 3)
    {
        printUsage(program_name);
        exit(1);
    }

    while((opt = getopt(argc, argv, "r:")) != 1)
    {
        switch(opt)
        {
            case 'r':
                num_iter = atoi(optarg);
                run(num_iter);
                break;
            
            default:
                printUsage(program_name);
                break;
        }
        break;
    }

    return 0;
}