print("欢迎来到动物园！")
if int(input("请输入您的身高：")) > 120:
    print("您的身高大于120cm，不可以免费")
    print("不过如果您的vip等级高于3，可以免费游玩")

    if int(input("请输入您的vip等级：")) > 3:
        print("您的vip等级高于3，可以免费游玩")
    else:
        print("Sorry，您需要补票10元")
else:
    print("欢迎你小朋友，可以免费游玩！")



# 示例1：公司发礼物
age = 20
entry_time = 4
grade = 2
if (age >= 18) & (age < 30):
    if (entry_time > 2) | (grade > 3):
        print("你可以领取礼物！")
    else:
        print("很遗憾！你不可以领取礼物！！")
else:
    print("很遗憾！你不可以领取礼物！！")


# 示例2：定义一个数字（1~10，随机产生），通过3次判断来才出数字
# 要求：1、通过3层嵌套来实现判断
#      2、每次猜不中，会提示大了或小了
# 提示：通过以下代码，可以定义一个变量unm，变量内存储随机数字
# import random
# num = random.randint(1, 10)
import random
num = random.randint(1, 10)
print(num)
num1 = int(input("请输入你所猜的数字："))
if num1 == num:
    print("恭喜你第一次就猜对啦！")
else:
    if num1 < num:
        print("你猜小了！")
    else:
        print("你猜大了！")
    num2 = int(input("再猜一遍："))
    if num2 == num:
        print("恭喜你第二次猜对啦！")
    else:
        if num2 < num:
            print("你猜小了！")
        else:
            print("你猜大了！")
        num3 = int(input("还是没猜对，最后再猜一遍："))
        if num3 == num:
            print("恭喜你最后一次猜对啦！")
        else:
            print("三次机会用完了，没有猜中！正确的数字是：%s" % num)
