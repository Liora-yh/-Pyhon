my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "itheima"
my_set = {3, 1, 2, 5, 4}
my_dict = {"name": "itheima", "age": 8, "gender": "male"}

print(f'列表对象的排序结果是：{sorted(my_list)}')
print(f'元组对象的排序结果是：{sorted(my_tuple)}')
print(f'字符串对象的排序结果是：{sorted(my_str)}')
print(f'集合对象的排序结果是：{sorted(my_set, reverse=True)}')  # reverse=True表示降序排序
# 字典对象的排序结果是：['age', 'gender', 'name']
print(f'字典对象的排序结果是：{sorted(my_dict)}')