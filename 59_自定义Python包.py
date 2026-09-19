"""
导入包：
    方式一：
        import 包名.模块名
        包名.模块名.目标
"""

"""
import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

# 方式二
from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

# 方式三
from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2
info_print1()
info_print2()

"""

# 注意必须在`__init__.py`文件中添加`__all__ = []`，控制允许导入的模块列表
from my_package import *
my_module1.info_print1()
my_module2.info_print2() # 就会报错