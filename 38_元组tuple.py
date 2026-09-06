t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")

# 定义一个单个元素的元组
# t4 = ("hello")    如果像这样定义的话，则t4的类型就是字符串，而不是元组了
# print(f"t4的类型是{type(t4)}，t4的内容是{t4}")   # 'str' hello
# 所以得在括号里面加一个逗号
t4 = ("hello", )
print(f"t4的类型是{type(t4)}，t4的内容是{t4}")


# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
# 根据下标（索引）取出数据
print(t5[0][0])  # 1

t6 = [1, 2, 'hello', 3, 4, 'hello']
# 根据index()，查找指定元素的第一个匹配项
print(t6.index('hello'))    # 2
# 统计某个数据在元组内出现的次数
print(t6.count('hello'))    # 2
# 统计元组内的元素个数
print(len(t6))      # 6



# 元组的遍历
# 1.用while循环
index = 0
while index < len(t6):
    print(f"元组的元素有：{t6[index]}")
    index += 1

# 2.用for循环
for element in t6:
    print(f"t6的元素有：{element}")
