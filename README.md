# Review_Python
My Python Review Notes ^_^</br>
<h3><strong>Python复习笔记啦啦啦~~~~</h3></strong>
----------03.17第一次更新---------
>ThreadLocal类，一个神奇的小工具。</br>
有时候，我们在一个线程里需要将同一个变量传递给不同的函数，也就是需要实现一个变量的多重操作。此时我们多么希望它是一个全局变量呀。然而并没有，于是我们只能苦逼地一一传参T_T。
自从有了ThreadLocal，为每一个线程创建自己的变量小天地，在local类实例中定义过的变量，可以在线程内部自由穿梭，如同全局一般。一旦出了这个线程，它就不见啦，所以也不会打扰到别的线程。
嘿嘿嘿。

欲知效果如何，请戳[threadlocal类特性小测试](https://github.com/wanzifa/Review_Python/blob/master/threadlocal%E7%B1%BB%E7%9A%84%E7%89%B9%E6%80%A7.py)
