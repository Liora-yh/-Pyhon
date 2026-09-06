name = "python"
# 从前往后，下标从0开始
# 从后往前，下标从-1开始
print(name[0])      # p
print(name[-1])     # n

# 字符串是一个无法修改的数据容器
# 所以：1、修改指定下标的字符    （如：字符串[0] = 'a'）
#      2、移除特定下标的字符    （如：del字符串[0]、字符串.remove()、字符串.pop()等）
#      3、追加字符等           （如：字符串：append()）
# 以上操作均不无法完成，如果必须要做，只能得到一个新字符串


name2 = "java and python"
# index方法
print(name2.index("and"))   # 5

# replace方法
# 语法：字符串.replace(字符1, 字符2)
# 将字符串内的全部字符1替换为字符2
# 注意：不是修改字符串本身，而是得到了一个新的字符串
new_name2 = name2.replace("a", "A")
print(f"将字符串{name2}进行替换后得到{new_name2}")

# split方法
# 语法：字符串.split(分隔符字符串)
# 按照制定的丰富字符串，将字符串划分为多个字符串
new_name3 = name2.split("p")
print(f"将字符串{name2}进行分割后得到{new_name3}，类型是{type(new_name3)}")

# strip方法
# 1.去前后空格 语法：字符串.strip()
str = "   java and python  "
print(str.strip())
# 2.去前后指定字符串 语法：字符串.strip(字符串)
str = "12java and python21"
print(str.strip("12"))    # 注意，传入的是"12"，其实就是："1"和"2"都会移除，是按照单个字符

# 统计字符串中某字符出现的次数  count
print(name2.count("a"))

# 统计字符串的长度  len
print(len(name2))
