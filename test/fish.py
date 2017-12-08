import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print ("我的位置:" , self.x, self.y)

class GoldFish(Fish):       #继承的作用是定义一个类、类属性和方法,子类继承父类,如果不用继承那么每定义一个类都需要重新定义类属性和方法,尤其属性和方法又是相似的.这样可以节省代码量
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        super().__init__()          #使用super方法自动找到父类的__init__方法定义否则会报错,因为shark重写了__init__方法
        self.hungry = True

    def eat(self):
        if self.hungry:
            print ("吃货的梦想就是天天吃^_^")
            self.hungry = False
        else:
            print ("吃不下")

    def move(self):         #多态,简单说就是调用的时候是子类重写的move函数而不是父类的move,如果super注销掉需要在子类重新定义x,y
        self.x += 1
        print ("我的位置:", self.x)

fish = Fish()

fish.move()

shark = Shark()

shark.eat()

shark.move()
