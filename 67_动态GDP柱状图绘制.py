from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
# 读取数据
f = open("E:/Python/PythonPro/pythonProject/data/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()

# 删除第一条数据——“year,GDP,rate”
data_lines.pop(0)

# 将数据转换为字典存储，格式为：
# { 年份：[国家, gdp], [国家, gdp], [国家, gdp], ....}
# 先定义一个字典
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]        # 国家
    gdp = float(line.split(",")[2])     # GDP数据
    # 如何判断字典里面是否有key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)

# 创建时间线对象
timeline = Timeline()

# 排序年份
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前八名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])   # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)   # y轴添加GDP数据

    # 构建柱状图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))

    # 反转x轴和y轴
    bar.reversal_axis()

    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("1960-2019年全球GDP前8国家.html")



