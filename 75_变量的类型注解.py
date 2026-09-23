# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: float = 3.1415926

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"item": 11}
my_str: str = "item"

# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_set1: set[int] = {1, 2, 3}
my_tuple1: tuple[str, int, bool] = ("item", 666, True)
my_dic1: dict[str, int] = {"item": 666}

"""
注意：元组类型设置类型详细注解，需要讲每一个元素都标记出来
字典类型设置类型详细注解，需要两个类型，第一个是key第二个是value
"""


# 在注释中进行类型注解
def func():
    return 10

var_5 = random.randint(1, 10)   # type: int
var_6 = json.loads('{"name": "luoyuhua"}')   # type: dict[str, int]
var_7 = func()   # type: Student











