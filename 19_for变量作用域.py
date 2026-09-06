for i in range(5):
    print(i)

print(i)  # 4,准确来说，在编程规范上，是不允许访问内部变量的，但是实际上是可以访问到的（不建议）
          # 如果想要访问，在for循环外部定义变量i即可，即 i = 0 ，如下


# i = 0
# for i in range(5):
#     print(i)
# print(i)