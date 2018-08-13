from com.chenzeshenga.module02.homework.atm.handler import load_user_data


def login(username, password):
    user_data = load_user_data(username)
    if user_data['status'] == 0:
        if password == user_data['data'].get("password"):
            return user_data['data']
    return None
