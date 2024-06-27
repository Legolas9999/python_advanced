# 使用Python函数编写通讯录系统

# 1、查看通讯录系统最终效果

![image-20210313174341286](media/image-20210313174341286.png)

# 2、需求分析

需求：进入系统显示系统功能界面，功能如下：

① 添加学员信息

② 删除学员信息

③ 修改学员信息

④ 查询学员信息(只查询某个学员)

⑤ 遍历所有学员信息

⑥ 退出系统

系统共6个功能，用户根据自己需求选取

# 3、功能实现步骤

① 显示功能界面

② 用户输入功能序号

③ 根据用户输入的功能序号，执行不同的功能(函数)

☆ 定义函数

☆ 调用函数

# 4、模块化的编程思想（面向过程）

模块化的编程思想是最早期的编程思想，其强调==把一个系统分解为若干个功能（步骤）==，每个功能就是一个模块（函数）。当所有功能开发完毕后，功能整合，则系统就完成了。

# 5、使用Python开发通讯录管理系统

① 显示功能界面

② 提示用户输入要操作的功能编号

③ 根据用户输入的序号执行相关功能 => if...elif...else

④ 如何让程序一直执行下去，而不是选择某个功能后，程序就退出了 => while True

⑤ 根据用户输入的序号，完成系统中的每一个功能

⑥ 扩展功能：把学生信息保存在文件中

```python
# 6、定义一个全局列表，用于保存所有学员信息
students = []

# 1、定义一个menu函数，用于显示功能菜单
def menu():
    print('-' * 40)
    print('学生管理系统 V1.0')
    print('[1] 添加学生信息')
    print('[2] 删除学生信息')
    print('[3] 修改学生信息')
    print('[4] 查询学生信息')
    print('[5] 遍历所有学生信息')
    print('[6] 保存数据到文件')
    print('[7] 退出系统')
    print('-' * 40)

# 5、定义一个add_student函数，用于添加学生信息
def add_student():
    # 接收要输入学生的信息
    name = input('请输入要添加学生的姓名：')
    age = int(input('请输入要添加学生的年龄：'))
    mobile = input('请输入要添加学生的电话：')
    # 创建一个空字典
    student = {}
    student['name'] = name
    student['age'] = age
    student['mobile'] = mobile
    # 声明全局列表
    global students
    students.append(student)
    print(f'学生{name}信息添加成功')

# 7、定义一个get_all_students函数，用于获取所有学生信息
def get_all_students():
    # 声明全局变量
    global students
    # 遍历所有学员信息
    for i in students:
        print(i)

# 8、定义一个del_student函数，用于删除指定的学员信息
def del_student():
    # 提示用户输入要删除学生的姓名
    name = input('请输入要删除学生的姓名：')
    # 遍历所有学员，查看是否有某个学员的name(key)与输入的name值相匹配
    global students
    for i in students:
        if i['name'] == name:
            students.remove(i)
            print(f'学生{name}信息删除成功')
            break
    else:
        print('您要删除的学生信息未找到！')

# 9、定义一个edit_student函数，用于编辑学员的信息
def edit_student():
    # 提示用户输入要编辑学生的姓名
    name = input('请输入要编辑学生的姓名：')
    # 声明全局变量
    global students
    for i in students:
        if i['name'] == name:
            # 提示用户输入要修改的信息
            i['name'] = input('请输入修改后的学生姓名：')
            i['age'] = int(input('请输入修改后的学生年龄：'))
            i['mobile'] = input('请输入修改后的学生电话：')
            # 提示修改成功，然后break
            print(f'学生{name}信息已修改成功')
            break
    else:
        print('您要修改的学员未找到')

# 10、定义一个get_student函数，用于查询某个学员信息
def get_student():
    # 提示用户输入要查询学员的姓名
    name = input('请输入要查询学生的姓名：')
    # 声明全局变量，然后循环遍历
    global students
    for i in students:
        if i['name'] == name:
            # 找到了这个学员
            print(i)
            break
    else:
        print('您要查询的学生信息暂未找到')

# 11、定义save_data_to_file函数，用于保存students数据到data.txt文件
def save_data_to_file():
    # 声明全局变量
    global students
    # 打开文件
    f = open('data.txt', 'w', encoding='utf-8')
    # 写入数据
    f.write(str(students))
    # 关闭文件
    f.close()
    # 弹出提示信息
    print('信息已保存成功！')

# 12、定义load_data函数，用于加载data.txt文件中的内容到students变量中
def load_data():
    print('重置students')
    # 声明全局变量
    global students
    # 打开文件
    f = open('data.txt', 'r', encoding='utf-8')
    # 读取文件
    students = eval(f.read())
    # print(students)
    # 关闭文件
    f.close()


# 调用load_data函数，用于加载保存在文件中的函数
load_data()

# 2、定义一个死循环，用于让系统一直处于运行状态
while True:
    # 调用menu()菜单函数
    menu()
    # 3、提示用户输入要操作的功能编号
    user_num = int(input('请输入您要操作的功能编号：'))
    # 4、根据用户输入功能编号实现对应的功能
    if user_num == 1:
        # 添加学生信息
        add_student()
    elif user_num == 2:
        # 删除学生信息
        del_student()
    elif user_num == 3:
        # 修改学生信息
        edit_student()
    elif user_num == 4:
        # 查询学生信息
        get_student()
    elif user_num == 5:
        # 遍历所有学生的信息
        get_all_students()
    elif user_num == 6:
        # 保存数据到文件
        save_data_to_file()
    elif user_num == 7:
        # 退出系统
        print('退出系统成功，感谢您使用学生管理系统V1.0')
        break
    else:
        # 输入异常
        print('您输入的功能编号不正确，请重新输入')
```

