"""
自定义模块
注意：每个Python文件都可以作为一个模块，模块的民资就是文件的名字，也就是说自定义模块名必须和表示符命名规则
"""
# 导入自定义模块使用
import my_module
my_module.test(1, 2)

# from my_module import test
# test(1, 2)


"""
导入不同模块的同名功能
    当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能的时候，调用的是后面打偶的模块里的功能
"""
from module1 import my_test
from module2 import my_test

my_test(1, 1)


# __main__变量
from my_module import test

# __all__变量
# 如果一个模块文件中有`__all__`变量，当使用`from xxx import *`导入时，只能导入这个列表中的元素
from my_module import *
testa(1, 2)
# testb(2, 1)     # 这个就会报错






