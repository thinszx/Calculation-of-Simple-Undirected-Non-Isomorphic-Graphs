# Calculation-of-Simple-Undirected-Non-Isomorphic-Graphs
信安数基大作业，闲来无事发到gtihub上

Term project of my Mathematical Foundations in Information Security course. Uploading this code because I'm trying to archive all my projects on GitHub from now on and this project is a flag.

# 原理/Theory
1. 计算 $n$ 元对称群 $S_n$ 的阶，即为 $|S_n|=n!$

2. 进行和式分解，如

$$
\begin{aligned}
4 &=1+1+1+1 \\\\
&=2+1+1 \\\\
&=2+2 \\\\
&=3+1 \\\\
\end{aligned}
$$

计算每种置换类型的个数，对 $n$ 次对称群 $S_n$，有

$$\phi(g)=\frac{n !}{1^{\lambda_{1}} \cdot \lambda_{1} ! \cdot 2^{\lambda_{2}} \cdot \lambda_{2} ! \cdots n^{\lambda_{n}} \cdot \lambda_{n} !}$$

其中，$\phi(g) = |(1)^{\lambda_1} (2)^{\lambda_2} \cdots (n)^{\lambda_n}|$

3. 利用Burnside公式求解

$$N = \frac{1}{n!}\sum_{g \in S_n} {\frac{n!}{1^{\lambda_1} \cdot \lambda_1! \cdot 2^{\lambda_2} \cdot \lambda_2! \cdots n^{\lambda_n} \cdot \lambda_n!} \cdot 2^{N_g}}$$

其中， $N_{g}=\frac{1}{o(g)} \sum\limits_{k=1}^{o(g)}\left(C_{\lambda_{k_1}}^{2}+\lambda_{k_2}\right)$，$g^k$ 的类型为 $1^{k_1}2^{k_2} \cdots n^{k_n}$， $o(g)$ 为 $g$ 的阶

注：若 $\lambda_{k_1} < 2$，${C^2_{\lambda_{k_1}}}$ 取 $0$
