def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

def compute(x, y):
    return x + y

test_func(compute)

"""
函数的定义中
    def关键字，可以定义带有名称的函数
    lambda关键字，定义匿名函数（无名称）
有名称的函数，可以基于名称重复使用
无名称的匿名函数，只可临时使用一次
"""
# lambda匿名函数
#语法：lambda 传入参数: 函数体（只能写一行）
def test_func(compute):
    result = compute(1, 2)
    print(result)

test_func(lambda x, y: x + y)