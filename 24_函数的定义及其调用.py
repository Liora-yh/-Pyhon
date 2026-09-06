# 统计字符串的长度，不使用内置函数len()
str = "python"
count = 0
for i in str:
    count += 1
print(count)

# 使用函数
def my_len(data):
    count2 = 0
    for i in data:
        count2 += 1
    print(count2)

my_len(str)




# 案例1：自动查核酸
def check():
    print("您好！\n请出示您的健康码以及72小时核酸证明！")

check()

# 案例2：升级版自动查核酸
# 定义一个函数，名称任意，并接受一个参数传入(数字类型，表示体温)
# 在函数内进行体温判断(正常范围：小于等于37.5度)
def check2(temp):
    print("您好！\n请出示您的健康码以及72小时核酸证明！")
    if temp <= 37.5:
        print(f"体温测量中，您的体温是：{temp}度，体温正常请进！")
        # return True
    else:
        print(f"体温测量中，您的体温是：{temp}度，需要隔离！")

check2(38)

def add(a, b):
    result = a + b
    return result
    # 如果返回后，还想输出一句话
    # print("我完事儿了！")   此行代码不会执行
# return后面的函数体不执行
r = add(1, 2)
print(r)

# None类型
def say_hello():
    print("Hello...")

result = say_hello()
print(result)     # 结果None
print(type(result))     # 结果<class 'NoneType'>

# None可以主动使用return返回，效果等同于不写return语句
def say_hello():
    print("Hello...")
    return None

result = say_hello()
print(result)  # 结果None
print(type(result))

# None勇于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(16)
if not result:
    # 进入if表示result是None值，也就是False
    print("未成年，不可以进入")

# None用于声明无初始内容的变量
name = None
