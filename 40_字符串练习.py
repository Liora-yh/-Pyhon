# 给定一个字符串："itheima itcast boxuegu"
# 1.统计字符串内有多少个"it"字符
# 2.将字符串内的空格，全部替换为字符: "|"
# 3.并按照"|"进行字符串分割，得到列表
my_str = "itheima itcast boxuegu"

print(my_str.count("it"))

num = my_str.count("it")
print(f"字符串{my_str}中有{num}个it字符")

new_my_str = my_str.replace(" ","|")
print(new_my_str)
print(f"字符串{my_str}被替换空格后，结果是：{new_my_str}")

new_my_str_list = new_my_str.split("|")
print(f"字符串{new_my_str}按照 | 分割后结果是：{new_my_str.split}")