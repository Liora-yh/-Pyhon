# Python的多线程可以通过threading模块来实现
# thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
# group:暂时无用，未来功能的预留参数
# target:表示线程要执行的任务名，即函数名
# name:表示线程的名字，一般不用设置，默认是Thread-N
# args:表示传递给target的参数，必须是元组类型
# kwargs:表示传递给target的参数，必须是字典类型

# 启动线程，让线程开始工作
# thread.obj.start()

import time
import threading

def sing():
    while True:
        print("我在唱歌，啦啦啦......")
        time.sleep(1)

def dance():
    while True:
        print("我在跳舞，噔噔噔......")
        time.sleep(1)

def sing1(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance1(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # sing()
    # dance()

    sing_thread = threading.Thread(target = sing)
    dance_thread = threading.Thread(target = dance)
    sing_thread1 = threading.Thread(target=sing1, args=("我在唱歌!!!!!",))
    dance_thread1 = threading.Thread(target=dance1, args=("我在跳舞!!!!!",))

    # sing_thread.start()
    # dance_thread.start()
    sing_thread1.start()
    dance_thread1.start()
