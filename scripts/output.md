> Формула обращения
---
# Теорема
$a < b$ $P(\xi = a) = P(\xi = b) = 0$
Тогда
$$P(a \leq \xi \leq b) = \lim_{T \to +\infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{-iat} - e^{-ibt}}{it}\varphi_\xi(t)dt$$
## Доказательство
**Шаг 1.** $\xi = \frac{a + b}{2} + \frac{b-a}{2}\eta$ , $a \leq \xi \leq b \iff -1 \leq \eta \leq 1$ 
$\varphi_\xi(t) = e^{i\frac{a+b}{2}t}\varphi_\eta (\frac{b-a}{2}t)$  . Если знаем формулу для $\eta$
$$P(a \leq \xi \leq b) = P(-1 \leq \eta \leq 1) = \lim_{T \to +\infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{it} - e^{-it}}{it}\varphi_\eta(t)dt$$
Докажем что формула для (a, b) выполнятся, заменив величину:
$$\lim_{T \to +\infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{-iat} - e^{-ibt}}{it}e^{i \frac{a+b}{2}t}\varphi_\eta(\frac{b-a}{2} t)dt$$
$$\lim_{T \to +\infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{i\frac{b-a}{2}t} - e^{-i\frac{b-a}{2}t}}{it}\varphi_\eta(\frac{b-a}{2} t)dt$$
$s = \frac{b-a}{2}t$
$$\lim_{T \to +\infty} \frac{1}{2\pi} \int_{-\frac{b-a}{2}T}^{\frac{b-a}{2}T} \frac{e^{is} - e^{-is}}{it} \varphi_\eta(s)dt$$
**Шаг 2.** $a = -1, b = 1$
$$P(-1 \leq \xi \leq 1) =? \lim_{T \to +\infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{it} - e^{-it}}{it}\varphi_\xi(t)dt$$
$$\int_{-T}^T \frac{e^{it} - e^{-it}}{it}\varphi_\xi(t)dt = \int_{-T}^T \frac{e^{it} - e^{-it}}{it} \int_{\R} e^{itx} d P_\xi(x)$$
$$= \int_\R \int_{-T}^T \frac{e^{it} - e^{-it}}{it}e^{itx} dt d P_\xi(x)$$
Можем поменять по Фубини, для этого нужно ограничинить и суммируемость
Если $|t| > 1$, то числитель можно оценить двойкой
А в $|t| < 1$ она непрерывна. А по $x$ - вероятностная мера, она 1 и константа суммируемая. Внутренний интеграл назовем $\Phi_T(x)$ 
$$\Phi_T(x) = \int_{-T}^T \int_{-1}^1 e^{itu} e^{itx} du\ dt = \int_{-1}^1 \int_{-T}^T e^{itu} e^{itx} dt \ du$$
$$= \int_{-1}^1 \frac{e^{it(x+u)}}{i(u+x)} \bigg |_{t = -T}^{t = T}du = \int_{-1}^1 \frac{2\sin((x + u) T)}{u + x}{}$$
$y= (x + u) T$
$$\int_{-(x-1T)}^{(x+1)T} \frac{2 \sin y}{y} d y \to_{п.в.} \begin{cases}0 \ \text{при } x > 1 \\ 0 \text{ при } x < -1 \\ 2\pi \text{ при } -1 < x < 1$\end{cases} = \mathbb{1}_{[-1, 1]}(x) \cdot 2\pi$$
$$\lim_{T \to \infty} \int_{\R} \Phi_T(x) d P_{\xi} (x) = \int_{\R} \lim _{T \to +\infty} \Phi_T(x) d P_\xi(x) = \int \mathbb{1}_{[-1, 1]}(x) \cdot 2\pi d P_{\xi} (x)$$
$$= P_\xi ([-1, 1]) \cdot 2\pi$$
Почему можем поменять предел с интегралом? $\Phi_T(x)$ ограничена и теорема лебега о предельном переходе   
# Следствия
## 1
Если $\varphi_\xi = \varphi_\eta$, то  $P_\xi = P_\eta$ 
### Доказательство
Проверим, что функция распределения определяется однозначно характеристической функцией
$$D := \{x \in \R: P(\xi = k) > 0\}$$ - это множество не более чем счетно.  Если $a, b \not \in D$, то $P_\xi([a, b])$ определена однозначно. $P_\xi([a, b]) = F_\xi(b) - F_\xi(a)$ (так как попасть на границу 0).
Рассмотрим последовательность $a_n$ убывают стремятся к $-\infty$ и $a_n \not \in D$ $P\xi([a_n, b]) \to P_\xi(-\infty, b)$. Тогда $P_\xi(-\infty, b]$ определена однозначно. То есть поняли, что $b \not in D$, то функция распределения определяется однозначно

Возьмем $b \in D$ и $b_n$ стремится к $b$ к сверху $b_n \not \in D$, тогда $F_\xi(b) = \lim F_\xi(b_n)$ из непрерывности справа, то есть $F_\xi(b)$ однозначно определяется $\varphi_\xi$

## 2
Если $\int_{\R} |\varphi_\xi(t) | dt < +\infty$, то существует плотность распределения $\xi$ и $$p_\xi(x) = \frac{1}{2\pi} \int_{\R} e^{-itx} \varphi_\xi(t) dt$$ - преобразования Фурье для функции $\varphi_\xi$
### Доказательство
Если $\int_\R |\varphi_\xi(t)| dt$ сходится, то $\int_\R\frac{e^{-iat} - e^{ibt}}{it} \varphi_\xi(t) dt$
абсолютно сходится потому что множитель ограничен, то есть можем писать не в главном значении.
Проверим что $p_\xi(x)$ подходит в качестве определения плотности

$$\int_{a}^b p_\xi(x) dx = \int_a^b \frac{1}{2\pi} \int_\R e^{-itx}\varphi_\xi(t) dt dx$$
Можем поменять местами (оно суммируется)
$$=\frac{1}{2\pi}\int_\R\int_a^b e^{-itx} dx\ \varphi_\xi(t)\ dt = P(a \leq \xi \leq b)$$
Так как интеграл это ровно то что получается в формуле обращения. Значит это плотность
---
> Теорема о сумме независимых нормальных случайных величин
---
# Теорема
$\xi_k \sim \mc{N}(a_k, \sigma_k^2)$ независимы, $c_1, ..., c_k \in \R$ не все нулевые
$\eta := a_0 + \sum_{k=1}^n c_k \xi _k$. Тогда $\eta \sim \mc{N}(a, \sigma^2)$, где $a = a_0 + \sum_{k=1}^n c_k a_k$ и $\sigma^2 = \sum_{k=1}^n c_k^2 \sigma_k^2$ 
## Доказательство
Знаем что $\varphi_{\xi_k}(t) = e^{ia_kt} e^{-\sigma_k^2 t^2 /2}$
$$\varphi_\eta(t) = e^{ia_0t} \varphi_{\xi_1}(c_1t) .... \varphi(\xi_n)(c_nt) =$$

Это дает ровно нужный ответ. А характеристическая функция определяет распределение
---
### Сходимость по распределению
> Распространение непрерывности в сумме независимых величин
---
# Теорема
Если $\xi$ и $\eta$ независимые и $\eta$ - непрерывная случайная величина, то $\xi + \eta$ непрерывная случайная величина.
## Доказательство
$P(\xi + \eta = x) = P_{\xi + \eta}({x}) = \int_{\R} P_\eta({x - y}) d P_\xi(y) = 0$
---
> Лемма о сходимости по распределению из сходимости по интервалам
---
# Лемма
$F_n$ и $F$ - функции распределения, такие что $\forall a, b\in \R$ $$F_n(b) -F_n(a)  \to F(b) - F(a) \quad \text{Тогда } F_n(x) \to F(x) \forall x \in \R$$
## Доказательство
Возьмем $a, b \in \R$, такие что $F(a) < \varepsilon$ $F(b) > 1 - \varepsilon$
Тогда $F_n(b) - F_n(a) \to F(b) - F(a) > 1 - 2 \varepsilon$ Следовательно при больших $n$
$F_n(b) - F_n(a) > 1 - 3\varepsilon$. Тогда $F_n(a) < 3\varepsilon$ $\forall n \geq N$
$$|F_n(x) - F(x)| = |(F_n(x) - F_n(a)) - (F(x) - F(a)) + F_n(a) - F(a)| \leq $$
$$\leq |(F_n(x) - F_n(a)) - (F(x) - F(a))| + |F_n(a)| + |F(a)| < 5\varepsilon$$
при больших $n$
---
> Множество регулярное для распределения
---
# Определение
$B \in \R$ регулярно для $P_\varepsilon$, если $P_\varepsilon(\text{Cl } B \setminus \text{Int } B) = 0$
---
> Теорема о сходимости по распределению
---
# Теорема
$\xi, \xi_1, \xi_2,..$ - случайные величины
$F, F_1, F_2, ...$ - их функции распределения
$\varphi, \varphi_1, \varphi_2, ...$ - их характеристические функции
Следующие условия равносильны:
1. $\xi_n \to \xi$ по распределению
2. $\forall \ \mc{U} \sub \R$  открытого $\underline{\lim} P(\xi_n \in \mc{U}) \geq P(\xi \in \mc{U})$ 
3. $\forall A \sub \R$ замкнутого $\overline{\lim} P(\xi_n \in A) \leq P(\xi \in A)$  
4. $\forall B \sub \R$ борелевского, регулярного для $P_\xi$ $\lim P(\xi_n \in B) = P(\xi \in B)$  
5. $\forall B \sub \R$ борелевского, регулярного для $P_\xi$  $\lim E \ \mathbb{1}_B(\xi_n) = E\ \mathbb{1}_B(\xi)$  
6. Для любого $f \in C(\R)$ и ограниченного $\lim E f(\xi_n) = E f(\xi)$ 
7. $\varphi_n \to \varphi$ поточечно
## Доказательство
$2 \iff 3$  $\mc{U} = \R \setminus A$ $P(\xi_n \in A) = 1 - P(\xi_n \in \mc{U})$ 
$$\overline{\lim} P(\xi_n \in A) = \overline{\lim} (1 - P(\xi_n \in \mc{U})) = 1 - \underline{\lim} P(\xi_n \in \mc{U})$$
$2 + 3 \Rightarrow 4$ $A  := Cl \ B$  , $\mc{U} := Int \  B$
$P(\xi \in B) = P(\xi \in A) \geq \overline\lim P(\xi_n \in A) \geq \overline{\lim} P(\xi_n \in B) \geq \underline \lim P(\xi_n \in B)$ $$\geq \underline{\lim} P(\xi_n \in \mc{U}) \geq P(\xi \in \mc{U}) = P(\xi \in B)$$
Следовательно везде равенства
$4 \iff 5$ $E \ \mathbb{1}_B (\xi) = P(\mathbb{1}_B(\xi) =1) = P(\xi \in B)$ 
$6 \Rightarrow 7$ $\varphi_\xi(t) = E e^{it\xi} = E(\cos (t \xi) + i \sin (t \xi)) = E \cos (t \xi) + i E \sin (t \xi)$. Непрерывные и ограниченные, следовательно стремление доказывается

$1 \Rightarrow 2$. Возьмем $\mc{U}$ - открытое, $\mc{U} = \bscup_{k=1}^\infty (a_k, b_k]$. $P(\xi = a_k) = P(\xi = b_k) = 0$. Почему такое будет? У нас плохих концов не более чем счетное множество. Вместо того что резать по половинкам будет выбирать точки рядом
$$P(\xi_n \in (a_k, b_k]) = F_n(b_k) - F_n(a_k) \to F(b_k) - F(a_k) = P(\xi \in (a_k, b_k])$$
$$P(\xi_n \in \mc{U}) = P(\xi_n \in \bscup_{k=1}^n (a_k, b_k]) \geq P(\xi_n \in \bscup_{k=1}^m (a_k, b_k])$$
$$\sum_{k=1}^m P(\xi_n \in (a_k, b_k]) \to \sum_{k=1}^m P(\xi_n \in (a_k, b_k]) \to \sum_{k=1}^m P(\xi \in (a_k, b_k])$$
$$=P(\xi \in \bscup_{k=1}^m (a_k, b_k])$$
$$\underline{lim} \ P(\xi_n \in \mc{U}) \geq \underline{\lim} \sum_{k=1}^m P(\xi_n \in (a_k , b_k] ) = P(\xi \in \bscup_{k=1}^m (a_k, b_k])$$
$$\to_{m \to \infty} P(\xi \in \bscup_{k=1}^\infty (a_k, b_k] ) = P(\xi \in \mc{U})$$
По непрерывности меры

$5 \Rightarrow 6$ $D = \{ x \in \R: P(f(\xi) = x) > 0\} = \{ x \in \R: P_\xi(f^{-1}(x)) > 0\}$ - не более чем счетное множество, так как они дизъюнктны
$f \in C(\R)$, и $|f| \leq M \not \in D$ 
Нарежем $[-M, M]$ точками $t_j \not \in D$ с мелкостью $< \varepsilon$ $t_0 = -M$ $t_m = M$ 

$B_j := \{x \in \R: t_{j-1} < f(x) \leq t_j\}$
$$\mc{U}_j := \{x \in \R: t_{j-1} < f(x) < t_j\} \sub B_j \sub \{x \in \R: t_{j-1} \leq f(x) \leq t_j\} := A_j$$
$\mc{U_j}$ открытое (прообраз открытого открытый), $A_j$ - замкнутое (дополнение прообраза двух лучей), то есть $\mc{U_j}$ это подмножество внутренности $B_j$, а $A_j$ надмножество замыкания
$\text{Cl } B_j \setminus \text{Int } B_j \sub A_j \setminus \mc{U}_j \sub \{x \in \R: f(x) = t_i \text{ для некоторого i}\}$ 
$P_\xi(\text{Cl } B_j \setminus \text{Int } B_j) \leq P_\xi(f^{-1} (t_i)_{i = 1...m}) = 0$, то есть $B_j$ - $P_\xi$ регулярные 

$E \mathbb{1}_{B_j} (\xi_n) \to E \mathbb{1}_{B_j}(\xi)$ 

$g(x) := \sum_{j=1}^m t_j \mathbb{1}_{B_j} (x) \Rightarrow E g(\xi_n) \to E g(\xi)$

$|f(x) - g(x)| \leq \varepsilon \Rightarrow$ $E|f(\xi_n) - g(\xi_n)| \leq \varepsilon$

$$|Ef(\xi_n) - Ef(\xi)| = |E(f\xi_n) - Eg(\xi_n) + Eg(\xi_n) - Eg(\xi) + Eg(\xi) - Ef(\xi)|$$
$$\leq 3\varepsilon$$ при больших n


$7 \Rightarrow 1$. Если $\varphi_n \to \varphi$ , то $F_n \to F$ в точках непрерывности
Возьмем $\eta_\sigma \sim \mc{N}(0, \sigma^2)$ не зависащая от $\xi_1, \xi_2$ 
$\psi_n(t):=\phi_{\xi_n + \eta_\sigma} = \varphi_n(t) \cdot \varphi_{\eta_\sigma}(t) = \varphi_n(t) e^{-\sigma^2t^2/2} \to \varphi(t) e^{-\sigma^2t^2/2} = \varphi_{\xi + \eta_\sigma} =: \psi(t)$ 
$$P(\xi_n + \eta_\sigma \in [a, b]) = \lim_{T \to \infty} \frac{1}{2\pi} \int_{-T}^T \frac{e^{-iat} - e^{-ibt}}{it}\psi_n(t) dt$$
$|\psi_n(t)| \leq e^{-\sigma^2 t^2/2}$
$$\frac{1}{2\pi}\int_{\R} \frac{e^{-iat} - e^{-ibt}}{it} \psi_n(t) dt \to \frac{1}{2\pi}\int_{\R} \frac{e^{-iat} - e^{-ibt}}{it} \psi(t) dt = P(\xi + \eta_\sigma \in [a, b])$$
то есть $P(\xi_n + \eta_\sigma \in *a, b]) \to P(\xi + \eta_\sigma \in (a, b])$ 
$G_n(x) := F_{\xi_n + \eta_\sigma}(x)$
Тогда $G_n(b) - G_n(a) \to G(B) - G(a) \forall a, b \in \R$ 
Тогда по лемме 
$G_n(x) \to G(x) \ \forall x \in \R$ 

Перейдем обратно
$\{\xi_n + \eta_\sigma \leq x - \delta \} \setminus \{|\eta_\sigma| \geq \delta\} \sub \{\xi_n \leq x\} \sub \{\xi_n + \eta_\sigma \leq x + \delta\} \cup \{|\eta_\sigma| \geq \delta\}$  
$$G_n(x - \delta) - P(|\eta_\sigma| \geq \delta)\leq F_n(x) \leq G_n(x + \delta) + P(|\eta_\sigma| \geq \delta)$$
$P(|\eta_\sigma| \geq \delta) \leq \frac{\sigma^2}{\delta^2}$ по Чебышеву. То есть можем заменить на $\sigma^2/\delta^2$ 
$$\overline{\lim} F_n(x) \leq \overline\lim G_n(x + \delta) + \frac{\sigma^2}{\delta^2} = G(x + \delta) + \frac{\sigma^2}{\delta^2} \leq F(x + 2\delta) + \frac{2\sigma^2}{\delta^2}$$
$$ F(x - 2\delta) - \frac{2\sigma^2}{\delta^2}\leq G(x - \delta) - \frac{\sigma^2}{\delta^2}\leq\underline\lim G_n(x - \delta) - \frac{\sigma^2}{\delta^2}\leq\underline \lim F_n(x)\leq \overline\lim F_n(x)$$
$$F(x - 2\delta) - \frac{2\sigma^2}{\delta^2} \leq \underline \lim F_n(x) \leq \overline \lim F_n(x) \leq F(x + 2\delta) + \frac{2\sigma^2}{\delta^2}$$
Устремляем $\sigma$ к нулю, избавимся от констант. Пусть $x$ точка непрерывности $F$ и $\delta \to 0$. Правый стремится к F(x), левый стремится к $F(x)$, неравенства обращаются в равенства. Доказали стремление по распределению.
---
> Критерий равномерной сходимости распределений
---
# Теорема
$F_n, F: \R \to [0, 1]$ функция распределения и $f \in C(\R)$. Если $F_n \to F$ поточечно, то $F_n \rightrightarrows F$  равномерно
## Доказательство
Найдем точки $t_k$, такие что $F(t_k) = \frac{k}{m}$. Если какое-то значение не нашлись, то множество значений меньше чем $[0, 1]$.

Во всех этих точках $F_n(t_k) \to F(t_k) \forall k$, найдедтся $N$, такой что $\forall n \geq N$ $|F_n(t_k) - F(t_k)| < \varepsilon$. Возьмем $t_k \leq t \leq t_{k+1}$ 
$$F_n(t) \leq F_n(t_{k+1}) < F(t_{k+1}) + \varepsilon = \frac{k}{m} + \frac{1}{m} + \varepsilon = F(t_k) + \varepsilon + \frac{1}{m} \leq F(t) + \varepsilon + \frac{1}{m}$$
С другой стороны:
$$F_n(t) \geq F_n(t_{k+1}) - \varepsilon = \frac{k}{m} - \varepsilon = \frac{k+1}{m} - \frac{1}{m} - \varepsilon = F(t_{k+1}) - \frac{1}{m} - \varepsilon \geq F(t) - \frac{1}{m} - \varepsilon$$
Если $k = 0$, то $F_n(t) \geq 0 \geq F(t_1) - \frac{1}{m} - \varepsilon \geq F(t) - \frac{1}{m} -\varepsilon$. Аналогично сверху для $k = m - 1$
Следовательно $|F_n(t) - F(t)| \leq \varepsilon + \frac{1}{m}$
---
### Центральная предельная теорема
> ЦПТ в форме Поля Леви
---
# Теорема
$\xi_1, \xi_2, ...$ независимые одинаково распределенные случайные величины
$a := E\xi_k$, $\sigma^2 := D\xi_k > 0$ конечная, $S_n := \xi_1 + ... + \xi_n$. Тогда $$P(\frac{S_n - na}{\sqrt{n} \sigma} \leq x) = P(\frac{S_n - ES_n}{\sqrt{DS_n} } \leq x) \rightrightarrows \Phi(x) = \frac{1}{2\pi}\int_{-\infty}^x e^{-t^2/2} dt$$
## Доказательство
Надо доказать что $F_{\frac{S_n - na}{\sqrt{n}\sigma}}\to \Phi$ то есть сходимость к нормальному распределению
Сдвинем все $\xi_n$ на $a$, то есть будем считать что $E\xi_n = 0$ 
Надо доказать, что $F_{\frac{S_n}{\sqrt{n} \sigma}} \to \Phi$. Достаточно доказать что $\varphi_{\frac{S_n}{\sqrt{n}\sigma}} \to \phi(t) = e^{-t^2/2}$ 
$\phi_{\xi_k}(t) = 1 - \frac{\sigma^2 t^2}{2} + o(t^2)$    $\varphi_{S_n} = \prod \varphi_{\xi_k} = (1 - \frac{\sigma^2 t^2}{2} + o(t^2))^n$   
$\varphi_{\frac{S_n}{\sigma\sqrt{n}}} = \varphi_{S_n} (\frac{t}{\sigma\sqrt{n}}) = (1 - \frac{t^2}{2n} + o(\frac{1}{n}))^n$  
Это стремится $e^{-\frac{t^2}{2}}$ 
# Следствия
## [[Интегральная теорема Муавра-Лапласа]]
В этот раз в терминах вероятностного пространства
$\xi_1, \xi_2, ...$ - независимые бернуливские случайные величины с вероятностью успеха $p$
$S_n = \xi_1 + ... + \xi_n$. Тогда $$P(\frac{S_n - np}{\sqrt{npq}} \leq x) \rightrightarrows \Phi(x)$$
---
> Теорема Пуассона (В)
---
# Теорема
$P(\xi_{nk} = 1) = p_{nk} \quad P(\xi_{nk} = 0) = 1 - P_{nk} =: q_{nk}$ 
$\xi_{n1}, ..., \xi_{nn}$ независимы. $p_{1n} + p_{n2} + ... + p_{nn} \to \lambda > 0$ 
$\max_{1 \leq k \leq n} p_{nk} \to 0$. Тогда $$P(S_n =m) \to e^{-\lambda} \cdot \frac{\lambda^m}{m!} \quad S_n := \xi_{n1} + \xi_{n2} + ... + \xi_{nn}$$
## Замечание
В прошлой [[Теорема Пуассона]] $p_{n1} = p_{n2} = ... = p_{nn} := p_n$ . $np_n \to \lambda$
## Доказательство
$\varphi_{\xi_{nk}}(t) = Ee^{it\xi_{nk}} = P(\xi_{nk} = 0) + e^{it} P(\xi_{nk} = 1) = e^{it} p_{nk} + 1 - p_{nk} = 1 + p_{nk} (e ^{it} - 1)$ 
$$\varphi_{S_n}(t) = \prod\varphi_{\xi_{nk}}(t) = \prod_{k=1}^n (1 + p_{nk}(e^{it} -1))$$
Хотим понять что есть сходимость к распределению пуассона, то есть $$\varphi(t) = \sum_{n=0}^\infty e^{itn} e^{-\lambda} \frac{\lambda^n}{n!} = \sum_{n=0}^\infty \frac{(\lambda e^{it})^n}{n!} e^{-\lambda} = exp(\lambda(e^{it} -1))$$
Логарифмируем. смотрим на $\sum_{k=1}^n \ln (1 + p_{nk} (e^{it} -1))$
По формуле Тейлора:
$$\sum_{k=1}^n ((e^{it} - 1)p_{nk} + O(p_{nk}^2)) \to \lambda (e^{it}-1) + \sum_{k=1}^n O(p_{nk}^2) \leq \lambda(e^{it}- 1) + C \max p_{nk}  \sum_{k=1}^n p_{nk} \to \lambda(e^{it} - 1)$$ То есть есть сходимость по распределению.
Так как величина дискретная, то нужно отойти $+\eps$ и $-\eps$ мы сможем получить как разницу (функция распределения ступенчатая)
---
> ЦПТ в форме Линденберга
---
# Теорема
$\xi_k$ - неазвисимые случайные величины $a_k = E\xi_k$, $\sigma^2 := D\xi_k > 0$ $S_n := \xi_1 + ... + \xi_n$ 
$D_n^2 := \sum_{k=1}^n \sigma_k^2 < +\infty$ 
$Lind(\varepsilon, n) L= \frac{1}{D_n^2} \sum_{k=1}^n E f(\xi_n - a_k) \to_{n \to \infty} 0$, где $f(x) := x^2 \mathbb{1}_{\{|x| \geq \varepsilon D_n\}}(x)$ при всех $\varepsilon > 0$ 
Тогда $$P(\frac{S_n - ES_n}{\sqrt{DS_n}} \leq x) \rightrightarrows \Phi(x)$$




#exercise  проверить что условие линденберга выполнена для независимых одинаково распределенных случайных величин с конечной дисперсией
---
> ЦПТ в форме Ляпунова
---
# Теорема
$\xi_1, ..$ - независимые
$a_k := E \xi_k$, $\sigma_k^2 := D\xi_k > 0$  $S_n = \sum \xi_k$ . $\mc{D}_n^2 := \sum_{k=1}^n \sigma_k^2 < +\infty$  
$L(\delta, n) :- \frac{1}{D_n^{2 + \delta}} \sum_{k=1}^n E |\xi_k - a_k|^{2+\delta} \to 0$  Для некоторого $\delta > 0$
Тогда $$P(\frac{S_n - E S_n}{\sqrt{D S_n}} \leq x) \rightrightarrows \Phi(x)$$
## Доказательство
Линденберг $=>$ Ляпунов
$$Lind(\varepsilon, n) L= \frac{1}{D_n^2} \sum_{k=1}^n E((\xi_k - a_k)^2 \mathbb{1}_{\{|x| \geq \varepsilon D_n\}}(\xi_k - a_k))$$
$$\leq \frac{1}{D_n^2} \sum_{k=1}^n E((\xi_k - a_k)^2 \frac{|\xi_k - a_k|^\delta}{(\varepsilon D_n)^\delta}) = \frac{1}{\varepsilon^\delta D_n^{2+\delta}} \sum E(|\xi_k -a_k|^{\delta + 2}) \to 0$$
---
> Оценки на скорость сходимости
---
# Теорема 
$\forall \delta \in (0, 1]$ $|P(\frac{S_n - ES_n}{\sqrt{DS_n}} \leq x) - \Phi(x) | \leq C_{\delta} L(\delta, n)$ 
## Замечание
Для одинаково распределенных $E\xi_k = a \ D\xi_k = \sigma$ $D_n^2 = n\sigma^2$ 
$L(\delta, n) = \frac{1}{(\sqrt{n} \sigma)^{2 + \delta}} \cdot n \cdot E|\sigma_k -a|^{2 + \delta}$
Из этого следует теорема Барри Эссеена при $\delta = 1$ 

$$|P(\frac{S_n - na}{\sqrt{n}\sigma} \leq x) - \Phi(n)| \leq C \frac{E |\xi_k - a|^3}{\sigma^3 \sqrt{n}}$$
Для Барри эссена есть следующие константы:
$C \geq \frac{\sqrt{10} + 3}{6\sqrt{2\pi}} \approx 0,4097$ (Доказал Эссен 1956)
$C \leq 0,469$ Шевцова (2014)

Для общего случая $C_1 \leq 0,5583$
---
> Теорема Хартмана-Винтнера
---
# Теорема
$\xi_1, \xi_2, ...$ - независимые одинаково распределенные случайные величины $E\xi_i = 0$ $D\xi_i = \sigma^2 > 0$
$$\overline \lim \frac{S_n}{\sqrt{2n\ln \ln n}} = \sigma$$
а нижний предел $-\sigma$
---
> Теорема Штрассена
---
Любая точка отрезка $[-\sigma, \sigma]$ предельная точка последовательности $\frac{S_n}{\sqrt{2n \ln \ln 2}}$ из [[Теорема Хартмана-Винтнера]]
---

### Вероятности больших уклонений
> ЗБЧ в форме Хинчина
---
# Теорема
$\xi_1, \xi_2, ...$ - независимые одинаково распределенные случайные величины. $a := E \xi_i$, $S_n := \xi_1 + \xi_2 + ... + \xi_n$. Тогда $\forall r > a$ $$P(\frac{S_n}{n} \geq r) \to 0$$
## Оценка
Неравенство чебышева дает оценку
$$P(\frac{S_n}{n} \leq r) \leq \frac{\sigma^2}{n (r -a)^2}$$
---
> Условие Крамера
---
# Определение
Случайная величина удовлетворяет условию Крамера, если в некоторой окрестности нуля $Ee^{\lambda \sigma} < +\infty$
---
> Оценка Чернова
---
$r > E \xi_i$, $\xi_i$ одинаково распределенные и независмые
$P(\frac{S_n}{n} \geq r) = P(\lambda S_n \geq \lambda r n) = P(e^{\lambda S_n} \geq e^{\lambda r n}) \leq \frac{E e^{\lambda S_n}}{e^{\lambda r n}} = (\frac{E(e^{\lambda \xi_i})}{e^{\lambda r}})^n$  
Пусть $\psi(\lambda) := \ln E e^{\lambda \xi_i}$ Тогда это становится равно $\exp(n(\psi(\lambda) - \lambda r)) = \exp(-n(\lambda r - \psi(\lambda))$ 
$I(r) := sup_{\lambda > 0} (\lambda r - \psi(\lambda))$ 
$$P(\frac{S_n}{n} \geq r) \leq e^{-nI(r)}$$
Это оценка чернова, а $I(r)$ - функция уклонения
## Примеры функций уклонения
$I(r) = sup_{\lambda > 0} (\lambda r - \psi(\lambda))$
$\psi(\lambda) \ln E e^{\lambda \xi_i}$
$\psi(0) = 0$ 
$\psi^\prime(0) = \frac{E(\xi_1 e^{\lambda \xi_1})}{E e^{\lambda \xi_1}} = E \xi_1$ 
1. $\xi_k \sim \mc{N}(0, 1)$
   $$\psi(\lambda) = \ln E e^{\lambda \xi_1} = \ln (\frac{1}{\sqrt{2\pi}} \int_{\R} e^{\lambda t} e^{-t^2/2} dt ) = \ln (\frac{1}{\sqrt{2\pi}} e^{\lambda^2/2} \int_{\R} e^{-(t - \lambda)^2/2} dt)$$
   $$= \ln e^{\lambda^2/2} = \lambda^2/2$$
   $$I(r) = sup_{\lambda > 0} (\lambda r - \lambda^2/2) = \frac{r^2}{2}$$
   $$P(\frac{S_n}{n} \geq r) \leq e^{-nr^2/2}$$
---
## Дискретные случайные процессы
### Условные математические ожидания
> Условное математическое ожидание относительно события
---
# Определение
$P(\Omega, F, P)$  - вероятностное пространство, $A \in F$ случайное событие. $P(A) > 0$
Условное математическое ожидание относительно случайного события $E(\xi \mid A) := \frac{E (\xi \mathbb{1}_A)}{P(A)}$
---
> Условное математическое ожидание относительно сигма-алгебры
---
# Определение
$(\Omega, F, P)$ - вероятностное пространство $\mc{A} \sub F$ - $\sigma$-алгебра. Условное мат ожидание относительно $\sigma$-алгебры $A$
$E (\xi \mid \mc{A})$ - случайная величина $\eta$, такая что
1. $\eta$ измерима относительно $\mc{A}$ 
2. $\forall A \in \mc{A}$ $E(\xi \mathbb{1}_A) = E(\eta \mathbb{1}_A)$
## Замечание
Если $A = \{0, \Omega\}$, то условное матожидание $= E\xi$ 

## Свойства условных мат ожиданий
1. $E(c | \mc{A}) = c$
2. линейность $E(\alpha \xi + \beta \eta | \mc{A}) = \alpha E(\xi | \mc{A}) + \beta E(\eta | \mc{A})$
   **докво** $\overline{\xi} := E(\xi \mid \mc{A})$ $\overline\eta := E(\eta \mid \mc{A})$ $\Rightarrow$ линейная комбинация измерима. По линейности можем разбить и собрать
3. $E(\xi | \{\emptyset, \Omega\}) = E\xi$
   **докво** $\overline{\xi} := E(\xi \mid \{0, \xi\})$. $\overline{\xi}$ измерима относительно $\{0, \Omega\}$, следовательно это контстанта. $E(\xi \mathbb{1}_\Omega) = E(c\mathbb{1}_\Omega) \Rightarrow c = E\xi$ 
4. Если $\mc{A}_1 \sub \mc{A}_2$, то $E(\xi | \mc{A}_1) = E(E(\xi | \mc{A}_2) | \mc{A}_1)$
   **докво** Пусть $\overline \xi := E(\xi | \mc{A}_1)$ $\tilde \xi = E(\xi | A_2)$. По определению для правого нужна 1) Измеримость $\overline \xi$  относительно $A_1$- она есть так как по условию условное матожидание измеримо  
   Во-вторых $E(\tilde \xi \mathbb{1}_{A}) = E(\overline\xi \mathbb{1}_{A})$ $\forall A \in A_1$. Первое у нас по определению равно Они оба равны $E(\xi \mathbb{1}_A) \forall A \in \mc{A}$ 
5. $E(E(\xi \mid \mc{A})) = E\xi$
   **докво** $E\xi = E(\xi \mid \{0, \Omega\}) = E(E(\xi \mid \mc{A}) | \{0, \Omega\}) = E(E(\xi \mid \mc{A}))$ 
6. Если $\xi$ измерима относительно $\mc{A}$, то $E(\xi \mid \mc{A}) = \xi$
7. Если $\xi \leq \eta$, то $E(\xi \mid \mc{A}) \leq E(\eta \mid \mc{A})$ почти наверное
   **док-во** $A:= \{\overline \xi > \overline \eta\} \in \mc{A}$ $\Rightarrow$ $E(\overline{\xi} \mathbb{1}_A) = E(\xi \mathbb{1}_{A}) \leq E(\eta \mathbb{1}_A) = E(\overline\eta \mathbb{1}_A)$   $\Rightarrow$ $E((\overline \xi - \overline \eta) \mathbb{1}_A) \leq 0$. Значит эта функция почти наверное 0.
# Важный пример
$\Omega = \bscup A_n$ не более чем счетное объединение, такое что $P(A_n) > 0$ $\forall n$. натянем на $A_n$ $\sigma$-алгебру $\mc{A}$. Поймем что такое $E(\xi \mid \mc A)$ - случайная величина, измеримая относительно $A$
и она имеет вид $\sum c_k \mathbb{1}_{A_k}$. Если бы какое-то множество имеет не константу. $\xi(k) < \xi(y)$, тогда $\xi(x) < c < \xi(y)$ и рассмотрим $\{\xi \leq c\}$ 
Ещё нужно проверить равенство $E(\xi\mathbb{1}_A) = E(\overline \xi \mathbb{1}_A) \forall A \in \mc{A}$ 
Для этого достаточно посмотреть на $A_K$
$$E(\xi \mathbb{1}_{A_k}) = E(\overline{\xi}\mathbb{1}_k) = E(\sum_{j} c_j \mathbb{1_{A_j} \cdot 1_{A_k})} = E(c_k \mathbb{1}_{A_k}) = c_k P(A_k)$$
$$c_k = \frac{E(\xi \mathbb{1}_{A_k})}{P(A_k)}$$
$$E(\xi \mid A) = \sum \frac{E(\xi \mathbb{1}_{A_k})}{P(A_k)} \mathbb{1}_{A_k}$$
---
> Теорема о существовании и почти единственности условного матожидания относительно сигма алгебры
---
# Теорема
$E(\xi | \mc{A})$ существует и единственно в следующем смысле: если $\eta_1$ и $\eta_2$ - условные матождания, то $\eta_1 = \eta_2$ почти наверное

## Доказательство
**Единственность:** $A := \{\eta_1 > \eta_2\}\ \in \mc{A}$ - лебегово множество для измеримой функции
$$E(\eta_1 \mathbb{1}_A) = E(\xi \mathbb{1}_A)= E(\eta_2 \mathbb{1}_A)$$$$E((\eta_1 - \eta_2) \mathbb{1}_A) = 0$$
Матожидание положительной штуки равна 0.
**Существование** $\mu_{\pm} A := E(\xi_{\pm} \mathbb{1}_A)$ - меры
если $P(A) = 0$ то $\mu_{\pm} A = 0$. То есть $\mu_{\pm}$ абсолютно непрерывно относительно $P$.
по теореме Радона-Никодима существует $\omega_\pm \geq 0$ плотность $\mu_\pm$ относительно P ![[Screenshot 2025-06-15 at 20.02.38.png]]
$$E(\xi_{\pm} \mathbb{1}_A) =\mu_{\pm} A = \int_A \omega_{\pm} dP$$
$$E(\xi\mathbb{1}_{A}) = \int_\Omega (\omega_+ - \omega_-) \mathbb{1}_A d P$$
---
> Условная вероятность относительно сигма-алгебры
---
# Определение
$P(B \mid \mc{A}) := E(\mathbb{1}_B \mid \mc{A})$
---
> Условное матожидание относительно случайной величины
---
# Определение
Условное матожидание одной случайной величины относительно другой случайной величины. Рассмотрим $\sigma (\eta)$ - наименьшая $\sigma$ алгебра, относительно которой $\eta$ измерима.
$$E(\xi\mid \eta) := E(\xi \mid \sigma(\eta))$$
# Свойства
1. Если $\xi$ и $\eta$ независимы, то $E(\xi \mid \eta) = E\xi$ 
   **доказательство** $E(\xi \mathbb{1}_{A}) ?= E(E(\xi )\mathbb{1}_A) \forall A \in \sigma(\eta)$ 
   Достаточно доказать что $\xi$  и $\mathbb{1}_{A}$ независимы
   Если $A = \{\eta \leq c\}$ то $\xi$ и $\mathbb{1}_A$ независимы. Для объединений верно, перейдем к пределу, свойство сохраняется
2. Если $\eta$ измерима относительно $\mc{A}$, то $E(\xi \eta \mid A) = \eta E (\xi \mid \mc{A})$ 
   **доказательство**  Шаг 1. $\eta = \mathbb{1}_B$, где $B \in \mc{A}$, Надо доказать что $\mathbb{1}_B E(\xi \mid \mc{A}) = E(\xi \mathbb{1}_B \mid \mc{A})$. $\mathbb{1}_B$  и $E(\xi \mid \mc{A})$ измеримы относительно $\mc{A}$. Нужно проверить равенство $$E(\mathbb{1}_B E(\xi \mid \mc{A}) \mathbb{1}_A) = E(\mathbb{1}_{A \cap B} E(\xi \mid \mc{A})) = E(\mathbb{1}_{A \cap B} \xi)$$ что и требовалось
   Шаг 2 для простых
   Шаг 3 По леви для неотрицательных
   Шаг 4 для всех функций
# Пример
$\eta$ - дискретная случайная величина, тогда $\{\eta = y_n\}$ образует разбиение $\Omega$
$$E(\xi \mid \eta) = \sum \frac{E(\xi \mathbb{1}_{\{\eta = y_n\}})}{P(\eta = y_n)} \mathbb{1}_{\{\eta = y_n\}}$$
# Пример
$N$ - случайная величина, принимающая натуральные значения. $\xi_1, \xi_2, \xi_3, ..$ - одинаково распределенные случайные величины. Пусть $N, \xi_1, \xi_2, ...$ - независимы $S := \xi_1 + ... + \xi_N$
Найдем $ES$
$$ES = E(E(S \mid N))$$
$$E(S \mid N) = \sum \frac{E (S \mathbb{1}_{\{N = n\}})}{P(N = n)} \mathbb{1}_{\{N = n\}}$$
Верхнее это $E((\xi_1 + ... + \xi_N) \mathbb{1}_{\{N = n\}}) = E((\xi_1 + ... + \xi_n) \mathbb{1}_{\{N = n\}}) = n \cdot E\xi \cdot P(N = n)$ 
$$=E\xi\sum_{n=0}^\infty n \mathbb{1}_{\{N = n\}}$$
$$ES = E(E\xi \sum_{n=0}^\infty \mathbb{1}_{N =n}) = E\xi \sum n \cdot P(N =n) = E\xi EN$$
# Пример
$N, \xi_1, \xi_2, ...$ принимают неотрицательные целые значения, независимы
$\xi_1, \xi_2, ...$ одинаково распределены, $G$ их производящая функция, $F$ - производяшая функция $N$ 
Найдем $G_S$, где $S := \xi_1 + \xi_2 + ... + \xi_N$
$$G_S(t) = Et^S = E(E(t^S | N))$$
$E(t^s \mid N) = \sum_{n=0}^\infty \frac{E t^s \mathbb{1}_{\{N = n\}}}{P(N = n)} \mathbb{1}_{N = n}$ 
Верхняя:
$$E(t^s \mathbb{1}_{N = n}) = E(t^{\xi_1 + \xi_2 + ... + \xi_N} \mathbb{1}_{N = n}$) = E t^{\xi_1} \cdot ... \cdot E t^{\xi_n} E \mathbb{1}_{\{N = n\}} \cdot P(N = n)$$ $$= \sum_{n=0}^\infty G^{n} (t) \mathbb{1}_{\{N = n\}}$$
Итого $E(E(t^s \mid N)) = E(\sum_{n=0}^\infty G^n(t) \mathbb{1}_{\{N = n\}}) = \sum_{n=0}^\infty G^n(t) P(N = n) = F(G(t))$
# Геометрическая интерпретация
Рассмотрим только такие $\xi$, у которых $E\xi^2 < +\infty$ $L^2(\Omega, \mc{F}, \mc{P})$ 
Возьмем $A \sub \mc{F}$ $\sigma$-алгебра, $L^2(\Omega, \mc{A}, \mc{P})$  такие $\overline{\xi}$, у которых $E \overline \xi^2 < +\infty$ и они измеримы относительно $\mc{A}$
Тогда это замкнутое подпространство верхнего пространства

Условное матожидание относительно $\mc{A}$ - проекция на $L^2 (\Omega, \mc{A}, P)$
Поймем что $\overline \xi - \xi \perp \mathbb{1}_A \forall A \in \mc{A}$ 
$0 = <\overline{\xi} - \xi, \mathbb{1}_\mc{A}> = \int_\Omega (\overline\xi - \xi) \mathbb{1}_A d P = E((\overline \xi - \xi) \mathbb{1}_A) = E(\overline{\xi} \mathbb{1}_A ) - E (\xi \mathbb{1}_A) = 0$
---

### Ветвящиеся процессы
> Ветвящийся процесс
---
# Определение
В нулевой момент времени есть одна частица
$\xi_j^{(k)}$ - случайные величины со значениями неотрицательными целыми числами, означающие колво потомков j-той частицы в k-тый момент времени.
Все $\xi_j^{(k)}$ независимые и одинаково распределены.
$\eta_k := \xi_1^{(k)} + ... + \xi_{\eta_{k-1}}^{(k)}$ - количество частиц  в $k$-тый момент времени
$P(\xi_j^{(k)} = m) =: f_m$ 
$F(t) = \sum_{m=0}^\infty f_m t^m$ производящая функция для $\xi_j^{(k)}$ 
$G_k(t)$ - производящая функция для $\eta_k$
$G_n(t) = G_{n-1}(F(t)) = F \circ F \circ ... \circ F(t)$ из примера в предыдущем параграфе
$E \eta_n = G_n^\prime(1) = (G_{n-1}(F(t))^\prime \mid_{t= 1} = G_{n-1}^\prime(F(1)) \cdot F^\prime(1)$
$= G_{n-1}^\prime (1) F^\prime(1) = E_{\eta_{n-1}} \cdot F^\prime (1) = (F^\prime(1))^n = (E\eta_1)^n$
---
> Вероятность вырождения процесса - наименьший неотрицательный корень уравенения F(x) = x
---
# Теорема
Вероятность вырождения процесса - наименьший неотрицательный корень уравнения $F(x) = x$ 
## Доказательство
$A_n := \{\eta_n = 0\}$ $A_n \sub A_{n+1}$ $P(A_n) = P(\eta_n = 0) = G_n(0)$ 
$P(A_n) \leq P(A_{n+1})$ Существует $\lim P(A_n) =: q$ - монотонная последовательность ограниченная сверху
$$q =\lim P(A_n) = \lim G_n(0) = \lim F(G_{n-1}(0)) = F(\lim G_{n-1}(0)) = F(q)$$
Поменять можем так как $F$ непрерывная
Следовательно $q$ - корень $F(x) = x$
Докажем что это наименьший корень
Пусть $y$ - наименьший неотрицательный корень этого уравнения. Докажем, что $q \leq y$ 
По индукции по $n$ $G_n(0) \leq y$ 
База $n = 0$ $0 \leq y$. Переход $n \to n +1$
$G_n(0) \leq y \Rightarrow F(G_n(0)) \leq F(y)$ 
# Замечания
1. $G_{1}^\prime(1) = F^\prime(1) = E\eta_1 = : m$ среднее количество потомков у частицы 
2. $F$ нестрого возрастает на $[0, 1]$ $F^\prime(t) =  \sum_{k=1}^\infty k f_k t^{k-1} > 0$. то есть если $f_0 < 1$ то это даже строго
   $F$ выпукла на $[0, 1]$ $\sum_{k=1}^\infty k (k - 1) f_kt^{k-2} > 0$, если $f_ 0 + f_1 < 1$. 
3. $F(0) = f_0 \geq 0$. Если $m \leq 1$ то вероятность вырождения 1. Если $m > 1$, то вероятность вырождения $< 1$. Так как нет второго корня отличного от единицы. Так как m это угол наклона.
   ![[Screenshot 2025-06-17 at 20.44.05.png]]
---
> Теорема о скорости вырождения частиц с средним количеством потомков 1
---
# Теорема
Пусть $m := F^\prime(1) = 1$ и $b = D \eta_1 > 0$ 
$q_n := P(\eta_n = 0)$ вероятность вырождения к $n$-ному шагу
$\gamma_n = q_{n+1} - q_{n}$  - вероятность того что частицы исчезли в точности после $n$-шага
Тогда $\gamma_n \sim \frac{2}{bn^2}$ и $1 - q_n \sim \frac{2}{bn}$
## Доказательство
$A_n := \{\eta_n = 0\}$ $q_n := P(A_n)$ 
$b = D\eta_1 = G^{\prime \prime}_1(1) + G^\prime_1(1) - (G^\prime(1))^2 = G_1^{\prime\prime}(1)$
$G_1(1) = 1$ и $G_1^\prime(1) = m = 1$

$g(x) = 1 - G(1 - x)$
$g^\prime(x) = G^\prime(1 - x) \Rightarrow g^\prime(0) = 1$
$g^{\prime\prime} (x) = - G^{\prime\prime}(1- x) \Rightarrow g^{\prime\prime}(0) = - b$
$g(x) = x - \frac{bx^2}{2} + o(x^2)$
$p_n := 1 - q_n$
$p_{n+1} = 1- q_{n+1} = 1 - G_1(q_n) = 1 - G_{1}(1 - p_n) = g(p_{n})$
$\gamma_n = p_n - g(p_n)$ 
$a_n = \frac{1}{p_n}$
$a_{n+1} - a_{n} = \frac{1}{p_{n+1}} - \frac{1}{p_n} = \frac{p_n - p_{n+1}}{p_n p_{n+1}} = \frac{p_n - g(p_n)}{p_n g(p_n)} = \frac{\frac{bp^2_{n}}{2} + o(1)}{p_n(p_n + o(p_n))} = \frac{b}{2} + o(1) \Rightarrow a_n \sim \frac{bn}{2}$
$$\gamma \sim \frac{bp_n^2}{2}$$
Значит чем больше дисперсия тем быстрее процесс вырождается
---

### Цепи Маркова
> Цепь маркова
---
# Определение
$Y$ - нбсч множество - фазовое пространство
$(\Omega, P, \mc{F})$ - вероятностное пространство. $\xi_0, \xi_1, ...: \Omega \to Y$ 
случайные величины и $$P(\xi_n = a_n \mid \xi_{n-1} = a_{n-1}, ..., \xi_{0} = a_0) = P(\xi_n - a_n \mid \xi_{n-1} = a_{n-1}) $$
если $P(\xi_{n-1} = a_{k=1} , ..., \xi_0 = a_0) > 0$, то $\xi_0, \xi_1, ...$ цепь Маркова 

# Замечание 1
$\xi_0, \xi_1, ...$ независимы, то это цепь Маркова
# Замечание 2
Состояние цепи определяется двумя характеристиками
Начальная функция распределения $\pi_0 = P_\xi$
Функции перехода $p_n(a, b) := p(\xi_n = b \mid \xi_{n-1} = a)$
# Примеры
1. Случайное блуждание по точкам прямой
2. Прибор: есть состояние работает и не работает. Может менять состояния с вероятностями $p$ и $q$ соответственно
---
> Траектория в цепи маркова
---
# Определение
Последовательность значений $\xi_0 = a_0, \xi_1 = a_1, ..., \xi_n = a_n$ - траектория [[Цепь маркова |цепи маркова]]. $\xi_n$ - состояние цепи в момент времени $n$
---
> Однородная цепь маркова
---
# Определение
Цепь маркова однородная, если $p_n(a, b)$ не зависят от $n$
$p_{ab} = p_n(a,b)$ 
$P = (p_{ab})_{a, b \in Y}$ - матрица переходов (возможно бесконечная)
$\pi_n$ распределение состояний цепи на $n$-м шаге
$\pi_n := P_{\xi_n}$
---
> Теорема о вероятности траектории
---
# Теорема
$p(\xi_0 = a_0, \xi_1 = a_1, ..., \xi_n = a_n) = \pi_0(a_0) p_{a_0 a_1} p_{a_1 a_2} ... p_{a_{n-1} a_n}$
---
> Теорема существования цепи маркова
---
# Теорема
Если заданы $\pi_0: Y \to [0, 1]$, такая что $\sum_{y \in Y} \pi_0 (y) = 1$ и $p: Y \times Y \to [0, 1]$ , такие что $\sum_{y \in Y} p_{ay} = 1 \forall a \in Y$
то существует $(\Omega, \mc{F}, \mc{P})$ и цепь маркова $\xi_0, \xi_1, ... : \Omega \to Y$ с начальным распределением $\pi_0$ и вероятность перехода $p_{ab}$
---
> Теорема о формуле распределения состояний цепи на n-ном шаге
---
# Теорема
$\pi_n = \pi_0 \cdot P^n$, где $P$ - матрица перехода
## Доказательство
$\pi_n(a) = P(\xi_n= a) = \sum_{y \in Y} P(\xi_{n-1} = y) p_{ya} = \sum_{y \in Y} \pi_{n-1}(y) p_{ya}$
---
> Распределение на фазовом пространстве
---
# Определение
$\pi$ - распределение на $Y$, если $\pi: Y \to [0, 1]$ и $\sum_{y \in Y} \pi(y) = 1$
# Определение
$\pi$ - стационарное распределение цепи Маркова если $\pi P= \pi$, $P$ - матрица переходов

# Пример
Есть ли стационарное распределение у случайного блуждания, пусть есть:
$\pi(y) = \frac{1}{2}\pi(y + 1) + \frac{1}{2} \pi (y - 1) \Rightarrow \pi(y + 1) - \pi (y) = \pi (y) - \pi(y - 1)$ 
Пусть это константа
$\pi(y+n) = \pi(y) + cn \geq cn$ если $c > 0$, то это больше 1 при больших $n$
В то же время это $\leq 1 + cn$, что отрицательно если $c < 0$
Тогда $c = 0$, то есть $\pi(y) = const$, но на $\Z$ не бывает равномерного распределения
То есть стационарное распределение существует не всегда
---
> Эргодическая теорема Маркова
---
# Теорема
Пусть $Y$-конечно $p_{a, b} > 0$ $\forall a, b \in Y$. Тогда существует единственное стационарное распределение $\pi$, причем $\pi(b) = \lim_{n \to \infty} p_{ab}(n)$, более того $\exists c > 0$ и $q \in (0, 1)$ такое что $$|\pi(b) - p_{ab}(n)| \leq cq^n \quad \forall a,b \in Y$$
# Доказательство
Пусть $\#Y = m$. Возьмем в $\R^m$ норму $||x|| = |x_1| + ... + |x_m|$
$K := \{x \in \R^m: ||x|| = 1\}$ - единичная сфера
$\tilde K := K \cap \{x_1, ..., x_n \geq 0\}$ - замкнутое подмноежство $\R^m$ - полное пространство
$T: \tilde K \to \tilde K$ $Tx := x P$ - стационарное распределение - неподвижная точка для отображения $T$
проверим, что $T$ - сжатие, то есть $||Tx - Ty || \leq \lambda || x- y||$ для некоторого $\lambda \in (0, 1)$. Пусть $z = x - y$ Пусть $\delta := \min p_{ij} >0$
$$(Tz)_j = \sum_{i=1}^m p_{ij} z_i = \sum_{i=1}^m (p_{ij} - \delta) z_i + \delta \sum_{i=1}^m z_i = \sum_{i=1}^m (p_{ij} - \delta) z_i$$
$$||Tz|| = \sum_{j=1}^m |(Tz)_j| = \sum | \sum_{i=1}^m (p_{ij} - \delta) z_i| \leq \sum_{j=1}^m \sum_{i=1}^m (p_{ij} - \delta) |z_i|$$
$$\leq \sum_{i=1}^m |z_i| \sum_{j=1}^m (p_{ij} - \delta) = (1-m\delta) \sum_{i=1}^m |z_i| = (1- m\delta)||z||$$
Следовательно по теореме банаха есть единственная неподвижная точкаб если стартовать с какого-то распределения и начать его итерировать то результат сходится к неподвижной точке. $p_{ab}(n)$ - распределение при старте из $a$ на $n$-ом шаге и в качестве $q$ пойдет $\lambda$
---
> Виды состояний цепи маркова
---
# Определение
Состояние $b$ достижимо из состояния $a$, если для некоторого $n \in \N \quad p_{ab}(n) > 0$

Состояния $a$ и $b$ сообщающиеся, если $a$ достижимо из $b$, а $b$ достижимо из $a$.

Состояние $a$ существенное, если для каждого достижимого из $a$ состояния $b$ $a$ и $b$ будут сообщающиеся

# Обозначения
$f_a(n) := P(\xi_n = a \mid \xi_{n-1} \not = a ... \xi_1 \not = a, \xi_0 = a)$ - вероятность того что возврат случился на $n$  -ном шаге
---
> Возвратное состояние
---
# Определение
Если $\sum_{n=1}^\infty f_a(n) = 1$, то $a$ возвратное состояние
иначе невозвратное

# Обозначение
$F_a := \sum_{n=1}^\infty f_a(n)$ - вероятность возврата
---
> Нулевое состояние
---
# Определение
Если $p_{aa}(n) \to_{n \to \infty} 0$, то $a$ - нулевое состояние
---
> Критерий возвратности
---
# Теорема
$a$ - возвратная $\iff$ $\sum_{n=1}^\infty p_{aa}(n)$ расходится
Если $a$-невозвратное, то $F_a = \frac{P_a}{1 + P_a}$, где $P_a = \sum_{n=1}^\infty p_{aa}(n)$ 
## Доказательство
Положим $p_{aa}(0) = 1$ и $f_a(0) = 0$
$F(t) := \sum_{n=0}^\infty f_a(n) t^n$
$P(t) = \sum_{n=0}^\infty p_{aa}(n) t^n$ 
$p_{aa}(n) = f_a(n) + f_a(n-1) p_{aa}(1) + ... = \sum_{k=0}^n f_a(k) p_{aa} (n - k)$ при $n > 0$
$P(T) F(T) = P(T) + 1$ 
$F(t) = 1 - \frac{1}{P(T)}$
$$\lim F(t)_{t \to 1-} F(t) = 1 - \lim_{t \to 1-} \frac{1}{P(t)}$$
Если $1 + P_a = \sum_{n=0}^\infty < +\infty$, то $\lim_{t \to 1-} P(t) = P_a + 1$ 
При бесконечности это бесконечность
# Следствие
Невозвратное состояние обязательно нулевое
## Доказательство
Члены ряда стремятся с нулю
---
> Теорема солидарности
---
# Теорема
Сообщающиеся состояния возвратны/невозвратны (нулевые/ненулевые) одновременно.
# Доказательство
$a$ и $b$ сообщающиеся, тогда $\exists i, j$ $p_{ab}(i) > 0$, $p_{ba}(j) > 0$
$$p_{bb}(i+j+n) \geq p_{ba}(j) p_{aa}(n) p_{ab} (i)$$
$$p_{aa}(n) \leq \frac{1}{p_{ab}(i) p_{bb}(j)}p_{bb}(i +j + n)$$
Тогда если $p_{bb}(n) \to 0$, то $p_{bb}(i + j + n) \to 0$  $\Rightarrow p_{aa}(n ) \to 0$

$$\sum_{n=1}^\infty p_{aa} (n ) \leq \frac{1}{p_{ab}(i) p_{ba} (j)} \sum_{n=1}^\infty p_{bb}(i+j+n)$$ если $b$ невозвратное, то и $a$ невозвратное
---

### Случайные блуждания
> Случайное блуждания в целые соседние точки
---
# Определение
$p \in (0, 1)$, случайное блуждание в соседние целые точки - p в одну $1 - p$ другое
---
> Теорема о возвратности случайного блуждании
---
# Теорема
Такое случайное блуждания возвратно $\iff p = \frac{1}{2}$
## Доказательство
$C_{2n}^n \sim \frac{4^n}{\sqrt{\pi n}} \leq 4^n$ 
$p_{00}(n) = 0$ если $n$-нечетно
$p_{00}(2n) = С_{2n}^n p^n (1-p)^n$
$$\sum_{n=1}^\infty p_{0, 0}(n) = \sum_{n=1}^\infty C_{2n}^n p^n (1- p)^n$$
Если $p \not = \frac{1}{2}$
$$C_{2n}^n p^n (1-p)^n \leq 4^n p^n (1-p)^n = (4p(1-p))^n < 1$$
Следовательно ряд сходится
Если $p = \frac{1}{2}$ $$\frac{C^n_{2n}}{4^n} \sim \frac{1}{\sqrt{\pi n}}$$
Ряд расходится. Следовательно возвратно
---
> Произвольное симметричное случайное блуждание
---
# Определение
$\xi_1, \xi_2, ...$ независимые одинаково распределенные случайные величины симметричные $P(\xi_1 = k) = P(\xi_1 = -k)$ 
$S_n = \xi_1 + \xi_2 + ... + \xi_n$  - случайное блуждание
---
> Теорема о возвратности произвольного симметричного случайного блуждания
---
# Теорема
Если $E|\xi_1| < +\infty$, то такое произвольное симметричное блуждание возвратно.
# Доказательство
Надо доказать что $\sum_{n=1}^\infty P(S_n = 0) = +\infty$ 
$G(z) := \sum_{k \in Z} P(\xi_1 = k) z^k$ при $|z| = 1$ абсолютно сходится
$G_{S_n}(z) = G^n(z)$ 
$P(S_n = 0)$ - коэффициент при $z^0$ у функции посчитае мвычет $G_{S_n}(z) = \frac{1}{2\pi} \int_{|z| = 1} \frac{G^n(z)}{z} dz$ 
Посчитаем сумму $0 < x < 1$ $$\sum_{n=0}^\infty P(S_n = 0) x^n = \frac{1}{2\pi i} \sum_{n=0}^\infty x^n \int_{|z| = 1|} \frac{G^n(z)}{z} dz = \frac{1}{2\pi i} \frac{1}{z} \sum_{n=0}^\infty x^n G^n(z) dz$$
$$= \frac{1}{2\pi i} \int_{|z| = 1} \frac{dz}{z(1 - xG(z))} = \frac{1}{2\pi} \int_{-\pi}^\pi\frac{dt}{ 1- xG(e^{it})}$$
$$= \frac{1}{\pi} \int_{0}^\pi \frac{dt}{1 - x(1 + o(t))} \geq \frac{1}{\pi}\int_{0}^\pi \frac{dt}{ 1 - x(1 - ct)}$$
Это логарифм который уходит в бесконечность при $x \to 1$
---
> Торема о нулевости произвольного симметричного случайного блуждания
---
# Замечание
$S_{n} := \xi_1 + \xi_2 + ... + \xi_n$ произвольное симметричное случайное блуждание
$G$ - производящая функция $\xi_1$ 
$G_n(z) := G_{S_{n}}(z) = G^{n}(z)$ jj
$P(S_n = 0) =$ коэффициент при $z^0$ у $G^n$ $$= \frac{1}{2\pi i} \int_{|z| = 1} \frac{G^n(z)}{z} = \frac{1}{2\pi} \int_{0}^{2\pi}G^n(e^{it}) dt$$$$|G(e^{it}) | =  |\sum_{k=\Z} P(\xi_1 = k) e^{ikt}| \leq \sum P(\xi_1 = k) = 1$$
Если получим строгое неравенство, то будет геом прогрессией стремящийся к 0.
Равенство $\iff$ все arg равны $\iff$ для $P(\xi_1 = k) > 0$ $kt = 2\pi m_k + \alpha$
$\overline{k}t = 2\pi\overline{m} + \alpha$
$t = \frac{2\pi (m - \overline{m})}{k - \overline{k}}$
таких $k$ лишь счетное множество
Тогда оно 0 почти везде
Следовательно блуждание нулевое
---
> Теорема Пойя о блуждании
---
# Определение
Случайное блуждание по $\Z^d$. С равной вероятностью можем пойти в любую из соседних точек
# Теорема
Такое случайное блуждание возвратно $\iff d = 1$ или $d = 2$
## Доказательство
$d = 2$
Проведем оси $y = x$ и $y = -x$ относительно позиции в которым мы находимся. Будем смотреть на проекции на эти оси
$\xi_k$ смещение на оси абцис
$\overline \xi_k$ смешение на оси ординаты

$\eta_k$ и $\overline{\eta_k}$ независимы (значения на новых осях)
$P(S_n = 0) = P(\sum \eta_k = 0, \sum_{k=1}^n \eta_k = 0) = P(\sum \eta_k = 0) P (\sum_{k=1}^n \overline\eta_k = 0) = (\frac{C_{2n}^n}{4^n})^2$   
А такое расходится, следовательно оно возвратно
$d = 3$. Посчитаем вероятность $p_{00}(2n) = \sum_{i + j \leq n}\binom{2n}{i, i, j, j, n - i -j, n - i - j} \frac{1}{6^{2n}} = \sum_{i + j \leq n} C_{2n}^n \binom{n}{i, j, n n - i -j}^2$ 
Обычная сумма это $3^n$, сумма квадратов тогда:
$$\leq C_{2n}^n \max_{i +j \leq n} \binom{n}{i, j, n - i - j} 3^n$$
Оно максимально когда они от друг друга не более чем на 1
$$\sim C_{2n}^n \frac{n!}{(\frac{n}{3}!)^3} 3^n \sim \frac{3^{2n} 3\sqrt{3}}{2\pi n} C_{2n}^n$$
Поделить на $^{2n}$  и сходится слудовательно нет возрастности
$d = 3 + k, k \geq 1$
Тогда $Z^{3}$ возвратна, а она не вовзратнај
---


