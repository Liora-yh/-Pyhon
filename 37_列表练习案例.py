# 取出列表内的偶数
# 定义一个列表，内容是：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 遍历列表，取出列表内的偶数，并存入一个新的列表对象中
# 使用while和for循环各操作一次
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
num = []
while i < len(number):
    if number[i] % 2 == 0:
        num.append(number[i])
    i += 1
print(num)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num2 = []
for x in number:
    if x % 2 == 0:
        num2.append(x)
print(num2)