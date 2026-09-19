import time

# 使用import导入time模块使用sleep功能（函数）
print("你好")
time.sleep(10)  # 通过 . 可以引用模块里的所有功能（类、函数、变量等）
print("我好")

"""
    from 模块名 import 功能名 -------这是针对某一个具体的功能去使用
    功能名()
"""
from time import sleep
print("开始")
sleep(10)
print("结束")


"""
    from 模块名 import * -------导入所有的功能
    功能名()
"""
from time import *
print("开始")
sleep(10)
print("结束")

"""
    模块别名
        import 模块名 as 别名
    功能别名
        from 模块名 import 功能 as 别名
"""