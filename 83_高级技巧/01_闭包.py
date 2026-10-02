# 简单闭包
def outer(logo):

    def inner(msg):
        print(f"<{logo}><{msg}><{logo}>")

    return inner

fn1 = outer("落雨花")
fn1("Python")
fn1("hahahaha")


def outer2(num1):

    def inner2(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner2

fn = outer2(10)
fn(10)
fn(10)


def account_create(initial_amount=0):

    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款： +{num}，余额账户：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款： -{num}，余额账户：{initial_amount}")

    return atm

atm = account_create(1000)
atm(100)
atm(200)
atm(100, deposit=False)
