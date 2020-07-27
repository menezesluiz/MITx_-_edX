# class Cordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance(self, other):
#         x_diff_sq = (self.x-other.x) ** 2
#         y_diff_sq = (self.y-other.y) ** 2
#         return (x_diff_sq + y_diff_sq) ** 0.5
#     def __str__(self):
#         return "<" + str(self.x) + "," + str(self.y) + ">"
#
# c = Cordinate(3,4)
# origin = Cordinate(0,0)

#_____________________________________________________________________________#

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = ""):
        self.name = newname
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:" + str(self.name) + str(self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:" + str(self.name) + str(self.age)

#class Person(Animal):
#    def __init__(self, name, age):

print((repr(alpha)) == str(alpha))
