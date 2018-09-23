# 定义类
class Student:
    name1 = "123"

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def learn(self):
        print("learning")


stu1 = Student("123", "2", "3")
print(stu1.__dict__)
stu2 = Student("124", "2", "3")
print(stu2.__dict__)
stu3 = Student("125", "2", "3")
print(stu3.__dict__)

# 类的数据属性，是所有对象共有的
print(id(stu1.name1))
print(id(stu2.name1))
print(id(stu3.name1))

# 类的函数属性是绑定在各个对象上的
print(Student.learn)
# <bound method Student.learn of <__main__.Student object at 0x00000293C1749A20>>
print(stu1.learn)
print(stu2.learn)
print(stu3.learn)
