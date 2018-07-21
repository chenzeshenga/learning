menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


def show(choice):
    for son in choice:
        print(son)
    param = input("[b/B] 返回上一层菜单, [q/Q] 退出菜单选择:").strip().lower()
    if param == 'q':
        exit()  # q/Q 退出
    elif param == 'b' and choice != menu:
        return  # b/B 返回上一层
    else:
        if param in choice:
            if choice[param]:  # 如果子元素是字典，则递归调用此方法
                show(choice[param])
        print("无您输入的对应菜单或已经在顶层菜单, 请重新选择")
        show(choice)


welcome = "请选择菜单"
print(welcome.center(50, '*'))
show(menu)
