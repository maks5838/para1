class Human:
    eyes = 2
    legs = 2
    hands= 2



class Student(Human):
    isStuding = True

class Worker(Student):
    age = 25

print(Student.hands)
print(Worker.age)
print(Worker.isStuding)


class ITStep:
    __student = "BoyAndGirl"
    def __init__(self):
        print(self. __student)



j = ITStep()
# print(ITStep.__student)
class Grandparent:
    def about(self):
        print("I am GrandParent")
    def about_myself(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
nick = Child()




class CPU:
    def working(self):
        print("Працюю дуже потужно")

class Display:
    def show(self):
        print("Показую меми")


class SmartPhone(CPU, Display):
    pass

xiaomi = SmartPhone()
xiaomi.working()
xiaomi.show()