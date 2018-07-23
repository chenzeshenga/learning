# 用户验证
# 用户信息 user.txt 每一个数据为{"user1":["password",10000]}
file = open("user.txt", "r", encoding="utf-8")
data = file.read()
# print(data)
if data != '':
    user_dict = eval(data)
else:
    user_dict = {}
print(user_dict)

username = input("请输入姓名：")
password = input("请输入密码：")
while True:
    if username in user_dict:
        if password == user_dict[username]['password']:
            salary = user_dict[username]['salary']
            print("%s 欢迎登陆， 您的余额为%f" % (username, salary))
            break
        else:
            print("密码错误，请重新输入。")
            password = input("请输入密码：")
            continue
    else:
        print("欢迎您 %s 首次登陆" % username)
        salary = input("请输入您的工资，以完成注册")
        user_dict[username] = [password, int(salary)]
        print(user_dict)
        file = open("user.txt", "w", encoding="utf-8")
        file.write(str(user_dict))
        break

# {'user1':[{'1':['name':'电脑','number':1,'amount':1999]}]} 字段含义：{用户名：[{商品编号:[商品名，数量，总价]}]}
query = input("是否需要查询历史订单[y/n]:")
if 'y' == query:
    file = open("record.txt", "r", encoding="utf-8")
    data = file.read()
    if data != '':
        shopping_dict = eval(data)
    else:
        shopping_dict = {}
    if username in shopping_dict:
        print(shopping_dict[username])
    else:
        print("当前账户为做任何消费")

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

goods_info = "当前商品及价格如下"
print(goods_info.center(50, "*"))
goods_dict = {}
index = 1
for good in goods:
    print("商品编号%s:\t\t种类:%s\t\t价格:%s" % (str(index), good.get('name'), good.get('price')))
    goods_dict[str(index)] = good
    index += 1
print('goods_dict%s' % goods_dict)

exit_flag = 'q'
while True:
    goods_seq = input("请输入需要购买的商品编号,[q/Q]退出系统：")
    if 'q' == goods_seq.strip().lower():
        if username in shopping_dict:
            print("您的购物清单为：\n%s" % shopping_dict[username])
            file = open("record.txt", "w", encoding="utf-8")
            file.write(str(shopping_dict))
        else:
            print("您未消费。")
        print("你的余额为：%s" % user_dict[username]['salary'])
        print("Byebye")
        break
    else:
        if goods_seq in goods_dict:
            if int(user_dict[username]['salary']) - int(goods_dict[goods_seq]['price']) > 0:
                user_dict[username]['salary'] = int(user_dict[username]['salary']) - int(goods_dict[goods_seq]['price'])
                if username in shopping_dict:
                    shopping_dict[username][goods_seq]['name'] = goods_dict[goods_seq]['name']
                    shopping_dict[username][goods_seq]['number'] = int(shopping_dict[username][goods_seq]['number']) + 1
                    shopping_dict[username][goods_seq]['amount'] = int(
                        shopping_dict[username][goods_seq]['amount']) + int(goods_dict[goods_seq]['price'])
                else:
                    shopping_dict[username] = {goods_seq: {'name': goods_dict[goods_seq]['name'],
                                                           'number': 1,
                                                           'amount': int(goods_dict[goods_seq]['price'])}}
                print('当前账户余额为%s' % user_dict[username]['salary'])
            else:
                print('当前账户余额不足')
            continue
        else:
            print("商品编号有误，请重新输入")
            goods_seq = input("请输入需要购买的商品编号,[q/Q]退出系统：")
            continue
