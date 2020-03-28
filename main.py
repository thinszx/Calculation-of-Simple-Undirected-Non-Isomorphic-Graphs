import math

def combinations(n, m): # 计算组合数C(n, m)
    if 0 <= n < 2:
        return 0
    else:
        return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

# 将整数分解为多个简单数之和
result_list = [] # 记录所有分解结果
# 递归，相当于一个减法，减到结果为0或比0小时停止
def partition(n, start=1, result=[]):   # n为要分解的数，start自增，以达到最大值
    for i in range(start, n + 1):
        if i == n:  # 当最后一个被减数与n相同时，result中的元素和加上i刚好等于n
            result += [i]
            result_list.append(result)  # 将结果元素加入分解结果列表，以便后续统计
            return
        elif i > n:
            return
        partition(n - i, start=i, result=result + [i]) # 递归迭代求解

# =========================================================================
# # 递归，对所得到的所有分解式进行分析，得到置换分解的角标表示(m)^a(n)^b
# # 列表中的数两个为一组，记录置换分解，如列表为[1,3,2,1]
# # 实际意义为(1)^3(2)^1，表示该置换由三个1阶置换和一个2阶置换生成
# 对该递归的举例：如对于四阶置换群，4=1+1+2
# 第一层递归：start=0，result[start]=1，result.count(result[start])=2，意为该分解式中有2个1
# 第二层递归：该层start变为上层start值加上分解式中1的个数，start=0+2=2，那么此时result[start]为2，
# result.count(result[start])为1，意为该分解式中有1个2，此时已遍历到最后，跳出递归
# 结果：analysis列表为[1, 2, 2, 1]，两两一组，则4阶置换可分解为(1)^2(2)^1，即两个1阶置换和一个2阶置换
# =========================================================================
analysis_list = []
def analyze_partition(result, start=0, analysis=[]):
    # print(*result)****************************
    # 依次填入result[start]和result[start]的个数
    analysis = analysis + [result[start]] + [result.count(result[start])]
    # 当遍历到最后一种变量时，跳出递归
    if start + result.count(result[start]) == len(result):
        analysis_list.append(analysis)
        return
    # 当前分析的项不是分解式的最后一种
    elif start + result.count(result[start]) > len(result):
        return
    analyze_partition(result, \
        start = start + result.count(result[start]), analysis = analysis)

def count_permutation_group(order, analysis_list): # 返回列表，记录每种分解的置换在Sn中的个数
    # 公式为φ(g) = n! / Π (m^λm)·λm!
    # n为Sn中的n，λm为置换分解后(m)的指数，如(1)^3(2)^1中λ1=1
    phi = [] # phi即为希腊字母φ，存储每种置换分解的个数，下标与analysis_list对应
    for analysis in analysis_list:
        denominator = 1
        for i in range(0, len(analysis), 2):
            denominator *= math.pow(analysis[i], analysis[i+1]) \
                * math.factorial(analysis[i+1])
        phi.append(int(order // denominator)) # order即为n!
    return phi

def generate_higher_order(analysis): # 返回列表，记录analysis分解的高阶复合类型
    higher_order_list = []
    # 若σ = (i)^l，则σ^k的置换类型为(i/d)^dl，其中d=gcd(i, k)
    higher_order = analysis[:] # 先对analysis进行复制，防止二者指向同一对象
    higher_order_list.append(analysis)
    order = 1
    for i in range(0, len(higher_order), 2):
        order *= higher_order[i] # order为analysis所代表置换群的阶数
    # 注意，以下的循环中所用的k均为真实值，因此从2开始计数
    for k in range(2, order + 1): # k为幂数，为真实值
        for i in range(0, len(analysis), 2):
            d = math.gcd(analysis[i], k)
            higher_order[i] = analysis[i] // d
            higher_order[i+1] = analysis[i+1] * d
        tmp_list = higher_order[:] # 临时队列，防止最终结果中列表都是同一对象
        higher_order_list.append(tmp_list)
    return higher_order_list

def count_orbit(higher_order_list): # 计算每种置换及其高阶置换生成的轨道数
    order = 1 # 即为群的阶o(g)
    lambda1_list = [] # 记录各高阶生成中λ1的值
    lambda2_list = [] # 记录各高阶生成中λ2的值
    for higher_order in higher_order_list:
        lambda1 = lambda2 = 0 # λ1, λ2为高阶生成群中阶数为1和2的置换的幂
        for i in range(0, len(higher_order), 2):
            # 统计λ1, λ2
            if higher_order[i] == 1:
                lambda1 += higher_order[i+1]
            elif higher_order[i] == 2:
                lambda2 += higher_order[i+1]
        lambda1_list.append(lambda1)
        lambda2_list.append(lambda2)
    for i in range(0, len(higher_order_list[0]), 2): # 第一个元素为1阶置换
        order *= higher_order_list[0][i] # order为analysis所代表置换群的阶数
    # 计算该置换对二元置换群的轨道数
    # 公式为 [1/o(g)] * Σ [(λ1的2组合)+λ2]，Σ从1到o(g)
    orbit_num = sum(combinations(lambda1_list[i], 2) + lambda2_list[i] for i in range(0, order)) // order
    return orbit_num

def count_graphs(n, phi, orbit_num_list): # 利用Burnside引理求最终的不同构图个数
# 参数为节点数目n，count_permutation_group所求φ值列表和count_orbit求得的所有轨道数列表
    graphs_num \
    = sum(phi[i] * math.pow(2, orbit_num_list[i]) for i in range(0, len(phi))) \
         // math.factorial(n) # Burnside公式
    return graphs_num

def main():
    n = int(input("\n请输入简单无向图的节点数目：")) # n即为n元对称群Sn中的n
    while n < 0:
        n = int(input("请输入大于等于0的正整数："))

    # 第一步，计算n元对称群的阶
    print("\n第一步，计算%d元对称群的阶" % n)
    order = math.factorial(n) # 群的阶
    print("%d元对称群S%d的阶为 %d! = %d" % (n, n, n, order))

    # 第二步，将n分解为多个正整数的和，并分析分解式
    print("\n第二步，将%d分解为多个正整数的和，进而得出置换的分解类型" % n)
    partition(n) # 分解n为多个整数的和
    print("共%d种情况：" % len(result_list))
    for result in result_list: # 序列化输出结果
        print("%d=" % n + "+".join(str(x) for x in result), end="; ")

    # 分析分解式
    for result in result_list:
            analyze_partition(result)
    # 格式化输出为(m)^a(n)^b的形式，并输出相应的分解在Sn中的个数
    print("\n该置换的分解类型及各分解类型的个数为：")
    phi = count_permutation_group(order, analysis_list)
    j = 0
    for analysis in analysis_list:
        for i in range(0, len(analysis), 2):
            print('({0})^{1}'.format(analysis[i], analysis[i+1]), end="") # 同一个分解式不换行
        print("-------------", str(phi[j])) # 换行
        j += 1

    # 第三步，计算每种分解对它的二元子集作用的轨道数，分为两小步
    print("\n第三步，计算每种分解对它的二元子集{0,1}作用的轨道数")
    orbit_num_list = []
    for analysis in analysis_list:
        # 第一小步，首先计算出g, g^2, ... g^k的表达式，其中k为g=(m)^a(n)^b的阶，即|m*n|
        higher_order_list = generate_higher_order(analysis)
        # 第二小步，计算每个高阶结果的Ng
        tmp = count_orbit(higher_order_list)
        orbit_num_list.append(tmp)
    print("上述%d种分解对二元置换的轨道数为：" % len(phi))
    print(", ".join(str(x) for x in orbit_num_list))

    # 第四步，由Burnside引理计算不同构图数目
    graphs_num = count_graphs(n, phi, orbit_num_list)
    print("\n第四步，由Burnside引理计算不同构图数目")
    print("由Burnside引理，可得到置换群诱导的S%d上的等价类个数为：" % n)
    print("+".join("({0}*2^{1})".format(phi[i], orbit_num_list[i]) \
         for i in range(0, len(phi))) + (" / %d!" % n))
    print("\n所以%d阶简单无向图（不保证连通）的不同构图数目为%d\n" % (n, graphs_num))

if __name__ == '__main__':
    main()