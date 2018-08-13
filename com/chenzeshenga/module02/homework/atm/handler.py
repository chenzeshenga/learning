import json
import os

from com.chenzeshenga.module02.homework.conf import prop


def load_user_data(username):
    user_file = os.path.join(prop.IO_PATH, '%s.json' % username)
    if os.path.isfile(user_file):
        f = open(user_file)
        data = json.load(f)
        f.close()
        return {'status': 0, 'data': data}
    else:
        return {'status': -1, 'data': '加载用户数据失败'}


def save_user_data(user):
    user_file = os.path.join(prop.IO_PATH, '%s.json' % user['id'])
    if os.path.isfile(user_file):
        f = open(user_file, "w")
        data = json.dump(user, f)
        f.close()
        return {'status': 0, 'data': data}
    else:
        return {'status': -1, 'data': '存储用户数据失败'}
