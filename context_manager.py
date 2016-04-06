#coding:utf-8
"""
python的上下文管理器
形式为with....as...
在某任务执行之初，上下文管理器做好执行准备
当任务执行完毕或者执行过程中出现了异常
上下文管理器负责结束工作
上下文管理器必须包含__enter__和__exit__两个方法
__enter__ 方法将在进入代码块前被调用。
__exit__ 方法则在离开代码块之后被调用(即使在代码块中遇到了异常)。
所以，事实上上下文管理器的任务是 – 代码块执行前准备，代码块执行后收拾
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
