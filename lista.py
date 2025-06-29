import numpy as np

def false_position(func, lower_bound, upper_bound, tol = 1e-7, max_iter = 100):
    f_lower = func(lower_bound)
    f_upper = func(upper_bound)

    num_iteracoes = 0

    if f_lower * f_upper > 0:
        return None

    for _ in range(max_iter):
        mid = (lower_bound * f_upper - upper_bound * f_lower) / (f_upper - f_lower)

        f_mid = func(mid)

        if abs(f_mid) < tol:
            return mid, num_iteracoes, func(mid)

        if f_lower * f_mid < 0:
            upper_bound = mid
            f_upper = f_mid
        else:
            lower_bound = mid
            f_lower = f_mid

        num_iteracoes += 1

    return (lower_bound * f_upper - upper_bound * f_lower) / (f_upper - f_lower), num_iteracoes, func((lower_bound * f_upper - upper_bound * f_lower) / (f_upper - f_lower))

def bisseccao(func, lower_bound, upper_bound, tol = 1e-7, max_iter = 100):
    num_interacoes = 0

    f_lower = func(lower_bound)
    f_upper = func(upper_bound)

    if f_lower * f_upper > 0:
            return None

    for _ in range(max_iter):
        mid = (upper_bound + lower_bound) / 2

        f_mid = func(mid)

        if func(mid) == 0 or (upper_bound - lower_bound) / 2< tol:
            return mid, num_interacoes, func(mid)

        if f_lower * f_mid < 0:
            upper_bound = mid
            f_upper = f_mid
        else:
            lower_bound = mid
            f_lower = f_mid

        num_interacoes += 1

    return (upper_bound + lower_bound) / 2, num_interacoes, func((upper_bound + lower_bound) / 2)

def newton_raphson(func, derivative, x0, tol = 1e-7, max_iter = 100):
    num_iteracoes = 0
    xk = 0

    for _ in range(max_iter):
        xk = x0 - func(x0)/derivative(x0)

        if abs(xk - x0) < tol:
            break

        x0 = xk

        num_iteracoes += 1

    return xk, num_iteracoes, func(xk)

def secante(func, lower_bound, upper_bound, tol = 1e-7, max_iter = 100):
    num_iteracoes = 0

    if (lower_bound == upper_bound):
        upper_bound += 1

    x = 0

    for _ in range(max_iter):
        f_lower = func(lower_bound)
        f_upper = func(upper_bound)

        if f_lower - f_upper == 0:
            print("Divisao por zero")
            break

        x = (lower_bound * f_upper - upper_bound * f_lower)/(f_upper - f_lower)

        if abs(x - upper_bound) < tol:
            break

        lower_bound = upper_bound
        upper_bound = x

        num_iteracoes += 1

    return x, num_iteracoes, func(x)

def main():
    fx = lambda x: x * np.log10(x) - 1
    dfdx = lambda x: np.log10(x) + 1 / np.log(10)

    raiz_bis, num_iter_bis, f_raiz_bis = bisseccao(fx, 2, 3)
    raiz_false, num_iter_false, f_raiz_false = false_position(fx, 2, 3)
    raiz_nr, num_iter_nr, f_raiz_nr = newton_raphson(fx, dfdx, 2.0)
    raiz_sec, num_iter_sec, f_raiz_sec = secante(fx, 2, 3)
    print(f"Bisseccao:\nraiz / f(raiz) / iteracoes\n{raiz_bis} / {f_raiz_bis:.15f} / {num_iter_bis}")
    print(f"\nFalsa posicao:\nraiz / f(raiz) / iteracoes\n{raiz_false} / {f_raiz_false:.15f} / {num_iter_false}")
    print(f"\nNewton-Raphson:\nraiz / f(raiz) / iteracoes\n{raiz_nr} / {f_raiz_nr:.15f} / {num_iter_nr}")
    print(f"\nSecante:\nraiz / f(raiz) / iteracoes\n{raiz_sec} / {f_raiz_sec:.15f} / {num_iter_sec}")

    print("=-"*50 + "=")
    n_fx = lambda x: x ** 3 - 2 * x + 2
    n_dfdx = lambda x: 3 * (x ** 2) - 2

    print(f"Newton-Raphson: {newton_raphson(n_fx, n_dfdx, 1)}")


main()