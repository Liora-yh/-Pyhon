# 单继承
class Phone:
    IMEI = None     # 序列号
    producer = "LLLLYH" # 厂商

    def call_by_5g(self):
        print("父类的5g通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "YH"             # 复写父类属性

    def call_by_5g(self):       # 复写父类方法
        print("子类的5g通话")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

# 在子类中，调用父类成员
class MyPhone2(Phone):
    producer = "YH"             # 复写父类属性

    def call_by_5g(self):       # 复写父类方法
        # 方式1
        print(f"父类的厂商是：{Phone.producer}")
        Phone.call_by_5g(self)
phone2 = MyPhone2()
phone2.call_by_5g()
print(phone2.producer)


# 方式2
class MyPhone3(Phone):
    producer = "YH"             # 复写父类属性

    def call_by_5g(self):       # 复写父类方法
        # 方式3
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
phone3 = MyPhone3()
phone3.call_by_5g()
print(phone3.producer)