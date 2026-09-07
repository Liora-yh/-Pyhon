# 要写在函数体之前
def add(a, b):
    """
    add函数可以接受两个参数，进行两数相加的功能
    :param a: 形参a表示相加的其中一个数字
    :param b: 形参b表示相加的另一个数字
    :return: 返回值是两数相加的结果
    """
    result = a + b
    return result

r = add(1, 2)
print(r)