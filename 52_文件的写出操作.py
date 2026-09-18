import time
# 文件的写入
"""
    直接调用write，内容并未真正的写入文件，只是存在缓冲区
    当调用flush时，才真正写入文件
    这样做时避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写入磁盘）
"""
from encodings import utf_8

# 打开文件，不存在的文件
f = open("E:/test.txt", "w", encoding="utf_8")

f.write("Hello world!!!")

# 文件刷新
f.flush()

time.sleep(600000)

f.close()   # close()方法内置了flush

# 打开一个存在的文件
f = open("E:/test.txt", "w", encoding="utf_8")
f.write("罗玉华")      # 会把里面的内容清空，再写入
f.close()
