#coding:utf-8
"""
承接分布式进程的第一个文件，下面这段代码实现的是队列中内容的输出
"""

import random, time, Queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

#只写名字，意味着获取
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器
server_addr = '127.0.0.1'
print 'connect to server {0}'.format(server_addr)
m = QueueManager(address=(server_addr, 5000), authkey='abc')
#从网络连接
m.connect()
#获取队列
task = m.get_task_queue()
result = m.get_result_queue()
#开始做任务啦
for i in range(10):
    try:
        n=task.get(timeout=1)
        print '取出了{0}*{0}'.format(n)
        r="{0}*{0}={1}".format(n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('队列是空的')
#处理完了
print('处理完啦！')
