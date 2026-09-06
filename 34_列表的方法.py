# 1.查询功能（index）
# index就是列表对象(变量)内置的方法(函数)
# 查找指定元素在列表的下标，如果找不到，会报错ValueError
# 语法：列表.index(元素)
name_list = ['python', 'java', 'C++', 'javascript']
index = name_list.index("java")
print(index)

# 修改指定下标的元素值
# 语法：列表[下标] = 值
my_list = [1, 2, 3]
my_list[0] = 5
print(my_list)  # 结果：[5, 2, 3]

# 插入元素(insert)
# 列表.insert(下标, 元素)
# 在指定的下标位置，插入指定的元素
my_list.insert(1, 4)
print(my_list)  # [5, 4, 2, 3]

# 追加单个元素(append)
# 列表.append(元素)
# 将指定元素追加到列表的尾部
my_list.append(7)
print(my_list)  # [5, 4, 2, 3, 7]

# 追加多个元素(extend)
my_list.extend([4, 9])
print(my_list)  # [[5, 4, 2, 3, 7], [4, 9]]

# 删除元素(del/pop)
# 语法1：del 列表[下标]
# 语法2：列表.pop(下标)
del my_list[0]
print(f"列表删除元素后的结果是：{my_list}")

element = my_list.pop(0)
print(f"通过pop方法取出元素后列表内容：{my_list}，取出的元素是：{element}")
# print(my_list, element)

# 列表.remove(元素)
# 删除某元素在列表中的第一个匹配项
my_list2 = [1, 2, 3, 2, 3]
my_list2.remove(2)
print(my_list2)

# 清空列表
# 语法：列表.clear()
my_list2.clear()
print(my_list2) # 结果：[]


# 统计某元素在列表内的数量
# 语法：列表.count(元素)
my_list3 = [1, 1, 1, 2, 3, 3]
print(my_list3.count(1))

# 统计列表的元素数量
# 语法：len(列表)
print(len(my_list3))