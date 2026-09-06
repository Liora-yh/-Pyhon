# 定义全局变量money name
money = 5000000
name = None

# 要求客户输入姓名
name = input("请输入您的姓名")

# 定义查询函数
def query(show_header):
    # 如果调用query()函数的话，在存款这里是不需要显示“-----查询余额-----”这个标题的
    # 所以我们需要用参数来控制
    if show_header:
        print("-----查询余额-----")
    print(f"{name}，您好，您的余额剩余：{money}元")

# 定义存款函数
def saving(num):
    global money
    money += num
    print("-----存款余额-----")
    print(f"{name}，您好，您存款{num}元成功。")

    # 调用query函数查询余额
    # 如果调用query()函数的话，在存款这里是不需要显示“-----查询余额-----”这个标题的
    # 所以我们需要用参数来控制
    query(False)

    # 或者这里不用调用函数，直接打印出money也可以


# 定义取款函数
def get_money(num):
    global money
    money -= num
    print("-----存款余额-----")
    print(f"{name}，您好，您存款{num}元成功。")

    query(False)

# 定义主菜单函数
def main():
    print("-----主菜单-----")
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return (input("请输入您的选择："))

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue   # 通过continue继续下一次循环，一进来就是回到了主菜单
    elif keyboard_input == "2":
        num = int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("程序退出！")
        break   # 通过break退出循环