name = "itheima"
for x in name:
    print(x)

# 示例：数一数有几个a
# 计数可以在循环外定义一个整数类型变量来做累加计数
name2 = "itheima is a brand of itcast"
count = 0
for letter in name2:
    if letter == "a":
        count = count + 1

print("这句话里面一共有%s个a" % count)
