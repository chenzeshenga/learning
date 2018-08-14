from com.chenzeshenga.module02.homework.atm.handler import load_user_data


def auth2(auth_type):
    def auth(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'user':
                username = input('请输入用户名：').strip()
                password = input('请输入密码：').strip()
                user_data = load_user_data(username)
                if user_data['status'] == 0:
                    if password == user_data['data'].get("password"):
                        print('登录成功')
                        res = func(*args, **kwargs)
                        return res
                else:
                    print("登录失败")

        return wrapper

    return auth


def login(username, password):
    user_data = load_user_data(username)
    if user_data['status'] == 0 and user_data['data']['status'] == 0:
        if password == user_data['data'].get("password"):
            return user_data['data']
    return None
