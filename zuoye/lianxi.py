#coding=utf-8
i = 0
li = []
s = {}
'''
登陆判断
'''
def login(username,password):
    username = username.strip()
    password = password.strip()
    with open('test.txt', 'r+', encoding="utf-8") as f:
        for line in f.readlines():
            s = line.strip()
            str1 = ' '.join(s.split())
            str2 = str1.replace(' ',',')
            li.append(str2)
        del li[0]
        for key,value in enumerate(li):

            if username in value:
                arr = value.split(',')
                if password == arr[1] and username == arr[0]:
                    return True


'''
根据数字找寻出结果

'''

def find(username):
    for key,value  in enumerate(li):
        if username in value:
            return li[key]


# s = login('alex','abc123')
# print(s)
'''
修改密码

'''
def update_pass(username,password):
    for key,value  in enumerate(li):
        if username in value:
            info_list = li[key].strip(',').split(',')
            info_list[1] = password
            li[key] = ','.join(info_list)
            return li[key]

'''
修改个人信息
'''

def update(username,name):
    for key,value  in enumerate(li):
        if username in value:
            info_list = li[key].strip(',').split(',')
            info_list[0] = name
            li[key] = ','.join(info_list)
            return li[key]



while True:
    username = input("用户名:")
    password = input("密码：")
    s = login(username,password)

    if s == True:
        print("登陆成功")
        while True:
            print("1 打印个人信息")
            print("2 修改个人信息")
            print("3 修改密码")
            number = input("请输入你的数字")
            if number.isdigit():
                if int(number) == 1:
                    s = find(username)
                    print(s)
                elif int(number) == 2:
                    name = input("输入用户名")
                    s = update(username,name)
                    print(s)
                elif int(number) == 3:
                    #print("修改密码")
                    passwd = input("输入密码")
                    s = update_pass(username,passwd)
                    print(s)
                else:
                    print("你不要那么任性")

            else:
                print("请输入数字")

    else:
        print("用户名或者密码错误")
        i += 1
        if i > 3:
            print("登陆次数过多，请稍后再试")
            break