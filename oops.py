# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# s1 = Student("Ravi", 20)
# s1.display()
# class A:
#     name="roopini"
#     def f1(self):
#       print("f1 fumction is working")
# myobj=A()
# print(myobj.name)
# print(myobj.f1())

# class A:
#     stuName = "hema"
#     def __init__(self,age, mobile):
#         self.age = age
#         self.mobile = mobile
#         print(f"my name is {self.stuName},my age is {self.age}, my mobile no is {self.mobile}")
# obj1 = A(20,947643895)
# print(obj1.age,obj1.mobile)


# class Parent:
#     def f1(self):
#         print("Parent class fun is working")
# class Child(Parent):
#     def f2(self):
#         print("Child class fun is working")
# childObj = Child()
# childObj.f2()
# childObj.f1()


# class Father:
#     def f1(self):
#         print("Father class fun is working")
# class Mother:
#     def f2(self):
#         print("Mother class fun is working")
# class Child(Father,Mother):
#     def f3(self):
#         print("Child class fun is working")

# objChild = Child()
# objChild.f1()
# objChild.f2()
# objChild.f3()


# class A:
#     def f1(self):
#         print("A class fun is working")
# class B(A):
#     def f2(self):
#         print("B class fun is working")
# class C(B):
#     def f3(self):
#         print("C class fun is working")
# ObjC = C()
# ObjC.f1()

from abc import ABC,abstractmethod
class abstraction(ABC):
    @abstractmethod
    def parent(self):
        print("parents is working")
class normal(abstraction):
    def parent(self):
        super(). parent()
        print("normal is working")
c=normal()
c.parent()
