from com.chenzeshenga.module02.homework.atm import handler


def user_info(user, atm_logger):
    print("user info".center(30, "*"))
    for k, v in user['data'].items():
        if k != 'password':
            print('%15s: %s' % (k, v))


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
