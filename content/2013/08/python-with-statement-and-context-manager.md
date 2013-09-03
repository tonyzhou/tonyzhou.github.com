Title: Python with语句和context manager
Date: 2013-08-07 16:57
Category: Python
Tags: python 
Slug: python with statement and context manager
Author: Tony Zhou
Summary: 资源管理是编码的一大话题， 很多语言都有专门的特性用于保证资源的合理创建和释放。比如利用C++的确定性析构， 封装一个RAII对象： 用对象的生命周期来控制资源的释放。

##Python with语句的引入

资源管理是编码的一大话题， 很多语言都有专门的特性用于保证资源的合理创建和释放。比如利用C++的确定性析构， 封装一个RAII对象： 用对象的生命周期来控制资源的释放。关于RAII，详细的介绍请见：http://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization

对Python来说，管理资源分配和释放常用的做法有try/finally:

``` python
set things up
try:
    do something
finally:
    tear things down
```

try/finally块经常出现在编码中，因此有必要考虑复用这部分功能，可以用一个函数封装：

``` python
def controlled_execution(callback):
    set things up
    try:
        callback(thing)
    finally:
        tear things down

def my_function(thing):
    do something

controlled_execution(my_function)
```

这种封装方式有很多弊端： 执行体(do something部分)被放在一个函数中，作用域被隔离了，不能使用当前作用域的局部变量， 非常不方便。 进一步优化，可以利用python的generator解决作用域隔离问题：

``` python
def controlled_execution():
    set things up
    try:
        yield thing
    finally:
        tear things down

for thing in controlled_execution():
    do something with thing
```

这样做虽然解决了问题，但看起来还是非常怪异，因为执行体(do something部分)只需要执行一次，我们却把它放入一个循环中，这样不利于代码的理解。
对此，python2.5中引入了新特性——context manager 和 with statement， 使用类去封装资源的分配和释放操作，用with语句去划定资源的生存范围。

``` python
class controlled_execution:
    def __enter__(self):
        set things up
        return thing
    def __exit__(self, type, value, traceback):
        tear things down

with controlled_execution() as thing:
     some code
```

with的执行流程是这样的： 每次执行controller_execution，会返回一个对象，这个对象被赋给thing，with语句会对thing自动执行一次__enter__，在with区块执行完毕之后，__exit__也会被自动调用。因此能保证资源的合理初始化和释放。
在这里，thing对象被称作context managers， 它代表了with块运行时上下文信息。controller_execution类被称作context manager class，它必须实现__enter__/__exit__函数对(context manager protocol)。


##更多用法

除了context manager protocol， python还提供了contextlib，这是一种更简单的定义context manager的方法，具体用法请查看：http://docs.python.org/2/library/contextlib.html#module-contextlib


##附录

* effbot博客——[理解pythonwith语句](http://effbot.org/zone/python-with-statement.htm)

* PEP343——[with语句](http://www.python.org/dev/peps/pep-0343/)

* python [contextlib文档](http://docs.python.org/2/library/contextlib.html#module-contextlib)


