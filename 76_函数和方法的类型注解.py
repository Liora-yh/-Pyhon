"""
函数和方法的形参类型注解语法：
def 函数方法名(形参名: 类型, 形参名: 类型, ...)
    pass
"""
def add(x: int, y: int):
    return x + y

def func(data: list):
    pass

"""
对返回值进行类型注解
def 函数方法名(形参: 类型, 形参: 类型, ...)  -> 返回值类型:
    pass
"""
def func1(data: list) -> list:
    return data




