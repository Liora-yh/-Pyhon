from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(['中国', '美国', '英国', '韩国'])
bar.add_yaxis("GDP", [30, 20, 10, 15], label_opts=LabelOpts(position="right"))     # 把数值标签放在右侧

# 反转x、y轴
bar.reversal_axis()


bar.render("基础柱状图.html")