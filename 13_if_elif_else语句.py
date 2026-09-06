height = int(input("请输入你的身高（cm）："))
# vip_level = int(input("请输入你的VIP等级（1-5）："))
if height < 120:
    print("身高小于120cm，可以免费。")
# elif vip_level > 3:
elif int(input("请输入你的VIP等级（1-5）：")) > 3:
    print("vip级别大于3，可以免费。")
else:
    print("不好意思，所有条件不满足，需要购票10元。")

# 示例 if嵌套
num1 = int(input("请输入第一次猜想的数字："))
if num1 != 10:
    num2 = int(input("不对，再猜一次："))
    if num2 != 10:
        num3 = int(input("不对，再猜最后一次："))
        if num3 != 10:
            print("Sorry，全部猜错啦，我想的是：10")
        else:
            print("恭喜你猜对啦！")
    else:
        print("恭喜你猜对啦！")
else:
    print("恭喜你猜对啦！")

# 还可以有下面一种写法
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你猜对啦！")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对啦！")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜你猜对啦！")
else:
    print("Sorry，全部猜错啦，我想的是：10")
