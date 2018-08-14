import os

from com.chenzeshenga.module02.homework.atm import handler
from com.chenzeshenga.module02.homework.conf import prop


def user_info(user, atm_logger):
    print("user info".center(30, "*"))
    for k, v in user['data'].items():
        if k != 'password':
            print('%15s: %s' % (k, v))
    print("user info".center(30, "*"))


def withdraw(user, atm_logger):
    atm_logger.info("current credit is %s, current balance is %s" % (user['data']['credit'], user['data']['balance']))
    while True:
        amount = input("请输入需要取出的数额：").strip()
        if amount.isdigit() and float(amount) > 0:
            amount = float(amount)
            if amount <= user['data']['balance'] + amount * 0.05:
                user['data']['balance'] = user['data']['balance'] - amount - amount * 0.05
                atm_logger.info("user %s withdraw %s" % (user['data']['id'], amount))
                atm_logger.info(
                    "current credit is %s, current balance is %s" % (user['data']['credit'], user['data']['balance']))
                status = handler.save_user_data(user['data'])['status']
                if status == -1:
                    print("存储用户数据失败")
                    print("请重试")
                    user['data']['balance'] = user['data']['balance'] + amount + amount * 0.05
                    continue
                else:
                    print("成功取出%s" % amount)
                    break
            else:
                print("可取余额不足")
        else:
            print("输入错误")
            continue


def repay(user, atm_logger):
    atm_logger.info("current credit is %s, current balance is %s" % (user['data']['credit'], user['data']['balance']))
    while True:
        amount = input("请输入还款的数额：").strip()
        if amount.isdigit() and float(amount) > 0:
            amount = float(amount)
            user['data']['balance'] = user['data']['balance'] + amount
            atm_logger.info("user %s repay %s" % (user['data']['id'], amount))
            atm_logger.info(
                "current credit is %s, current balance is %s" % (user['data']['credit'], user['data']['balance']))
            status = handler.save_user_data(user['data'])['status']
            if status == -1:
                print("存储用户数据失败")
                print("请重试")
                user['data']['balance'] = user['data']['balance'] - amount
                continue
            else:
                print("成功还款%s" % amount)
                break
        else:
            print("输入错误")
            continue


def transfer(user, atm_logger):
    while True:
        transfer_user = input("请输入对方id：").strip()
        transfer_amount = input("请输入转账金额：").strip()
        transfer_user_data = handler.load_user_data(transfer_user)
        if transfer_user_data['status'] == 0:
            if transfer_amount.isdigit() and float(transfer_amount) > 0:
                if float(transfer_amount) > float(user['data']['balance']):
                    print("当前账户余额不足")
                    continue
                else:
                    transfer_amount = float(transfer_amount)
                    transfer_user_data['data']['balance'] = transfer_user_data['data']['balance'] + transfer_amount
                    user['data']['balance'] = user['data']['balance'] - transfer_amount
                    status1 = handler.save_user_data(transfer_user_data['data'])['status']
                    status2 = handler.save_user_data(user['data'])['status']
                    if status1 == 0 and status2 == 0:
                        print("成功转账给%s %s" % (transfer_user, transfer_amount))
                        atm_logger.info(
                            "user %s transfer %s to user %s" % (user['data']['id'], transfer_amount, transfer_user))
                    else:
                        print("转账失败")
                        continue
            else:
                print("输入金额有误")
                break
        else:
            print("无对应的对方账户 %s" % transfer_user)
            break


def shopping(user, atm_logger):
    print("下面将打印当前系统的物品，如需购买请输入编号。")
    goods = prop.GOODS
    goods_info = "当前商品及价格如下"
    print(goods_info.center(50, "*"))
    goods_dict = {}
    index = 1
    for good in goods:
        print("商品编号:%s\t\t种类:%s\t\t价格:%s" % (str(index), good.get('name'), good.get('price')))
        goods_dict[str(index)] = good
        index += 1
    exit_flag = 'q'
    curr_shopping_dict = {}
    shopping_dict = {}
    username = user['data']['id']
    while True:
        goods_seq = input("\n请输入需要购买的商品编号,[q/Q]结账并退出系统：")
        if 'q' == goods_seq.strip().lower():
            if username in curr_shopping_dict:
                print("\n此次您的购物清单为：")
                for key in curr_shopping_dict[username]:
                    print("商品编号:%s\t\t种类:%s\t\t消费数量:%s\t\t消费总金额%s" % (
                        key, curr_shopping_dict[username][key]['name'], curr_shopping_dict[username][key]['number'],
                        curr_shopping_dict[username][key]['amount']))
                for key in curr_shopping_dict[username]:
                    if shopping_dict:
                        if key in shopping_dict[username].keys():
                            shopping_dict[username][key]['number'] += curr_shopping_dict[username][key]['number']
                            shopping_dict[username][key]['amount'] += curr_shopping_dict[username][key]['amount']
                        else:
                            shopping_dict[username][key] = curr_shopping_dict[username][key]
                    else:
                        shopping_dict = {username: curr_shopping_dict[username]}
                status = handler.save_user_data(user['data'])['status']
                if status == 0:
                    print("结账成功，退出商城")
                    atm_logger.info("%s buy %s in the shopping mall" % (username, str(curr_shopping_dict)))
                else:
                    print("转账失败")
                    continue
            else:
                print("您未消费。")
            print("Byebye")
            break
        else:
            if goods_seq in goods_dict:
                if float(user['data']['balance']) - float(goods_dict[goods_seq]['price']) >= 0:
                    user['data']['balance'] = float(user['data']['balance']) - float(
                        goods_dict[goods_seq]['price'])
                    if username in curr_shopping_dict:
                        if goods_seq in curr_shopping_dict[username]:
                            curr_shopping_dict[username][goods_seq]['name'] = goods_dict[goods_seq]['name']
                            curr_shopping_dict[username][goods_seq]['number'] = int(
                                curr_shopping_dict[username][goods_seq]['number']) + 1
                            curr_shopping_dict[username][goods_seq]['amount'] = float(
                                curr_shopping_dict[username][goods_seq]['amount']) + float(
                                goods_dict[goods_seq]['price'])
                        else:
                            curr_shopping_dict[username][goods_seq] = {'name': goods_dict[goods_seq]['name'],
                                                                       'amount': float(
                                                                           goods_dict[goods_seq]['price'])}
                    else:
                        curr_shopping_dict[username] = {goods_seq: {'name': goods_dict[goods_seq]['name'],
                                                                    'number': 1,
                                                                    'amount': float(goods_dict[goods_seq]['price'])}}
                    print('当前账户余额为%s' % user['data']['balance'])
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


def manager(user, atm_logger):
    def add_user_info(user, atm_logger):
        print("新建账号")
        user_id = input("请输入账号：").strip()
        password = input("请输入密码：").strip()

        new_user = {
            "balance": 15000,
            "expire_date": "2022-08-14",
            "enroll_date": "2018-08-13",
            "credit": 15000,
            "id": user_id,
            "status": 0,
            "repay_day": 22,
            "password": password
        }
        user_file = os.path.join(prop.IO_PATH, '%s.json' % new_user['id'])
        user_file = open(user_file, "w")
        user_file.close()
        handler.save_user_data(new_user)

    def adjust(user, atm_logger):
        while True:
            amount = input("请输入调整金额：").strip()
            if amount.isdigit() and float(amount) > 0:
                amount = float(amount)
                orginal_amount = user['data']['credit']
                if amount < user['data']['balance']:
                    print("%s 小于当前账单额度")
                    print("调整失败")
                    continue
                else:
                    user['data']['credit'] = amount
                    status = handler.save_user_data(user['data'])['status']
                    if status == -1:
                        print("调整额度失败")
                        print("请重试")
                        user['data']['credit'] = orginal_amount
                        continue
                    else:
                        print("额度调整成功")
                        atm_logger.info("user %s adjust credit to %s" % (user['data']['id'], amount))
                        break

    def disable_user(user, atm_logger):
        username = input("请输入需要冻结的用户：").strip()
        user_lock = handler.load_user_data(username)
        if user_lock['status'] == 0:
            user_lock['data']['status'] = -1
            status = handler.save_user_data(user_lock['data'])['status']
            if status == 0:
                print("用户%s 冻结成功" % username)
                atm_logger.info("user %s was locked by user %s" % (username, user['data']['id']))
            else:
                print("冻结失败")
        else:
            print("无您输入的用户%s" % username)

    functions = [
        ('添加账户', add_user_info),
        ('用户额度调整', adjust),
        ('冻结账户', disable_user)
    ]
    while True:
        print("当前有如下管理功能：\n")
        for index, function in enumerate(functions):
            print(index, "\t" + function[0])
        print("exit\t退出")
        choice = input("请输入功能序号：").strip()
        if not choice:
            continue
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(functions):
                functions[choice][1](user, atm_logger)
        if choice == "exit":
            exit()
