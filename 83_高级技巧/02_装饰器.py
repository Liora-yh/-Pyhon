# def sleep():
#     import random
#     import time
#     print("睡眠中...")
#     time.sleep(random.randint(1, 5))

"""
    希望给sleep函数，增加一个功能：
        1、在调用sleep前输出：我要睡觉了
        2、在调用sleep后输出：我起床了
"""

# 写法一
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner
def sleep():
    import random
    import time
    print("睡眠中...")
    time.sleep(random.randint(1, 5))

fn = outer(sleep)
fn()


# 写法二
def outer2(func):
    def inner2():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner2

@outer2     # 使用@outer2装饰器，等价于fn = outer2(sleep2)
def sleep2():
    import random
    import time
    print("睡眠中...")
    time.sleep(random.randint(1, 5))

sleep2()