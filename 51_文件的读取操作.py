import time

# 打开文件 - open()函数
f = open('C:/Users/小罗/Desktop/class CameraState.txt', 'r', encoding='UTF-8')
print(type(f))

# 读操作
# 1、read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：{f.read()}")
print("----------------------------------------------------")

# 2、readlines()
# lines = f.readlines()
# print(type(lines))
# print(f'读取全部行的结果是{lines}')  # 结果是空列表
# 因为前面8行的时候已经读取了全部数据，所有这次读的时候，继续接着上次的内容往后面读，没有内容了，返回空列表
print("----------------------------------------------------")

# 3、readline() 一次读取一行
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f'第一行数据是：{line1}')
print(f'第二行数据是：{line3}')
print(f'第三行数据是：{line2}')

# for循环读取文件行
for line in open('C:/Users/小罗/Desktop/class CameraState.txt', 'r', encoding='UTF-8'):
    print(line)

# 文件的关闭
f.close()
time.sleep(500000)

# with open 语法操作文件
with open('C:/Users/小罗/Desktop/class CameraState.txt', 'r', encoding='UTF-8') as f:
    f.readlines()
