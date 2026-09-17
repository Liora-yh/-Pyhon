"""
有如下列表对象：
    my_list = ['落雨花', '罗玉华', '罗小罗', '罗小罗', '落雨花', 'liora', 'jack', 'liora', 'jack', 'lucy']
请：
    1、定义一个空集合
    2、通过for循环遍历列表
    3、在for循环中讲列表的元素添加至集合
    4、最终得到元素去重后的集合对象，并打印输出
"""
my_set = set()  # 定义一个空集合
my_list = ['落雨花', '罗玉华', '罗小罗', '罗小罗', '落雨花', 'liora', 'jack', 'liora', 'jack', 'lucy']
for element in my_list:
    my_set.add(element)
print(f"去重后的集合对象是：{my_set}") # set集合自动去重