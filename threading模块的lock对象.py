#coding:utf-8
"""
介绍python中threading模块的Lock()对象
顾名思义，它就是锁的意思
为什么要锁？
因为在有的脚本里，我们希望在一个线程运行的时候，另一个线程不要随便就来插一脚
最好等我彻底运行完了，下一个线程再执行
比如我们写一个队列，我们想要先设定队列的每一个值，再按顺序输出
这时候如果设置函数还没有执行完，输出函数就出来捣乱了
是不是达不到我们想要的效果？
是不是很可怕？
Lock对象出场啦～～～
"""

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        
        # acquire函数用来获取一个锁
        # 内部参数是timeout参数 如果超过了这个时间 还没有获取到锁
        # 就会返回获取失败 然后程序往下走
        # 如果不设定timeout 又获取不到锁  程序会一直阻塞下去
        # 当acquire已经被调用过一次时 就会获取不到锁
        if mutex.acquire(1):
            num = num + 1
            msg = self.name + 'set num to' + str(num)
            print msg
            # 释放锁
            # 如果线程事先没有获取锁 那么释放锁函数调用后会返回一个error
            mutex.release()

num = 0
#创建一个全局的线程锁实例
mutex = threading.Lock()

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test()
