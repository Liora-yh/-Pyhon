# 对list进行切片，从1开始，4结束，步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]  # 步长默认为1，可以省略不写
print(f"切片结果是：{result1}")  # [1, 2, 3]

# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(f"切片结果是：{result2}")  # (0, 1, 2, 3, 4, 5, 6)

# 对str进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]
print(f"切片结果是：{result3}")   # 0246

# 对列表进行切片，从3开始，到2结束，步长-1
my_list = [0, 2, 3, 5, 8, 4, 9]
result4 = my_list[3:2:-1]
print(f"切片结果是：{result4}")  # [5]

# 对tuple进行切片，从尾开始，到头结束，步长-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result5 = my_tuple[::-2]
print(f"切片结果是：{result5}")  # (6, 4, 2, 0)