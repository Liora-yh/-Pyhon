"""
工厂模式：当需要大量创建一个类的实例的时候，就可以使用工厂模式，
即，从原生的使用类的构造去创建对象的形式
迁移到，基于工厂提供的方法去创建对象的形式
"""

# 原生的构造方式
# class Person:
#     pass
#
# class Worker(Person):
#     pass
# class Student(Person):
#     pass
# class Teacher(Person):
#     pass
#
# worker = Worker()
# student = Student()
# teacher = Teacher()


# 工厂模式
class Person:
    pass

class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class PersonFactory:
    def get_person(self, p_type):
        if p_type == "worker":
            return Worker()
        elif p_type == "student":
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker = pf.get_person("worker")
student = pf.get_person("student")
teacher = pf.get_person("teacher")











