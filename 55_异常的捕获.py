try:
    f = open("linux", "r")
except:
    print("出现异常了，因为文件不存在")
    f = open("linux", "w")

# 捕获指定异常
    # 如果尝试执行的代码的异常类型与要补货的异常类型不一致，则无法捕获异常
    # 一般try下方只放一行尝试执行的代码
try:
    print(name)
    # 1 / 0
except NameError as e:
    print("出现了变量未定义的异常")    # 若是1 / 0 就不会捕获到异常，因为类型不一样
    # 1 / 0 是ZeroDivisionError异常错误
    print(e)

# 捕获多个异常
try:
    print(1/0)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常错误")


# 捕获所有的异常
try:
    1 / 0
    # print(name)
except Exception as e:
    print("出现异常")

# 异常else：表示的是如果没有异常，所要执行的代码
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("我是else，是没有异常的时候所执行的代码")


# 异常的finally：表示的是无论是否出现异常都要执行的代码
try:
    f = open("test.txt", "r")
except Exception as e:
    f = open("test.txt", "w")
else:
    print("没有异常，真开心")
finally:
    f.close()
