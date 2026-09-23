"""
多态；指的是多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)



"""
抽象类（也可以称之为接口）：含有抽象方法的类称之为抽象类【比如上面的Animal类】
抽象方法：方法时空实现的(pass)称之为抽象方法【就比如说上面Animal类里面的speak()方法】
    父类用雷绝地有哪些方法，具体的方法实现由子类自行决定
"""
# 演示抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")

class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()

midea = Midea_AC()
gree = Gree_AC()

make_cool(midea)
make_cool(gree)





