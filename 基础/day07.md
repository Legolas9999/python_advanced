# Python文件操作与异常处理

# 一、文件的概念

## 1、什么是文件

内存中存放的数据在计算机关机后就会消失。要长久保存数据，就要使用硬盘、光盘、U 盘等设备。为了便于数据的管理和检索，引入了==“文件”==的概念。

一篇文章、一段视频、一个可执行程序，都可以被保存为一个文件，并赋予一个文件名。操作系统以文件为单位管理磁盘中的数据。一般来说，==文件可分为文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别。==

![image-20210315171013811](media/image-20210315171013811.png)

## 2、思考：文件操作包含哪些内容呢？

在日常操作中，我们对文件的主要操作：创建文件、打开文件、文件读写、文件备份等等

![image-20210315171310117](media/image-20210315171310117.png)

## 3、文件操作的作用

文件操作的作用就是==把一些内容(数据)存储存放起来==，可以让程序下一次执行的时候直接使用，而不必重新制作一份，省时省力。

# 二、文件的基本操作

## 1、文件操作三步走

① 打开文件

② 读写文件

③ 关闭文件

## 2、open函数打开文件

在Python，使用open()函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下：

```python
f = open(name, mode)
注：返回的结果是一个file文件对象（后续会学习，只需要记住，后续方法都是f.方法()）
```

name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。

mode：设置打开文件的模式(访问模式)：只读r、写入w、追加a等。

> r模式：代表以只读模式打开一个已存在的文件，后续我们对这个文件只能进行读取操作。如果文件不存在，则直接报错。另外，r模式在打开文件时，会将光标放在文件的第一行（开始位置）。

> w模式：代表以只写模式打开一个文件，文件不存在，则自动创建该文件。w模式主要是针对文件写入而定义的模式。但是，要特别注意，w模式在写入时，光标也是置于第一行同时还会清空原有文件内容。

> a模式：代表以追加模式打开一个文件，文件不存在，则自动创建该文件。a模式主要也是针对文件写入而定义模式。但是和w模式有所不同，a模式不会清空文件的原有内容，而是在文件的尾部追加内容。

文件路径：① 绝对路径 ② 相对路径

① 绝对路径：绝对路径表示绝对概念，一般都是从盘符开始，然后一级一级向下查找（不能越级），直到找到我们要访问的文件即可。

比如访问C盘路径下的Python文件夹下面的python.txt文件，其完整路径：

```powershell
Windows
C:\Python\python.txt
Linux
/usr/local/nginx/conf/nginx.conf
```

> 绝对路径一般路径固定了，文件就不能进行移动，另外在迁移过程中会比较麻烦。



② ==相对路径==：相对路径表示相对概念，不需要从盘符开始，首先需要找到一个参考点（就是Python文件本身）

同级关系：我们要访问的文件与Python代码处于同一个目录，平行关系，同级关系的访问可以使用`./文件名称`或者直接写`文件名称`即可

上级关系：如果我们要访问的文件在当前Python代码的上一级目录，则我们可以通过`../`来访问上一级路径（如果是多级，也可以通过../../../去一层一层向上访问

下级关系：如果我们要访问的文件在与Python代码同级的某个文件夹中，则我们可以通过`文件夹名称/`来访问某个目录下的文件

## 3、write函数写入文件

基本语法：

```python
f.write('要写入的内容，要求是一个字符串类型的数据')
```

## 4、close函数关闭文件

```python
f.close()
```

## 5、入门级案例

```python
# 1、打开文件
f = open('python.txt', 'w')
# 2、写入内容
f.write('人生苦短，我学Python！')
# 3、关闭文件
f.close()
```

> 强调一下：中文乱码问题，默认情况下，计算机常用编码ASCII、GBK、UTF-8

## 6、解决写入中文乱码问题

```python
# 1、打开文件
f = open('python.txt', 'w', encoding='utf-8')
# 2、写入内容
f.write('人生苦短，我学Python！')
# 3、关闭文件
f.close()
```

## 7、文件的读取操作

`read(size)方法`：主要用于文本类型或者二进制文件（图片、音频、视频...）数据的读取

size表示要从文件中读取的数据的长度（单位是字符/字节），如果没有传入size，那么就表示读取文件中所有的数据。

```python
f.read()  # 读取文件的所有内容
f.read(1024)  # 读取1024个字符长度文件内容，字母或数字
```

```python
# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、使用read()方法读取文件所有内容
contents = f.read()
print(contents)
# 3、关闭文件
f.close()
```

`readlines()方法`：主要用于文本类型数据的读取

readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。

```python
# 1、打开文件
f = open('python.txt', 'r', encoding='utf-8')
# 2、读取文件
lines = f.readlines()
for line in lines:
    print(line, end='')
# 3、关闭文件
f.close()
```

`readline()方法`：一次读取一行内容，每运行一次readline()函数，其就会将文件的指针向下移动一行

```python
f = open('python.txt’)

while True:
   # 读取一行内容
   content = file.readline()
   # 判断是否读取到内容
   if not content:
       break
   # 如果读取到内容，则输出
   print(content)

# 关闭文件
f.close()
```

## 8、聊聊文件操作的mode模式

| **模式** | **描述**                                                     |
| -------- | ------------------------------------------------------------ |
| r        | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb       | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 |
| r+       | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+      | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w        | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb       | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+       | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+      | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a        | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab       | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+       | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+      | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

> 虽然mode文件操作模式很多，但是我们只需要记住3个字符即可。r、w、a

> r+、w+、a+，代加号，功能全，既能读，又能写（区别在于指针到底指向不同）

> rb、wb、ab，代b的字符，代表以二进制的形式对其进行操作，适合读取文本或二进制格式文件，如图片、音频、视频等格式

> rb+、wb+、ab+，代加号，功能全，既能读，又能写（区别在于指针到底指向不同）

# 三、文件备份案例

## 1、案例需求

需求：用户输入当前目录下任意文件名，完成对该文件的备份功能(备份文件名为xx[备份]后缀，例如：(test[备份].txt)。



实现思路：

① 接收用户输入的文件名

② 规划备份文件名

③ 备份文件写入数据

## 2、代码实现

```python
# 1、接收用户输入的文件名（要备份的文件名）
oldname = input('请输入要备份的文件名称：')  # python.txt
# 2、规划备份文件名（python[备份].txt）
# 搜索点号
index = oldname.rfind('.')
# 返回文件名和文件后缀
name = oldname[:index]
postfix = oldname[index:]
newname = name + '[备份]' + postfix
# 3、对文件进行备份操作
old_f = open(oldname, 'rb')
new_f = open(newname, 'wb')

# 读取源文件内容写入新文件
while True:
    content = old_f.read(1024)
    if not content:
        break
    new_f.write(content)
# 4、关闭文件
old_f.close()
new_f.close()
```

# 四、文件和文件夹操作

## 1、os模块

在Python中文件和文件夹的操作要借助os模块里面的相关功能，具体步骤如下：

第一步：导入os模块

```python
import os
```

第二步：调用os模块中的相关方法

```python
os.函数名()
```

## 2、与文件操作相关方法

| **编号** | **函数**                          | **功能**             |
| -------- | --------------------------------- | -------------------- |
| 1        | os.rename(旧文件名称，新文件名称) | 对文件进行重命名操作 |
| 2        | os.remove(要删除文件名称)         | 对文件进行删除操作   |

案例：把Python项目目录下的python.txt文件，更名为linux.txt，休眠20s，刷新后，查看效果，然后对这个文件进行删除操作。

```python
# 第一步：导入os模块
import os
# 第三步：引入time模块
import time


# 第二步：使用os.rename方法对python.txt进行重命名
os.rename('python.txt', 'linux.txt')

# 第四步：休眠20s
time.sleep(20)

# 第五步：删除文件（linux.txt)
os.remove('linux.txt')
```

## 3、与文件夹操作相关操作

前提：

```python
import os
```

相关方法：

| **编号** | **函数**                 | **功能**                                    |
| -------- | ------------------------ | ------------------------------------------- |
| 1        | os.mkdir(新文件夹名称)   | 创建一个指定名称的文件夹                    |
| 2        | os.getcwd()              | current  work   directory，获取当前目录名称 |
| 3        | os.chdir(切换后目录名称) | change  directory，切换目录                 |
| 4        | os.listdir(目标目录)     | 获取指定目录下的文件信息，返回列表          |
| 5        | os.rmdir(目标目录)       | 用于删除一个指定名称的"空"文件夹            |

案例1：

```python
# 导入os模块
import os


# 1、使用mkdir方法创建一个images文件夹
if not os.path.exists('images'):
	os.mkdir('images')

if not os.path.exists('images/avatar')
    os.mkdir('images/avatar')

# 2、getcwd = get current work directory
print(os.getcwd())

# 3、os.chdir，ch = change dir = directory切换目录
os.chdir('images/avatar')
print(os.getcwd())

# 切换到上一级目录 => images
os.chdir('../../')
print(os.getcwd())

# 4、使用os.listdir打印当前所在目录下的所有文件，返回列表
print(os.listdir())

# 5、删除空目录
os.rmdir('images/avatar')
```

案例2：准备一个static文件夹以及file1.txt、file2.txt、file3.txt三个文件

① 在程序中，将当前目录切换到static文件夹

② 创建一个新images文件夹以及test文件夹

③ 获取目录下的所有文件

④ 移除test文件夹

```python
# 导入os模块
import os

# ① 在程序中，将当前目录切换到static文件夹
os.chdir('File')
# print(os.getcwd())

# ② 创建一个新images文件夹以及test文件夹
if not os.path.exists('images'):
    os.mkdir('images')

if not os.path.exists('test'):
    os.mkdir('test')

# ③ 获取目录下的所有文件
# print(os.listdir())
for file in os.listdir():
    print(file)

# ④ 移除test文件夹
os.rmdir('test')
```

## 4、文件夹删除补充（递归删除、慎重！）

```python
# 导入shutil模块
import shutil

# 递归删除非空目录
shutil.rmtree('要删除文件夹路径')
```

> 递归删除文件夹的原理：理论上，其在删除过程中，如果文件夹非空，则自动切换到文件夹的内部，然后把其内部的文件，一个一个删除，当所有文件删除完毕后，返回到上一级目录，删除文件夹本身。

## 5、普及路径的小知识

绝对路径：从盘符开始，一级一级向下移动，不能越级

```python
D:\PycharmProjects\pythonProject\static
```

缺点：不适合迁移



相对路径：以当前正在运行的工作目录作为参考点

① 同级路径，都在同一个文件夹中，兄弟关系，如static目录下有file1.txt和file2.txt，则file1.txt和file2.txt就是同级关系，==同级访问直接使用名称即可或者使用./文件名称==。

② 下一级路径，我们的文件与另外一个文件存在上下级关系，如images文件夹中存在一个avatar文件夹，则images是上级目录，avatar是下级目录。==则我们访问avatar可以通过images/avatar来实现==。

③ 上一级路径，如果我们某些时候，向从当前目录下，跳出到外一层路径，我们可以使用==../==来实现。

#五、Python异常

## 1、什么是异常

当检测到一个错误时，解释器就无法继续执行了，反而出现了一些错误的提示，这就是所谓的"异常"。

> 特别强调：异常并不是错误，有所不同的。异常往往是由于输入信息异常或者未知的结果导致程序无法执行！

## 2、异常演示

```python
# 除数为0
# print(10/0)

# 文件读取异常
f = open('python.txt', 'r')
content = f.readlines()
print(content)
```

## 3、异常捕获

基本语法：

```python
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
```

> try...except主要用于捕获代码运行时异常，如果异常发生，则执行except中的代码

案例：

```python
try:
    f = open('python.txt', 'r')
    content = f.readline()
    print(content)
except:
    f = open('python.txt', 'w', encoding='utf-8')
    f.write('发生异常，执行except语句中的代码')
f.close()
```

## 4、捕获异常并输出错误信息

无论我们在except后面定义多少个异常类型，实际应用中，也可能会出现无法捕获的未知异常。这个时候，我们考虑使用Exception异常类型捕获可能遇到的所有未知异常：

```python
try:
    可能遇到的错误代码
except Exception as e:
    print(e)
```

案例：打印一个未定义变量，使用Exception异常类进行捕获

```python
try:
    print(name)
except Exception as e:
    print(e)
```

## 5、异常捕获中else语句

else语句：表示的是如果没有异常要执行的代码。

```python
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('哈哈，真开森，没有遇到任何异常')
```

案例：

```python
try:
    f = open('python.txt', 'r')
except Exception as e:
    print(e)
else:
    content = f.readlines()
    print(content)
    f.close()
```

## 6、异常捕获中的finally语句

finally表示的是无论是否异常都要执行的代码，例如关闭文件

```python
try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    content = f.readlines()
    print(content)
finally:
    f.close()
```

# 六、Python内置模块

## 1、什么是Python模块

Python 模块(Module)，是一个==Python 文件==，以 .py 结尾，包含了 Python 对象定义和Python语句。模块能定义==函数，类和变量==，模块里也能包含可执行的代码。

```python
import os		=>     os.py
import time	    =>     time.py

os.mkdir('Python')
```

## 2、模块的分类

在Python中，模块通常可以分为两大类：==内置模块(目前使用的)== 和 ==自定义模块==

## 3、模块的导入方式

☆ import 模块名

☆ import 模块名 as 别名

☆ from 模块名 import *

☆ from 模块名 import 功能名

## 4、使用import导入模块

基本语法：

```python
import 模块名称
或
import 模块名称1, 模块名称2, ...
```

使用模块中封装好的方法：

```python
模块名称.方法()
```



案例：使用import导入math模块

```python
import math

# 求数字9的平方根 = 3
print(math.sqrt(9))
```

案例：使用import导入math与random模块

```python
import math, random

print(math.sqrt(9))
print(random.randint(-100, 100))
```

> 普及：我们在Python代码中，通过import方式导入的实际上都是文件的名称

## 5、使用as关键字为导入模块定义别名

在有些情况下，如导入的模块名称过长，建议使用as关键字对其重命名操作，以后在调用这个模块时，我们就可以使用别名进行操作。

```python
import time as t

# 调用方式
t.sleep(10)
```

> 在Python中，如果给模块定义别名，命名规则建议使用大驼峰。

## 6、使用from...import导入模块

提问：已经有了import导入模块，为什么还需要使用from 模块名 import 功能名这样的导入方式？

答：import代表导入某个或多个模块中的所有功能，但是有些情况下，我们只希望使用这个模块下的某些方法，而不需要全部导入。这个时候就建议采用from 模块名 import 功能名

### ☆ from 模块名 import *

这个导入方式代表导入这个模块的所有功能（等价于import 模块名）

```python
from math import *
```

### ☆ from 模块名 import 功能名（推荐）

```python
from math import sqrt, floor
```



注意：以上两种方式都可以用于导入某个模块中的某些方法，但是在调用具体的方法时，我们只需要`功能名()`即可

```python
功能名()
```



案例：

```python
# from math import *
# 或
from math import sqrt, floor

# 调用方式
print(sqrt(9))
print(floor(10.88))
```

## 7、扩展：time模块中的time()方法

在Python中，time模块除了sleep方法以外，还有一个方法叫做time()方法

```python
time.time()
```

主要功能：就是返回格林制时间到当前时间的秒数（时间戳）



案例：求循环代码的执行时间

```python
import time

# 返回：格林制时间到当前时间的秒数
start = time.time()

# 编写一个循环
list1 = []
for i in range(1000000):
    list1.append(i)

end = time.time()
print(f'以上代码共执行了{end - start}s')
```



# 七、扩展：Python中的自定义模块

## 1、什么是自定义模块

在Python中，模块一共可以分为两大类：内置系统模块  和  自定义模块

模块的本质：在Python中，模块的本质就是一个Python的独立文件（后缀名.py），里面可以包含==全局变量、函数以及类==。

> 注：在Python中，每个Python文件都可以作为一个模块，模块的名字就是==文件的名字==。也就是说自定义模块名必须要符合标识符命名规则。

> 特别注意：我们在自定义模块时，模块名称不能为中文，不能以数字开头，另外我们自定义的模块名称不能和系统中自带的模块名称(如os、random)相冲突，否则系统模块的功能将无法使用。比如不能定义一个叫做os.py模块

## 2、定义一个自定义模块

案例：在Python项目中创建一个自定义文件，如my_module1.py

```python
def sum_num(num1, num2):
   	return num1 + num2
```

## 3、导入自定义模块

```python
import 模块名称
或
from 模块名称 import 功能名
```

案例：

```python
import my_module1


# 调用my_module1模块中自定义的sum_num方法
print(my_module1.sum_num(10, 20))
```

## 4、测试模块

在我们编写完自定义模块以后，最好在模块中对代码进行提前测试，以防止有任何异常。

测试需求：

① 要求我们可以直接在模块文件中对代码进行直接测试

② 代码测试完毕后，当导入到其他文件时，测试代码要自动失效



引入一个魔术变量：`__name__`，其保存的内容就是一个==字符串类型==的数据。

==随着运行页面的不同，其返回结果也是不同的：==

① 如果`__name__`是在当前页面运行时，其返回结果为`__main__`

② 如果`__name__`在第三方页面导入运行时，其返回结果为模块名称（文件名称）

基于以上特性，我们可以把`__name__`编写在自定义模块中，其语法如下：

```python
if __name__ == '__main__':
    # 执行测试代码
```

> 以上代码主要出现在自定义模块中，主要用于实现代码测试

## 5、模块命名的注意事项

> 在实际项目开发中，一定要特别注意：我们自定义的模块名称一定不能和系统内置的模块名称相同，否则会导致代码无法正常执行。

举个栗子：定义一个与系统内置模块同名的模块

random.py

```python

```

08-Python中引入与系统模块同名的自定义模块.py

```python
import random

print(random.randint(-100, 100))
```

以上代码运行结果：

![image-20210319113537997](media/image-20210319113537997.png)

randint属于random模块的内置方法，不可能存在找不到的情况。之所以出现以上问题的主要原因在于：我们的项目中存在了一个与系统模块同名的模块文件。所以其在引用random模块式，其执行顺序：

`引入某个模块 => 当前项目中寻找是否有同名的文件 => 如果找到则直接使用，未找到 => 继续向上寻找 => Python解析器中`

如何证明：模块的引用一定是按照你说的这个顺序呢？

答：使用`__file__`魔术变量

```python
print(random.__file__)
```

# 
