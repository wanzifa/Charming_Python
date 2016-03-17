#coding:utf-8
"""
通过一个小例子来验证thread.local类的特性
这个类为每一个线程提供自己的小天地，它定义的变量，可以在线程内部自由穿梭，实现一种“半全局”状态
"""

import threading

local_data = threading.local()
local_data.name = 'xiaowanzi'


class TestThread(threading.Thread):
    def run(self):
        print threading.currentThread()
        print 'TestThread内部的Threadlocal对象的字典内容为：'+str(local_data.__dict__)

def process_student(name):
    local_data.name=name
    test1()

def test1():
    print '线程1输出的学生姓名为'+local_data.name

t1=threading.Thread(target=process_student, args=('xiaoming',))
t1.start()
t1.join()
t2=TestThread()
t2.start()
t2.join()
print '全局Threadlocal对象的字典内容为：'+str(local_data.__dict__)




