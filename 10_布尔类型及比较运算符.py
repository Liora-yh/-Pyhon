result = 10 > 5
print(f" 10 > 5 的结果是：{result}, 类型是：{type(result)}")

result2 = "itcast" == "itheima"
print(f"字符串itcast是否和itheima相等，结果是：{result2}")

# 比较运算符
# ==、!=、>、<、<=、>=
num1 = 10
num2 = 10
print(f" 10 == 10 的结果是：{num1 == num2}")

num3 = 15
print(f" 10 != 15 的结果是：{num1 == num3}")


# 示例
print("欢迎来到儿童游乐场，儿童免费，成人收费。")
a = input("请输入您的年龄：")
a = int(a)
# 还可以将19、20行的代码合并
# a = it(input("请输入您的年龄："))
if a >= 18:
    print("您已成年，游玩需要补票10元。")

print("祝您游玩愉快！")
