from com.chenzeshenga.module02.homework.atm import logics
from com.chenzeshenga.module02.homework.atm.auth import login
from com.chenzeshenga.module02.homework.atm.logger import logger

atm_logger = logger()

functions = [
    ('账户信息', logics.user_info),
    ('提现', logics.withdraw),
    ('还款', logics.repay)
]


def controller(user):
    while True:
        for index, function in enumerate(functions):
            print(index, "\t" + function[0])
        print("exit\t退出")
        choice = input("请输入功能序号：").strip()
        if not choice:
            continue
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(functions):
                functions[choice][1](user,atm_logger)
        if choice == "exit":
            exit()


def start():
    user = {
        'authored': False,
        'data': None
    }

    tries = 0

    while user['authored'] is not True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        user_data = login(username, password)
        if user_data:
            user['authored'] = True
            user['data'] = user_data
            print('用户%s, 欢迎登陆' % username)
            atm_logger.info('user %s loggin.' % username)
            controller(user)
        else:
            print('用户名/密码错误')
            tries += 1

        if tries == 3:
            err_msg = '%s 用户名密码输入次数过多' % username
            print(err_msg)
            atm_logger.info(err_msg)
            break
