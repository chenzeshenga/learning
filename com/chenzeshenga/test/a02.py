import datetime
import time


def before(fun):
    def inner():
        print("before->inner")
        bt = datetime.datetime.now()
        res = fun()
        at = datetime.datetime.now()
        print(at - bt)
        print("finish")
        return res

    return inner


@before
def fun1():
    print("fun1")
    time.sleep(1)

    return "fun1"


print(fun1())
