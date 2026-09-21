from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar1.set_global_opts(legend_opts=LegendOpts(is_show=False))

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
bar2.set_global_opts(legend_opts=LegendOpts(is_show=False))

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [70, 40, 30], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
bar3.set_global_opts(legend_opts=LegendOpts(is_show=False)) # 隐藏图例

# 创建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT}      # 设置主题
)

timeline.add(bar1, "2021年GDP")
timeline.add(bar2, "2022年GDP")
timeline.add(bar3, "2023年GDP")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,     # 自动播放时间间隔，单位毫秒
    is_timeline_show=True,  # 是否自动播放的时候，显示时间戳
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环自动播放
)

# 通过时间线绘图
timeline.render("基础柱状图-时间线.html")
