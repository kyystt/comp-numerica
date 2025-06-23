# Integração numérica

## Caracterizando o problema
Dada uma função $f \in C[a, b]$, queremos determinar $\displaystyle \int_a^b f(x) \, dx$. Vamos ver apenas o chamado Método de Newton-Cotes que consideramos uma discretização regular do intervalo $[a, b]$ na forma fechada, ou seja, $a$ e $b$ percentem a discretização.

Assim,
$$
\begin{align*}
x_0 &= a \\
x_i &= a + ih \\
h &= \frac{b-a}{n} \\

\end{align*}
$$

Nessa família de métodos, consideramos $f(x) \approx P_n(x)$ e então $\displaystyle \int_a^b f(x) \, dx \approx \int_{x_0}^{x^n} P_n(x) \, dx$

### 1) Método do Trapézio (MT)
Neste caso,
$$
\int_a^b f(x) \, dx \approx \int_{x_0}^{x_1} P_1(x) \, dx
$$
Sabemos:
$$
\begin{align*}
P_1(x) &= L_0(x) \, f(x_0) + L_1(x) \, f(x_1)\\\\
&= \frac{x-x_1}{x_0 - x_1}f(x_0) + \frac{x-x_0}{x_1-x_0}f(x_1) \\\\
&= \frac{x-x_1}{-h}f(x_0) + \frac{x-x_0}{h}f(x_1) 
\end{align*}
$$
Logo,
$$
\begin{align*}
\int_a^b f(x) \, dx \approx \int_{x_0}^{x_1} P_1(x) \, dx = -\frac{f(x_0)}{h}\int_{x_0}^{x_1}(x-x_1) \, dx + \frac{f(x_1)}{h}\int_{x_0}^{x_1}(x-x_0) \, dx
\end{align*}
$$
Seja $z = x - x_0$. Então:
$$
\begin{cases}
dz &= dx \\
z &= 0, & \text{se } x = x_0 \\
z &= h, & \text{se } x = x_1
\end{cases}
$$
e
$$
\begin{align*}
x &= z + x_0 \\
x - x_1 &= z + x_0 - x_1 \\
&= z - (x_1 - x_0) = z - h 
\end{align*}
$$
Logo,
$$
\begin{align*}
\int_a^b f(x) \, dx & \approx -\frac{f(x_0)}{h}\int_{0}^{h}(z - h) \, dz + \frac{f(x_1)}{h}\int_{0}^{h}(z) \, dz \\
&= -\frac{f(x_0)}{h} \left[\frac{z²}{2} - hz \right]\left. \vphantom{\int} \right|_0^h + \frac{f(x_1)}{h} \frac{z²}{2} \left. \vphantom{\int} \right|_0^h \\
&= -\frac{f(x_0)}{h} \left[\frac{h^2}{2} - h^2\right] + \frac{f(x_1)}{h} \frac{h^2}{2} \\
&= f(x_0)\frac{h}{2} + f(x_1) \frac{h}{2} \\
&= \frac{h}{2} \left[f(x_0) + f(x_1) \right]
\end{align*}
$$
OBS.: seja $f(x) = x(x-10)$. Queremos
$$
\int_0^{10} f(x) \, dx
$$
Neste caso, 
$$
\int_0^{10} f(x) \, dx \approx \int_{x_0 = 0}^{x_1 = 10} P_1(x) \, dx = 0
$$
Solução: melhorar a discretização

### 2) Métodos dos Trapézios Repetidos (MTR)
Neste caso, consideramos de fato uma discretização na forma 
$$
x_0 = a \\ 
x_i = a + ih
$$
com  $h = \frac{b-a}{n}$, e aplicamos o MT a cada subintervalo, ou seja,
$$
\begin{align*}
\int_a^b f(x) \, dx &= \int_{x_0}^{x_1} f(x) \, dx + \int_{x_1}^{x_2} f(x) \, dx + \dots + \int_{x_{n-1}}^{x_n} \\
&\approx \frac{h}{2}(f(x_0) + f(x_1)) + \frac{h}{2}(f(x_1) + f(x_2)) + \dots + \frac{h}{2}(f(x_{n-1}) + f(x_n)) \\
&= \frac{h}{2} \left[ f(x_0) + 2 \sum_{k=1}^{n-1} f(x_k) \, + f(x_n) \right]
\end{align*}
$$

# Exercício
Implemente o MTR

Dados:
- $f$ função contínua
- $a < b$, $a, b \in \mathbb{R}$
- $n$ inteiro positivo