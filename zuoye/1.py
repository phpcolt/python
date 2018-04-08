#coding=utf-8
#user = input("please input you username:")
#passwd = input("please input you password:")
"""
 一／编译性语言和解释性语言

编译性语言是解析过程中将语言转换成机器语言
解析性语言是源代码不是直接翻译成机器语言，而是先翻译成中间代码，再由解释器对中间代码进行解释运行。
编译性语言c＋＋ java 等
解释性语言：php   python等


二／执行python的两种方式
答：一种是shell编辑器调用  另外一种是解释器调用

三／Pyhton 单行注释和多行注释分别用什么?
单行注释用＃
多行注释用三个冒号开始，三个冒号结尾

四／布尔值分别有什么?
答  True和False

五／声明变量注意事项有那些?
声明变量不要以数字开头。命名要规范，变量也要规范

六／如何查看变量在内存中的地址?
答：通过id可以查看变量的内存地址

#第7题1小题
user_name = input("请输入您的名字： ")
user_password = input("请输入您的密码： ")
if user_name == 'seven' and user_password == '123':
    print("登陆成功")
else:
    print("登陆失败")

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

username = "seven"
password = "123"
count = 0
while count < 3:
    user = input("please input you username:")
    passwd = input("please input you password:")
    if user == username and passwd == password:
        print("登陆成功")
        break
    else:
        print("用户名或者密码错误")

    count += 1
    if count == 3:
        go_on = input("please input you y or n:")
        if go_on == 'y':
            count = 0


------------------------------------------------------
username = "seven"
username1 = 'alex'
password = "123"
count = 0
while count < 3:
    user = input("please input you username:")
    passwd = input("please input you password:")
    if  user == username or user == username1:
        if passwd == password:
            print("登陆成功")
            break
        else:
            print("登陆失败")

    count += 1
    if count == 3:
        go_on = input("please input you y or n:")
        if go_on == 'y':
            count = 0

-----------------------------------------
count = 0
sum = 0
while count < 100:
    count += 1
    sum += count
print(sum)

-----------------------------------------
count = 0

while count < 100:
    count += 1

    if count == 6:
        pass
        continue
    elif count == 10:
        pass
        continue
    elif count > 12:
        pass
        continue
    else:
        print(count)

--------------------------------------------
count = 100
while count <= 100 and count >= 50:
    print(count)
    count -= 1




-----------------------------------------
count = 0
while count <= 100:
    if count % 2 == 1:
        print(count)

    count += 1



-----------------------------------------

count = 0
while count <= 100:
    if count % 2 == 0:
        print(count)

    count += 1



----------------------

n1和n2

答：123456是将值赋给你了n1，n2取了n1值的地址

----------------------

name = input("please input your name:")
address  = input("please input your address")
like = input("please input your like")
info ="敬爱的%s，最喜欢在%s地方干%s"  %(name,address,like)
print(info)



－－－－－－－－－－－－－－－－－－－－－－

year = int(input("please input year:"))
if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
    print("闰年",year)
else:
    print("不是闰年")


---------------------
benjin = 10000
lx = 0.0325
year_lr = benjin * lx

time = benjin // year_lr
print(time)



-----------------------------------------
count = 0

while count < 3:
    username = input("please input username:")
    password = input("please input password:")
    if username == 'user' and password == '123':
        print("登录成功",username)
    else:
        print("登陆失败")

    count += 1

"""

count = 0
turn = True
while count <=3  and  turn == True:
    username = input("please input username:")
    password = input("please input password:")
    if username == 'user' or username == 'usr2' or username == 'usr3':
        if password == "123":
            print("登陆成功")
            break
        else:
            print("用户名错误")

    count += 1
    if count == 3:
        turn = False
        print("用户被锁定")


