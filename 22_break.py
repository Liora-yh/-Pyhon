for i in range(1, 10):
    print("语句1")
    break
    print("语句2")

print("语句3")

# break的嵌套语句
for m in range(1, 10):
    print("语句1")
    for n in range(1, 10):
        print("语句2")
        break
        print("语句3")

    print("语句4")
