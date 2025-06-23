# Metodo de Euler para aproximar EDOs

Seja a EDO a seguir: 

$$ 
\begin{align}
    \left \lbrace
        \begin{array}{rcl}
            y'(t) &= & f(t, y(t)) \\
            y(t_0) &= & y_0 
        \end{array}
    \right.
\end{align}
$$

Escolhendo um $h$ para ser o tamanho de cada passo, podemos discretizar nosso intervalo da seguinte maneira:

$$
t_n = t_0 + n \cdot h
$$

E então:

$$
y_{n+1} = y_n + hf(t_n, y_n)
$$

O valor $y_n$ é uma aproximação da solução da EDO no ponto $t_n: y_n \approx y(t_n)$
