# num = 100
# def testA():
#     print(num)
#
# def testB():
#     print(num)
#
# testA()
# testB()
# print(num)


# 如果testB()函数需要修改变量num的值为200
num = 100


def test_a():
    print(num)


def test_b():
    num = 200
    print(num)


test_a()                            # 结果：100
test_b()                            # 结果：200
print(f'全局变量num = {num}')       # 结果：全局变量num = 100
