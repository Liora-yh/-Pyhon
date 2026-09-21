"""
数据集不太一样，看一下视频
"""
import json

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
f = open("E:/Python/PythonPro/pythonProject/data/json_tx/COVID-19_2020-02-03(CN-DATA)by_TX.json", "r", encoding="UTF-8")
data = f.read()

# JSON转Python字典
dict = json.loads(data)
# print(type(dict))
# print(dict)

# 获取areaTree里第0号元素的total key
total = dict['areaTree'][0]['total']
# print(total)

# 获取chinaDayList里的date用于x轴
# 取出列表
china_day_list = dict['chinaDayList']
x_data = []  # 存日期
y_data = []  # 存确诊人数
# 3. 循环遍历列表里的每一个字典
for item in china_day_list:
    # item 就是列表里的每一天的数据（一个字典）
    date = item['date']  # 取出这一天的日期
    confirm = item['confirm']  # 取出这一天的确诊人数

    # 把取出来的数据加到空列表里
    x_data.append(date)
    y_data.append(confirm)

# 4. 打印结果看看
print("x轴数据（日期）：", x_data)
print("y轴数据（确诊）：", y_data)

# 生成图表
line = Line()
line.add_xaxis(x_data)
line.add_yaxis("确诊人数", y_data, label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts=TitleOpts(title="中国确诊人数", pos_left="center")
)
line.render("疫情病例案例.html")
f.close()





