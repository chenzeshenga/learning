# li = ['alex', 'egon', 'yuan', 'wusir', '666']
#
# li[4] = '999'
# print(li)
#
# index = li.index('yuan')
# print(index)
#
# newLi = li[-3:]
# print(newLi)
#
# s = 'www.luffycity.com'
# list = s.split(".")
# print(list)
#
# d = {
#     "Development": "开发小哥",
#     "OP": "运维小哥",
#     "Operate": "运营小仙女",
#     "UI": "UI小仙女"
# }
#
# print(d["Development"])
# d["OP"] = 123
# d.pop("UI")
# d.setdefault("ddd", "sss")
# print(d)
#
# sum = 0
# for i in range(1, 101):
#     sum += i
#
# print(sum)
#
# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

# name = input("name:")
# location = input("location:")
# hobby = input("hobby:")
#
# print("敬爱可爱的%s，最喜欢在%s地方干%s" % (name, location, hobby))

usernameTuple = ("seven", "alex")
passwordDefault = "123"

loginAttamp = 0

failDict = {"seven": 0, "alex": 0}

while True:
    username = input("username:")
    password = input("password:")
    if username in usernameTuple:
        if password == "123":
            print("welcome %s" % username)
        else:
            failDict[username] = failDict[username] + 1
            # print(failDict)
            if failDict[username] >= 3:
                break
    else:
        print("%s can't login" % username)
