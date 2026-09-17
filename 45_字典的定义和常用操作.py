# 字典的定义
# 定义字典字面量
# {key: value, key: value, ...}
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# 定义空字典
my_dict1 = {}
my_dict2 = dict()  # 使用dict()函数创建空字典

# 定义重复key的字典
my_dict3 = {'name': 'Alice', 'age': 25, 'name': 'Bob'}  # 后面的值会覆盖前面的值
print(f'重复key的字典的内容是：{my_dict3}')

# 从字典中基于key获取value
name = my_dict['name']   # 使用方括号获取值
age = my_dict.get('age')  # 使用get()方法获取值
print(f'从字典中获取的name是：{name}，age是：{age}')

# 定义嵌套字典
my_dict4 = {
    'name': 'Alice',
    'age': 25,
    'address': {
        'city': 'New York',
        'street': 'Main Street'
    }
}
stu_score_dict = {
    '张三': {
        '语文': 90,
        '数学': 95,
        '英语': 88
    },
    '李四': {
        '语文': 85,
        '数学': 92,
        '英语': 80
    },
    '王五': {
        '语文': 78,
        '数学': 88,
        '英语': 90
    }
}
print(f'嵌套字典的内容是：{stu_score_dict}')

# 从嵌套字典中获取数据
city = my_dict4['address']['city']  # 使用方括号获取值
street = my_dict4['address'].get('street')  # 使用get()方法获取值

# 看一下李四的语文成绩
li_si_chinese_score = stu_score_dict['李四']['语文']
print(f'李四的语文成绩是：{li_si_chinese_score}')

################ 字典的操作 ################
my_dict = {'张三': 90, '李四': 85, '王五': 78}
# 1、新增元素
my_dict['赵六'] = 88
print(f'新增元素后的字典内容是：{my_dict}')

# 2、更新元素
my_dict['张三'] = 95
print(f'更新元素后的字典内容是：{my_dict}')

# 删除元素
# del my_dict['王五']
# print(f'删除元素后的字典内容是：{my_dict}')
value = my_dict.pop('李四')
print(f'删除元素后的字典内容是：{my_dict}，删除的元素的值是：{value}')

# 获取全部的key
keys = my_dict.keys()
print(f'字典的key是：{list(keys)}')

# 遍历字典
# 方式1：通过获取全部的key来完成
for key in keys:
    print(f'字典的key是：{key}')
    print(f'字典的value是：{my_dict[key]}')

# 方式2：直接对字典通过for循环，每一次遍历都是直接得到key
for key in my_dict:
    print(f'字典的key是：{key}')
    print(f'字典的value是：{my_dict[key]}')

# 统计字典内的元素数量
count = len(my_dict)
print(f'字典内的元素数量是：{count}')

# 清空元素
my_dict.clear()
print(f'清空元素后的字典内容是：{my_dict}')