# 将列表内的元素依此取出进行处理
# 定义一个变量表示下标，从0开始
# 循环条件为 下标值 < 列表的元素数量
# index = 0
# while index < len(列表):
#     元素 = 列表[index]
#     (对元素进行处理)
#     index += 1

# 使用while
my_list = ["python", "java", "C++"]
index = 0
while index < len(my_list):
    element = my_list[index]
    print(f"列表的元素：{element}")
    index += 1


# 使用for循环
my_list = ["python", "java", "C++"]
for element2 in my_list:
    print(f"列表的元素有：{element2}")