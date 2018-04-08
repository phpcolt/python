#coding=utf-8
'''

查询全部数据，存入在list1中

'''
list1 = []
def all_select():
    with open('sql.txt','r',encoding="utf-8") as f:
        for i in f.readlines():
            #print(i)
            s = i.strip().split(',')
            list1.append(s)




'''

判断是什么查询语句

'''
def judge(args):
    s = args.strip().split(' ')
    return s[0],s[1],s[len(s)-3],s[len(s)-2],s[len(s)-1]


'''
为了增加一个数据调用
'''
def add_stuff(args):
    s = args.strip().split(' ')
    return s


'''
查询结果：
'''
def select(args):
    count = 0
    if args[2] == 'age':
        #count = 0
        for i in list1:
            if i[2] > args[4]:
                count += 1
                print(i[1],i[2])
        print("影响了%s条记录"%count)
    elif args[4] == '"IT"':
        for i in list1:
            if i[4] == 'IT':
                count += 1
                print(i)
        print("影响了%s条记录" % count)
    elif args[2] == 'enroll_date':
        for i in list1:
            img_list2 = i[len(i) - 1].split('-')
            #print(img_list2)
            if eval(args[4]) in img_list2:
                count += 1
                print(i)
        print('影响了%s条记录' % count)
    else:
        print("不支持其他查询")



'''

增加员工
'''
def add(args):

    del args[0]
    del args[1]
    s = ','.join(args)
    s1 = s.strip().split(',')
    number = len(list1) +1
    s1.insert(0,number)
    list1.append(s1)
    print(list1)


'''
删除员工

'''
def delete(args):
    count = 0
    s = args[len(args)-1]
    s1 = s.strip().split('=')
    print(s1)
    for key,i in enumerate(list1):
        if int(i[0]) == int(s1[1]):
            del list1[key]
    count += 1
    print('影响了%s条记录' % count)
    print(list1)



'''
更新员工信息
'''
def update(args):
    # count = 0
    # print(args)
    # strs3 = args[len(args)-1]
    # str2 = args[len(args)-2] + ' ' +args[len(args)-1]
    # print(str2)
    # for i in list1:
    #     if eval(strs3) in i and eval(strs3) == 'IT':
    #         count += 1
    #         s = i.index(eval(strs3))
    #         i[s] = 'Market'
    #         print(i)
    #     # elif eval(str2) in i:
    #     #     count += 1
    #     #     s = i.index(eval(str2))
    #     #     i[s] = ''
    # print('影响了%s条记录' % count)
    #print(args)
    count = 0
    li2 = ['id','name','age','phone','dept','enroll_date']
    li1 = args.strip().split(' ')
    s = li1.index('SET')
    strs = li1[s+1]
    #print(strs)
    s1 = li1.index('WHERE')
    strs1 = li1[s1+1:]
    #print(strs1)
    length = strs1.index('=')
    s2 = ' '.join(strs1[length+1:])
    #print(s2)
    for i in list1:
        if eval(s2) in i :
            #print(i)
            new_str = strs.split('=')
            #print(new_str[0])
            if new_str[0] in li2 :
                count += 1
                s5 = li2.index(new_str[0])
                i[s5] = new_str[1]
                print(i)
    print('影响了%s条记录' % count)



while True:
    keyword = input("用户请输入查询语句:")
    all_select()
    if len(keyword) > 0:
        s = judge(keyword)
        if s[0] == 'find':
            #print(s)
            select(s)
        elif s[0] == 'del':

            delete(s)
        elif s[0] == 'add':
            count = 0
            value = add_stuff(keyword)
            add(value)
            count += 1
            print('影响了%s条记录' % count)
            #print(value)
        elif s[0] == 'UPDATE':

            update(keyword)
        else:
            print("只支持这几种查询方法")


    else:
        print("亲，您没有输入内容。")
        strs = input("您想继续（c）还是退出 q ,不要那么无聊就可以了")
        if strs == 'c':
            continue
        elif strs == 'q':
            print('bye')
            break
        else:
            print("能不能输入正规点")
            break