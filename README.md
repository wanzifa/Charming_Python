# Review_Python
My Python Review Notes ^_^</br>
<h3><strong>Python复习笔记啦啦啦~~~~</h3></strong>
----------03.17第一次更新---------
>ThreadLocal类，一个神奇的小工具。</br>
有时候，我们在一个线程里需要将同一个变量传递给不同的函数，也就是需要实现一个变量的多重操作。此时我们多么希望它是一个全局变量呀。然而并没有，于是我们只能苦逼地一一传参T_T。
自从有了ThreadLocal，为每一个线程创建自己的变量小天地，在local类实例中定义过的变量，可以在线程内部自由穿梭，如同全局一般。一旦出了这个线程，它就不见啦，所以也不会打扰到别的线程。
嘿嘿嘿。

欲知效果如何，请戳[threadlocal类特性小测试](https://github.com/wanzifa/Review_Python/blob/master/threadlocal%E7%B1%BB%E7%9A%84%E7%89%B9%E6%80%A7.py)

----------03.17更新--------------
>添加了分布式进程的处理，基础知识都在注释上啦，欢迎pr！！！^_^</br>
分布式进程很厉害的，有时候我们一台电脑解决不完的问题，就让大家一起来解决！

----------03.18更新--------------
>添加了werkzeug模块的小应用。
最近在看flask源码，一脸懵逼。看了werkzeug之后多少好一些了
抹泪走。

----------03.18晚上更新----------
>终于把werkzeug代码和注释写了个差不多，注释还可以写得更细一些，不过有点晚了，明天继续更😄

----------03.19更新--------------
>werkzeug注释已更完～～欢迎pr！！！

----------03.20更新--------------
>更新threading模块的Lock对象</br>
介绍python中threading模块的Lock()对象</br>
Lock对象干啥使的？</br>
顾名思义，它就是锁的意思</br>
为什么要锁？</br>
事实上，锁是一直存在的。</br>
我们的python解释器有一个全局锁（GIL），它使得在任意时刻解释器内只能有一个线程在运行</br>
在有的脚本里，我们希望在一个线程运行的时候，另一个线程不要随便就来插一脚</br>
最好等我彻底运行完了，下一个线程再执行</br>
然而事实是，多线程的实现，正是通过线程间的不断切换</br>
于是一般情况下，一个线程执行完毕之前，全局锁会被另个线程获取，另个线程执行了一点，再把全局锁还回来</br>
如此交替下去，切换速度快了，才造就一种多个线程同时运行的假象。</br>
那么如果我希望，虽然这个进程里有不同的线程，但要让它们顺序执行</br>
这时候,拿Lock(线程锁)出来说事就很重要了</br>
在全局中定义一个Lock对象，可以实现线程的顺序运行，也就是同步.</br>

----------03.21更新-------------
>更新了re模块的match和search两个函数，比较小的一个点，没有什么说的😂</br>
大家还是看代码吧！摸摸大！
django源码龟速读
捂脸走
