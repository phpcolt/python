#coding=utf-8
import os
if os.path.exists("4.txt"):
    i = 0
    while True:
        username = input("请输入您的用户名：")
        password = input("请输入您的密码")
        #f = open("4.txt",'r+',encoding="utf-8")
        with open("4.txt",'r+',encoding="utf-8") as f:
            s = f.read()
        strs = username+' '
        if username not in s:

            if (username == "root" and password == '123456') or (username == 'root1' and password == '123456') :
                print("登陆成功")
                break
            else:
                print("登陆失败")
                i += 1
                if i == 3:
                    f.write(strs)
                    f.close()
                    break
                continue
        else:
            print("你的账号由于错误了很多次禁止登陆")
            break
else:
    print("文件不存在")
