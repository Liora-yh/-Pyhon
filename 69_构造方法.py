class Student:
    # 下面三行可以省略不写
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")

stu = Student("周杰伦", 31, "180789744444")
print(stu.name)
print(stu.age)
print(stu.tel)
