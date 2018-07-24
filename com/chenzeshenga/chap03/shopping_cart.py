# 用户验证
# 用户信息 user.txt 每一个数据为{'user1': {'password': 'password1', 'salary': 10000}}
file = open("user.txt", "r", encoding="utf-8")
users = file.read()
if users != '':
    user_dict = eval(users)
else:
    user_dict = {}
# print("user_dict: %s " % user_dict)

# 消费记录 record.txt 数据为{'user1': {'1': {'name': '电脑', 'number': 1, 'amount': 1999}}}
# {'user1':{'1':{'name':'电脑','number':1,'amount':1999}}} 字段含义：{用户名：{商品编号:{商品名，数量，总价}}}
file = open("record.txt", "r", encoding="utf-8")
records = file.read()
if records != '':
    shopping_dict = eval(records)
else:
    shopping_dict = {}
# print("shopping_dict: %s " % shopping_dict)

username = input("请输入姓名：")
password = input("请输入密码：")
while True:
    if username in user_dict:
        if password == user_dict[username]['password']:
            print("%s 欢迎登陆， 您的余额为%s" % (username, user_dict[username]['salary']))
            break
        else:
            print("密码错误，请重新输入。")
            password = input("请输入密码：")
            continue
    else:
        print("欢迎您 %s 首次登陆" % username)
        salary = input("请输入您的工资，以完成注册")
        user_dict[username] = {'password': password, 'salary': int(salary)}
        # print(user_dict)
        file = open("user.txt", "w", encoding="utf-8")
        file.write(str(user_dict))
        break

print()
query = input("是否需要查询历史订单[y/n]:")
if 'y' == query:
    if username in shopping_dict:
        # print(shopping_dict[username])
        print("历史订单如下")
        for key in shopping_dict[username]:
            print("商品编号:%s\t\t种类:%s\t\t消费数量:%s\t\t消费总金额%s" % (
                key, shopping_dict[username][key]['name'], shopping_dict[username][key]['number'],
                shopping_dict[username][key]['amount']))
    else:
        print("当前账户未做任何消费")

print()
print("下面将打印当前系统的物品，如需购买请输入编号。")

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
    print("商品编号:%s\t\t种类:%s\t\t价格:%s" % (str(index), good.get('name'), good.get('price')))
    goods_dict[str(index)] = good
    index += 1
# print('goods_dict%s' % goods_dict)

# 购物车功能
exit_flag = 'q'
curr_shopping_dict = {}
while True:
    goods_seq = input("\n请输入需要购买的商品编号,[q/Q]退出系统：")
    if 'q' == goods_seq.strip().lower():
        if username in curr_shopping_dict:
            # print("您的购物清单为：\n%s" % shopping_dict[username])
            print("\n此次您的购物清单为：")
            for key in curr_shopping_dict[username]:
                print("商品编号:%s\t\t种类:%s\t\t消费数量:%s\t\t消费总金额%s" % (
                    key, curr_shopping_dict[username][key]['name'], curr_shopping_dict[username][key]['number'],
                    curr_shopping_dict[username][key]['amount']))
            file = open("record.txt", "w", encoding="utf-8")
            # dict1 {'user1': {'1': {'name': '电脑', 'number': 1, 'amount': 1999}}}
            # dict2 {'user1': {'1': {'name': '电脑', 'number': 1, 'amount': 1999}}}
            # curr_shopping_dict[username]  {'1': {'name': '电脑', 'number': 1, 'amount': 1999}}
            # print(curr_shopping_dict)
            for key in curr_shopping_dict[username]:
                if shopping_dict:
                    if key in shopping_dict[username].keys():
                        shopping_dict[username][key]['number'] += curr_shopping_dict[username][key]['number']
                        shopping_dict[username][key]['amount'] += curr_shopping_dict[username][key]['amount']
                    else:
                        shopping_dict[username][key] = curr_shopping_dict[username][key]
                else:
                    shopping_dict = {username: curr_shopping_dict[username]}
            file.write(str(shopping_dict))
            file = open("user.txt", "w", encoding="utf-8")
            file.write(str(user_dict))
        else:
            print("您未消费。")

        print("你的余额为：%s" % user_dict[username]['salary'])
        print("Byebye")
        break
    else:
        if goods_seq in goods_dict:
            if int(user_dict[username]['salary']) - int(goods_dict[goods_seq]['price']) >= 0:
                user_dict[username]['salary'] = int(user_dict[username]['salary']) - int(goods_dict[goods_seq]['price'])
                if username in curr_shopping_dict:
                    if goods_seq in curr_shopping_dict[username]:
                        curr_shopping_dict[username][goods_seq]['name'] = goods_dict[goods_seq]['name']
                        curr_shopping_dict[username][goods_seq]['number'] = int(
                            curr_shopping_dict[username][goods_seq]['number']) + 1
                        curr_shopping_dict[username][goods_seq]['amount'] = int(
                            curr_shopping_dict[username][goods_seq]['amount']) + int(goods_dict[goods_seq]['price'])
                    else:
                        curr_shopping_dict[username][goods_seq] = {'name': goods_dict[goods_seq]['name'],
                                                                   'number': 1,
                                                                   'amount': int(
                                                                       goods_dict[goods_seq]['price'])}
                else:
                    curr_shopping_dict[username] = {goods_seq: {'name': goods_dict[goods_seq]['name'],
                                                                'number': 1,
                                                                'amount': int(goods_dict[goods_seq]['price'])}}
                print('当前账户余额为%s' % user_dict[username]['salary'])
                # print(shopping_dict)
                print("当前已消费列表如下：")
                for key in curr_shopping_dict[username]:
                    print("商品编号:%s\t\t种类:%s\t\t消费数量:%s\t\t消费总金额%s" % (
                        key, curr_shopping_dict[username][key]['name'], curr_shopping_dict[username][key]['number'],
                        curr_shopping_dict[username][key]['amount']))
            else:
                print('当前账户余额不足')
            continue
        else:
            print("商品编号有误，请重新输入")
    continue
