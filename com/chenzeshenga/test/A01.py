# def fil():
#     l1 = [11, 22, 33, 44, 55]
#     a = filter(lambda x: x > 33, l1)
#     for i in a:
#         print(i)
#
#
# fil()

# print(list(filter(lambda x: x > 33, [11, 22, 33, 44, 55])))

# import logging
# # import datetime
#
# fomatter= logging.Formatter("%(acstime)s -%(name)s-%(levelname)s-%(message)s")
# myLog=logging.FileHandler("example.log")
# myLog.setFormatter(fomatter)
#
# myLog.setFormatter(fomatter)
# # logging.addLevelName("info","bug")
# myLog.setLevel(logging.INFO)
#
# myLog.

import hashlib

m = hashlib.md5()

m.update(b"hello")

password0 = m.hexdigest()
user = "root"
fail = 0

while True:
    username = input("username:")
    pwd = input("password")

    m1 = hashlib.md5()
    m1.update(pwd.encode())
    password = m1.hexdigest()

    if username == user and password == password0:
        print("success")
    else:
        fail = fail + 1

    if fail >= 3:
        f = open("text.txt", "w")
        f.write(username)
        f.close()
        break
