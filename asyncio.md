# 同步IO 和 异步IO
- 同步IO就是指IO操作开始后，线程必须等待IO操作结束后拿到结果。
- 异步IO就是指IO操作开始后，线程可以不必等待IO操作的结果，而是等IO操作结束后由系统通知IO操作结束，再回来处理结果。

异步IO的核心就是对IO操作的调度。

# 使用asyncio定义协程
## 使用装饰器
```python
import asyncio
from collections import Generator, Coroutine

@asyncio.coroutine
def hello():
    pass

coro = hello()


print(isinstance(coro,Coroutine))  # False
print(isinstance(coro,Generator))  # True
```

使用装饰器来定义协程，本质上是将函数对象标记为协程对象。本质上还是一个生成器。
只是标记后可以作为协程使用

## 使用asyncio 原生定义
```python
import asyncio
from collections import Generator, Coroutine

#async关键字
async def hello():
    print('hello')

#创建协程对象，但并不执行函数内的内容
coro = hello()

print(isinstance(coro,Coroutine))  # True
```
这种方法定义的协程，没有实现`__iter__`和`__next__`,所以不是生成器，不可迭代

# asyncio框架的概念

## event_loop
事件循环。<br>asyncio中开启的一个无限的事件循环，asyncio 会自动在满足条件时去调用相应的协程对象，我们只需要将协程对象注册到该事件循环上即可。

## coroutine
协程对象。<br>指一个用async 来定义的函数，它在调用时不会立即执行，而是返回一个协程对象。协程对象需要注册到事件循环，由事件循环进行调用。

## future
代表将来执行或没有执行的任务的结果。它和我们下面要讲的task对象没有本质区别。

## task
一个协程对象就是一个原生可以挂起的函数，而任务则是对协程的进一步封装，其中包含任务的各种状态。taks 对象是future对象的子类，它可以将corotutine和future联系在一起，将corotutine封装为一个future对象。

## async/await 关键字
python3.5之后用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口，其作用类似于yield.

# 协程的工作流程
- 定义/创建协程对象
- 定义事件循环对象容器
- 将协程转为task任务
- 将task扔进循环对象中触发
 
 ```python
 import asyncio

# 定义协程对象
async def hello(name):
    print('hello', name)

# 创建协程对象
coro = hello('world')

# 获取事件循环对象容器
loop = asyncio.get_event_loop()

# 将协程对象转化为task(下面两种方式二选一)
task = loop.create_task(coro)
task = asyncio.ensure_future(coro)

# 将task任务扔进事件循环对象中触发
loop.run_until_complete(task)
 ```
## 获取协程的工作结果
### tsak.result() 直接取得结果
```python
import asyncio, time

async def hello(x):
    # time.sleep(x)  # time.sleep是一个同步操作语句，无法达到异步的结果
    await asyncio.sleep(x)
    return '暂停了{}秒'.format(x)

coro = hello(4)
loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coro)
loop.run_until_complete(task)

# 通过task.result()获取返回结果
print('返回结果是：{}'.format(task.result()))
```

### 使用回调函数
```python
async def hello(x):
    # time.sleep(x)  # time.sleep是一个同步操作语句，无法达到异步的结果
    await asyncio.sleep(x)
    return x

def callback(future):
    sum = 10 + future.result()
    print('回调返回结果相加的值为：', sum)

coro = hello(4)
loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coro)
#绑定回调函数
task.add_done_callback(callback)
loop.run_until_complete(task)
```

# 协程中的并发 

```python
import asyncio, time

# 定义协程
async def do_some_work(x):
    print('等待：', x)
    await asyncio.sleep(x)   # 模拟一个等待耗时操作
    return '等待时间: {}'.format(x)

if __name__ == '__main__':
    start = time.time()
    # 创建多个协程对象
    coro1 = do_some_work(1)
    coro2 = do_some_work(2)
    coro3 = do_some_work(3)

    # 将协程对象转换为task，并组成一个list
    tasks = [
        asyncio.ensure_future(coro1),
        asyncio.ensure_future(coro2),
        asyncio.ensure_future(coro3)
    ]

    # 将tasks注册到事件循环中
    # 两种方法：asyncio.wait，asyncio.gather

    loop =  asyncio.get_event_loop()

    #以下二选一
    loop.run_until_complete(asyncio.wait(tasks))  # wait方法只接受列表作为参数
    loop.run_until_complete(asyncio.gather(*tasks))   # gather方法接收不定量参数，所以要解包

    for task in tasks:
        print('任务返回的结果是：', task.result())

    print('总的运行时间为：', time.time()-start)  #3s

```