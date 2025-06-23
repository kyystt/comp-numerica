import numpy as np
import matplotlib.pyplot as plt

def mtr(f, a, b, n):
    h = (b - a)/n
    xs = np.zeros(n+1)
    ys = np.zeros(n+1)

    xs[0] = a
    xs[n] = n
    ys[0] = 0

    for i in range(n-1):
        xs[i+1] = xs[0] + (i+1)*h
        ys[i+1] = (h * (f(xs[i]) + f(xs[i+1])))/2

    res = sum(ys)

    return xs, ys, res

def main():
    funcao = lambda x: x*(x-10)

    xs, ys, res = mtr(funcao, 0, 10, 100)


main()