# 在字符串内 包含单引号
name = " '你好' "
# 在字符串内 包含双引号
name1 = ' "你好" '
# 使用转义字符 \ 解除引号的效用
name2 = " \"你好\" "

# 字符串拼接
name3 = "小明"
print("我的名字是：" + name3 + "，我来自重庆")

# tel1 = 17338646927
# print("我的电话是：" + tel1)  会报错，因为tel1的类型不是字符串

tel2 = str(17338646927)
print("我的电话是：" + tel2)

# 占位拼接 %s
class_num = 2
avg_salary = 1000000
message = "软工%s班的同学，毕业平均工资：%s" % (class_num, avg_salary)
print(message)
print("软工%s班的同学，毕业平均工资：%s" % (class_num, avg_salary))

name4 = "传智播客"
set_up_year = 2006
stock_price = 19.99
message2 = "我是：%s，我成立于：%d，我今天的股份是：%f" % (name4, set_up_year, stock_price)
print(message2)

# 字符串格式化
print(f"我是{name4}，我成立于{set_up_year}，我今天的股份是{stock_price}")



# 股价计算小程序
name7 = "传智播客"
stock_code = "003032"
stock_price2 = 19.99
print(f"公司：{name7}，股票代码{stock_code}，当前股价{stock_price2}")

stock_price_daily_growth_factor = 1.2
growth_days = 7
stock_price3 = 71.63
print("每日增长系数是：%.1f，经过%d天的增长后，股票达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, stock_price3))