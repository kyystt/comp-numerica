# Vamos usar isso pra calcular uma raiz quadrada 
# a raiz de k eh raiz da equacao y = x^2 - k, derivando temos:
# y' = 2x; e a nossa iteracao vai ser x_{n+1} = x_n - y(x_n)/y'(x_n)
# ou seja, x_{n+1} = x_n - (x_n^2-k)/2x_n
from math import sqrt

tol = 1e-9

def main():
    k = int(input("Digite a raiz para aproximarmos: "))
    x_n = k/2.0
    x = 0

    while True:
        x = x_n - (pow(x_n, 2) - k)/(2*x_n)

        if abs(x-x_n) < tol:
            break
        
        x_n = x


    print(f"Raiz aproximada: {x}\n\rRaiz da biblioteca math: {sqrt(k)}\n\rErro absoluto: {x - sqrt(k)}")

main()