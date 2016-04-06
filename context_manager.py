#coding:utf-8
"""
python的上下文管理器
形式为with....as...
在某任务执行之初，上下文管理器做好执行准备
当任务执行完毕或者执行过程中出现了异常
上下文管理器负责结束工作
上下文管理器必须包含__enter__和__exit__两个方法
"""

#without context manager
f=open("new.txt", 'w')
print(f.closed)
f.write("Hello world!")
f.close()
print(f.closed)

#with context manager
with open('new.txt', 'w') as f:
    print(f.closed)
    f.write("Hello world!")
print (f.closed)

"""
任何定义了__enter__和__exit__的对象都是上下文管理器
"""
