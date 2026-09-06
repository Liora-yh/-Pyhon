# 将数值类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

# 将字符串转换成数字
num = int("11")
print(type(num), num)

# 错误示例，想要将字符串转换成数字，必须要求字符串内的内容都为数字
num2 = int("罗嘉意")
print(type(num2), num2)