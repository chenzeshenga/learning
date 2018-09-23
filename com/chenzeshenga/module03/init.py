# 定义类
class Student:
    name = "123"

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def learn(self):
        print("learning")


# python先生成一个空对象，然后调用__init__方法初始化
stu1 = Student("123", "2", "3")

print(stu1)

print(stu1.__dict__)
