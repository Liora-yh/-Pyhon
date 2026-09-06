# 语法1：range(num)
#       获取一个从0开始，到num结束的数字序列（不含num）
#       如：range(5)取得的数据是：[0, 1, 2, 3 ,4]
for x in range(10):
    print(x)

# 语法2：range(num1, num2)
#       从num1到num2（不含num2）
for x in range(5, 10):
    print(x)

# 语法3：range(num1, num2, step)
#       同语法2，数字之间相差step（step默认为1）
#       如：range(5, 10, 2)取得的数据是：[5, 7, 9]
for x in range(5, 10, 2):
    print(x)