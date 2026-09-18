import time
# 文件的追加
from encodings import utf_8

# 打开文件，不存在的文件
f = open("E:/test.txt", "a", encoding="utf_8")

f.write("Hello world!!!")

# 文件刷新
f.flush()

time.sleep(600000)

f.close()   # close()方法内置了flush

# 打开一个存在的文件
f = open("E:/test.txt", "a", encoding="utf_8")
f.write("罗玉华")      # 再最后追加写入文件
f.close()