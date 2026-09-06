# 有一个列表，内容是：[21, 25, 21, 23, 22, 20]，记录失物是一批学生的年龄
# 1. 定义这个列表，并用变量接收它
# 2. 追加一个数字31，到列表的尾部
# 3. 追加一个新列表[29, 33, 30]，到列表的尾部
# 4. 取出第一个元素(即21)
# 5. 取出最后一个元素(即30)
# 6. 查找元素31，在列表中的下标位置

age = [21, 25, 21, 23, 22, 20]

age.append(31)
print(age)

age.extend([29, 33, 30])
print(age)

# element1 = age.pop(0)
# print(element1)
num1 = age[0]
print(num1)

# element2 = age.pop(8)
# print(element2)
num2 = age[-1]
print(num2)

print(age.index(31))
