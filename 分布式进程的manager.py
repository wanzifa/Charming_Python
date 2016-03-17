#coding:utf-8

"""
有时候 我们一台电脑负载不了那么多任务的时候，可以把任务分布到多台电脑上去。
分布式进程，就是多台电脑建立网络连接，一起处理任务
"""

import random, time, Queue
from multiprocessing.managers import BaseManager

#写入内容的队列
task_queue = Queue.Queue()
#输出内容的队列
result_queue = Queue.Queue()


#BaseManager可以理解为管理任务调度的对象
class QueueManager(BaseManager):
    pass

#把两个队列对象注册到网络上
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)

#abc在这里就是接入服务器的密码，绑定了端口才能与外界进行通信。
manager = QueueManager(address=('', 5000), authkey='abc')
#启动Queue
manager.start()
#现在两个queue都已经放上网络了，我们从网络上获取它们
task = manager.get_task_queue()
result = manager.get_result_queue()
#加入任务
for i in range(10):
    n=random.randint(0,10000)
    print '放入{0}'.format(n)
    task.put(n)
#取出结果
print('正在试图取出结果')
for i in range(10):
    r = result.get(timeout=10)
    print '取出了{0}'.format(r)
#关闭队列管理对象
manager.shutdown()


