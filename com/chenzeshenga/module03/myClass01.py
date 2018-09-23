# 定义类
class Student:
    # 数据属性
    name = "123"

    # 函数属性
    def learn(self):
        print("learning")


# 查看类的名称空间
print(Student.__dict__)

# 查看类的属性
print(Student.name)

# 增加类的属性
Student.age = 18
print(Student.__dict__)

# 删除类的属性
del Student.age
print(Student.__dict__)

# 改
Student.name = "kjhkjh"
print(Student.__dict__)
