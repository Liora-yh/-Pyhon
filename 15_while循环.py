# i = 0
# while i < 10:
#     print("Hello World!")
#     i += 1

# 示例1：求1-100的和
j = 1
sum = 0
while j <= 100:
    sum = sum + j    # 或者 sum += j
    j += 1
print("1-100累加的和是:", sum)

# 示例2：猜数字案例
# 设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
# 要求：1、无限次机会，直到猜中为止
#      2、每一次猜不中，会提示大了或小了
#      3、猜玩数字后，提示猜了几次

import random
num = random.randint(1, 100)
# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
count = 0
while flag:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("你猜中了")
        flag = False  # 设置为False就是终止循环的条件
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
print("恭喜你猜对啦，一共猜了%s次！" % count)