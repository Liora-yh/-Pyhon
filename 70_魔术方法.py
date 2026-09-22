class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__字符串方法
    def __str__(self):
        return f"student类对象：name={self.name}, age={self.age}"

    # __lt__ 小于符合比较方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__小于等于符号比较方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__   ==符号比较
    def __eq__(self, other):
        return self.age == other.age

student = Student("周杰伦", 11)
print(student)
print(str(student))

stu1 = Student("罗玉华", 21)
stu2 = Student("落雨花", 18)
print(stu1 < stu2)
print(stu1 > stu2)
print(stu1 <= stu2)
print(stu1 >= stu2)
print(stu1 == stu2)
