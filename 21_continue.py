for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")


# continue嵌套循环
for m in range(1, 6):
    print("语句1")
    for n in range(1, 6):
        print("语句2")
        continue
        print("语句3")

    print("语句4")
