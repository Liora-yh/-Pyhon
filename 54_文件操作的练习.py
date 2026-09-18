fr = open("E:/bill.txt", "r", encoding="UTF-8")
fw = open("E:/bill.txt.bak", "w", encoding="UTF-8")

for line in fr:
    line.strip()
    if line.split(",")[4] == "测试":
        continue
    fw.write(line)
    #由于前面进行了strip操作，所有需要手动的写入换行符
    fw.write("\n")

fr.close()
fw.close()
