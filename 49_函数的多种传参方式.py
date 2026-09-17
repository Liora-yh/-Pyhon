def user_info(name, age, gender):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}")

# 1、位置传参
"""
位置传参：调用函数时根据函数定义的参数位置来传递参数
    注意！传递的参数和定义的参数的顺序及个数必须一致
"""
user_info('落雨花', 21, '女')

# 2、关键字传参
"""
关键字参数：函数调用时通过“键=值”的形式传递参数
    作用：可以让函数更加清晰、容易使用，同事也清除了参数的顺序需求
    注意！函数调用时，如果有位置参数，位置参数必须在关键字参数的前面，但关键字参数直接不存在先后顺序
"""
user_info(name='罗玉华', age=20, gender='女')
user_info(age=21, name='罗小罗', gender='女')
user_info('罗小华', gender='女', age=19)

# 3、缺省传参
"""
缺省参数也叫默认参数，在函数定义时为参数指定默认值，调用时可以不传递该参数
（注意：所有位置参数必须出现在默认参数前面，包括函数的定义和调用
       函数调用时，如果为缺省参数传值则修改默认参数值，否则使用这个默认值）值
       设置默认值的时候，必须要在最后面，比如name='XX', age, gender就会报错）
"""
def user_info(name, age, gender='男'):
    print(f"姓名：{name}，年龄：{age}，性别：{gender}")
user_info('天天', 21)
user_info('小明', 21, gender='女')

"""
不定长参数（也叫可变参数）：用于不确定调用而癫时候会传递多少个参数（不传参也可以）的场景
    作用：当调用函数时不确定参数个数时，可以使用不定长参数
在函数定义时使用*args和**kwargs来接收不确定数量的参数
    *args：接收位置参数，以元组的形式存储
    **kwargs：接收关键字参数，以字典的形式存储
"""
# 4、不定长传参 - 位置不定长，*号
# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是位置传递
def user_info(*args):
    print(f'agrs参数的类型是：{type(args)}，内容是：{args}')
    # print(f"姓名：{args[0]}，年龄：{args[1]}，性别：{args[2]}")
# user_info('小明', 21, '男')
user_info(1, 2, 3, '小明', '男孩')


# 4、不定长传参 - 关键字不定长，**号
# 参数是“键=值”形式的情况下，所有的“键=值”都会吧kwargs接受，同事会根据“键=值”组成字典
def user_info(**kwargs):
    print(f'kwargs参数的类型是：{type(kwargs)}，内容是：{kwargs}')
    # print(f"姓名：{kwargs['name']}，年龄：{kwargs['age']}，性别：{kwargs['gender']}")
user_info(name='小明', age=21, gender='男')

