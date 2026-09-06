# 使用while嵌套循环打印九九乘法表
# 1、控制行的循环（外）
# 一共有9行，所以定义一个i，i <= 9
# 2、控制每一行输出的循环（内）  j <= i
# 找规律发现，每一行的内容：j * i

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t", end='')
        j += 1
    i += 1
    # print("\t")
    print()
