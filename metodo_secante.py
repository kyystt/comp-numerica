# A ideia eh quase a mesma do metodo de newton, mas agora utilizando secantes ao inves da reta tangente
# o problema eh que precisamos de dois pontos iniciais x_0 e x_1

from math import sqrt

def f(x, k):
    return x ** 2 - k

def secante(value, x_0, x_1, tol = 1e-9):
    if (x_0 == x_1):
        x_1 += 1

    x = 0
    while True:
        f_x0 = f(x_0, value)
        f_x1 = f(x_1, value)

        if f_x0 - f_x1 == 0:
            print("Divisao por zero")
            break

        x = (x_0 * f_x1 - x_1 * f_x0)/(f_x1 - f_x0)

        if abs(x - x_1) < tol:
            break
        
        x_0 = x_1
        x_1 = x

    return x

def main():
    # k = int(input("Digite a raiz para aproximarmos: "))
    values_err = []

    for k in range(1, 101):
        x_n0 = k / 2.0
        x_n1 = k * 1.0
        aprox = secante(k, x_n0, x_n1)
        print(f"Loop #{k}, aprox: {aprox}")
        values_err.append(abs(aprox - sqrt(k))/sqrt(k))

    media_erro = sum(values_err) / len(values_err)
    
    print(f"A media do erro relativo do metodo da secante foi: {media_erro:e}")
    print(f"A media do erro relativo percentual do metodo da secante foi: {media_erro*100:.15f}%")


main()