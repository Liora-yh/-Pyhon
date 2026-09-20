"""
创建一个自定义包，名称为：my_utils(我的工具)
在包内提供两个模块：
    1、str_util.py（字符串相关工具，内含：）
        函数：str_reverse(s), 接受传入字符串，将字符串反转返回
        函数：substr(s, x, y), 按照下标x和y，对字符串进行切片
    2、file_util.py（文件处理相关工具，内含：）
        函数：print_file_info(file_name), 接收传入文件的路径，打印文件的全部内容，如文件不存在
        则捕获异常，输出提示信息，通过finally关闭文件对象
        函数：append_to_file(file_name, data), 接收文件路径以及传入数据，将数据追加写入到文件中
"""

# 文件处理相关的模块
def print_file_info(file_name):
    """
    功能是将给定路径的文件内容输出到控制台
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是：{e}")
    finally:
        if f:           # 如果变量是None，表示False，如果有任何内容，就是True
            f.close()

def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("E:/bill.txt")
    append_to_file("E:/test_append.txt", "你好")