# 定义一个全局变量：money，用来记录银行卡余额（默认5000000）
# 定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
# 定义以下函数：
# 查询余额函数，存款函数，取款函数，主菜单函数
# 程序启动后要求输入客户姓名
# 查询余额、存款、取款后都会返回主菜单
# 存款、取款后，都显示一下当前余额
# 客户选择退出或者输入错误，程序会退出，否则一直运行


name = input("请输入您的姓名:")


# 定义主菜单函数
def menu():
    print("-----主菜单-----")
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")

menu()
num = int(input("请输入您的选择："))


def check_money(m):
    print("-----查询余额-----")
    print(f"{name}，您好，您的余额剩余：{m}元")


def save_money(m):
    print("-----存款-----")
    print(f"{name}，您好，您存款{m}元成功")
    check_money(money + m)


def draw_money(m):
    print("-----取款-----")
    print(f"{name}，您好，您取款{m}元成功")
    check_money(money - m)


money = 5000000
money2 = 0
if num == 1:
    check_money()
    menu()
if num == 2:
    save_money(50000)
    menu()
if num == 3:
    draw_money(50000)
    menu()
if num == 4:
    print("程序已退出！")
