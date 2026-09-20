from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 99),
    ("重庆市", 199),
    ("上海市", 299),
    ("湖南省", 9),
    ("台湾省", 199),
    ("安徽市", 499),
    ("广东省", 399),
    ("湖北省", 599)
]
map.add("地图", data, "china")

# 绘图
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 599, "label": "100-599", "color": "#990033"}
        ]
    )
)
map.render()
