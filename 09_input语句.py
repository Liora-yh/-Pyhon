input("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)


# 输入数据类型
num = input("请输入电话号码：")
print("您的电话号码的类型是：", type(num))

# 数据类型转换
num2 = input("请输入您的幸运数字：")
num2 = int(num2)
print("您的幸运数字的类型是：", type(num2))
