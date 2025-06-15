# Aproximando um PVI com o metodo de Euler
# Vamos fazer com o PVI: 
# { y'(t) = y(t)
# { y(0) = 1
import numpy as np

def euler(funcao_derivada, t0, y0, steps, T):
    N = int((T - t0)/steps)
    ts = np.linspace(t0, T, N+1)
    ys = np.zeros(N+1)
    ys[0] = y0

    for i in range(N):
        ys[i+1] = ys[i] + steps*funcao_derivada(ts[i], ys[i])

    return ts, ys

def main():
    dydx = lambda t, y: y
    sol = lambda y: np.exp(y) 

    t0, y0, T, steps = 0, 1, 2, 0.1

    t, y_approx = euler(dydx, t0, y0, steps, T)

    y = sol(t)

    print('='*20 + "\nSolucao aproximada:")
    print(y_approx)
    print('='*20 + "\nSolucao exata:")
    print(y)

main()

