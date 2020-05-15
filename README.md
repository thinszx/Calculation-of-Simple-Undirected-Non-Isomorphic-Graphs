# Calculation-of-Simple-Undirected-Non-Isomorphic-Graphs
信安数基大作业，闲来无事发到gtihub上

Term project of my Mathematical Foundations in Information Security course. Uploading this code because I'm trying to archive all my projects on GitHub from now on and this project is a flag.

# 原理/Theory
1. 计算![](https://www.zhihu.com/equation?tex=n)元对称群![](https://www.zhihu.com/equation?tex=S_n)的阶，即为

![](https://www.zhihu.com/equation?tex=%7cS_n%7c%3dn!)

2. 进行和式分解，如

![](https://www.zhihu.com/equation?tex=%5cbegin%7baligned%7d4%26%3d1%2b1%2b1%2b1%5c%5c%26%3d2%2b1%2b1%5c%5c%26%3d2%2b2%5c%5c%26%3d3%2b1%5cend%7baligned%7d)

3. 计算每种置换类型的个数
对![](https://www.zhihu.com/equation?tex=n)次对称群![](https://www.zhihu.com/equation?tex=S_n)，有

![](https://www.zhihu.com/equation?tex=%5cphi(g)+%3d+%5cfrac%7bn!%7d%7b1%5e%7b%5clambda_1%7d+%5ccdot+%5clambda_1!+%5ccdot+2%5e%7b%5clambda_2%7d+%5ccdot+%5clambda_2!+%5ccdots+n%5e%7b%5clambda_n%7d+%5ccdot+%5clambda_n!%7d)

其中，

![](https://www.zhihu.com/equation?tex=%5cphi(g)+%3d+%7c(1)%5e%7b%5clambda_1%7d+(2)%5e%7b%5clambda_2%7d+%5ccdots+(n)%5e%7b%5clambda_n%7d%7c)

4. 利用Burnside公式求解

![](https://www.zhihu.com/equation?tex=N+%3d+%5cfrac%7b1%7d%7bn!%7d%5csum_%7bg+%5cin+S_n%7d+%7b%5cfrac%7bn!%7d%7b1%5e%7b%5clambda_1%7d+%5ccdot+%5clambda_1!+%5ccdot+2%5e%7b%5clambda_2%7d+%5ccdot+%5clambda_2!+%5ccdots+n%5e%7b%5clambda_n%7d+%5ccdot+%5clambda_n!%7d+%5ccdot+2%5e%7bN_g%7d%7d)

其中

![](https://www.zhihu.com/equation?tex=N_g+%3d+%5cfrac%7b1%7d%7bo(g)%7d+%5csum%5e%7bo(g)%7d_%7bk%3d1%7d%7b(C%5e2_%7b%5clambda_%7bk1%7d%7d+%2b+%5clambda_%7bk_2%7d)%7d)

![](https://www.zhihu.com/equation?tex=g^k)的类型为![](https://www.zhihu.com/equation?tex=1%5e%7bk_1%7d2%5e%7bk_2%7d+%5ccdots+n%5e%7bk_n%7d)，![](https://www.zhihu.com/equation?tex=o(g))为![](https://www.zhihu.com/equation?tex=g)的阶

注：若![](https://www.zhihu.com/equation?tex=%5clambda_%7bk1%7d+%3c+2)，![](https://www.zhihu.com/equation?tex=%7bC%5e2_%7b%5clambda_%7bk1%7d%7d%7d)取![](https://www.zhihu.com/equation?tex=0)
