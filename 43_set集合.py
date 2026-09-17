# 集合不支持下标索引
# 定义集合
my_set = {"落雨花", "luoyuhua", "罗玉华", "luoyuhua"}
my_set_empty = set()  # 定义一个空集合
print(f"my_set的内容是：{my_set}, 类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}, 类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("新元素")
print(f"my_set的内容是：{my_set}, 类型是：{type(my_set)}")

# 移除元素
my_set.remove("新元素")
print(f"my_set的内容是：{my_set}, 类型是：{type(my_set)}")

# 随机取出一个元素
element = my_set.pop()
print(f"随机取出的元素是：{element}, 剩余元素是：{my_set}, 类型是：{type(my_set)}")

# 清空集合
my_set.clear()
print(f"my_set的内容是：{my_set}, 类型是：{type(my_set)}")

# 取两个集合的差集
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.difference(set2)
print(f"set1和set2的差集是：{set3}")
print(f"set1和set2的差集是：{set1 - set2}")
print(f'原来的set1是：{set1}, 原来的set2是：{set2}')

# 消除两个集合的差集
set1.difference_update(set2)
print(f"消除差集后的set1是：{set1}, 原来的set2是：{set2}")

# 合并两个集合
set4 = set1.union(set2)
print(f"合并后的set4是：{set4}, 原来的set1是：{set1}, 原来的set2是：{set2}")

# 取两个集合的交集
set5 = set1.intersection(set2)
print(f"set1和set2的交集是：{set5}, 原来的set1是：{set1}, 原来的set2是：{set2}")

# 消除两个集合的交集
set1.intersection_update(set2)
print(f"消除交集后的set1是：{set1}, 原来的set2是：{set2}")

# 统计集合的元素数量
set6 = {1, 2, 3, 4, 5, 2, 3, 4, 5}
print(f"set6的元素数量是：{len(set6)}")

# 集合的遍历
set = {1, 2, 3, 4, 5}
for element in set:
    print(f"set的元素有：{element}")