# 坚持吃饭10天，每天吃5个鸡腿
i = 0
for i in range(1, 11):
    print(f"坚持吃饭{i}天，继续保持。")
    for j in range(1, 6):
        print(f"吃的第{j}个鸡腿")

    print("这个鸡腿好香呀！")

print(f"第{i}天吃完所有饭！")

# 用for循环打印九九乘法表
for m in range(1, 10):
    for n in range(1, m + 1):
        print(f"{n}*{m}={n * m}\t", end='')
    print()