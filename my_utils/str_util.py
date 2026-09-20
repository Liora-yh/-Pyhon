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

# 字符串处理相关的模块
def str_reverse(s):
    """
    功能是将字符传完成反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def substr(s, x, y):
    """
    功能是按照给定的下标完成给定字符串的切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("落雨花今天真棒"))
    print(substr("落雨花今天真棒", 1, 3))
