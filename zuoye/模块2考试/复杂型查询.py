#coding=utf-8
'''
查询全部数据，存入在list1中

'''
import os
list1 = []
list2 = []
sign = ['=','>','<','like']
li2 = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
def all_select():
    with open('sql.txt','r',encoding="utf-8") as f:
        for i in f.readlines():
            #print(i)
            s = i.strip().split(',')
            list1.append(s)
        f.close()

'''

判断是什么查询语句

'''
def judge(args):
    s = args.strip().split(' ')
    return s[0],s[1],s[len(s)-3],s[len(s)-2],s[len(s)-1]

'''

修改数据保存到文本中

'''
def sava(args):
    with open('sql.txt','w',encoding="utf-8") as new_file:
        for i in args:
            s = ','.join(i)+'\n'
            new_file.write(s)
        new_file.close()
    #os.renames('sql.txt','sql_bak.txt')
    #os.renames('sql_bak.txt','sql.txt')





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
    tmp_list  = args.strip().split(' ')
    print(tmp_list)

    s1 = tmp_list.index('where')
    temp = tmp_list[s1+1:]
    if temp[1] in sign:
        length = sign.index(temp[1])
        fh = sign[length]
        if temp[0] in li2:
            s = li2.index(temp[0])
            print(s)
            for j in list1:
                if fh == '>':
                    zh = temp[2].replace('"','')
                    if j[s] > zh:
                        count += 1
                        print(j)
                elif fh == '<':
                    zh = temp[2].replace('"', '')
                    if j[s] < zh:
                        count += 1
                        print(j)
                elif fh == '=':
                    zh = temp[2].replace('"', '')
                    if j[s] == zh:
                        count += 1
                        print(j)
                elif fh == 'like':
                    leb = len(j)
                    date_list = j[leb-1].strip().split('-')
                    zh = temp[2].replace('"', '')
                    if zh in date_list:
                        count += 1
                        print(j)
                else:
                    print("哈哈哈")

        print('影响了%s条记录' % count)





'''

增加员工
'''
def add(args):
    count = 0
    temp_arr = []
    del args[0:2]
    args = ' '.join(args)
    temp_list = args.strip().split(',')
    s = len(list1)+1
    temp_list.insert(0,str(s))
    for i in list1:
        temp_arr.append(i[3])

    if temp_list[3] not in temp_arr:
        count += 1
        list1.append(temp_list)
        sava(list1)
    else:
        print("电话号码已存在")
    print(list1)
    print('影响了%s条记录' % count)






'''
删除员工

'''
def delete(args):
    count = 0
    s = args[len(args)-1]
    strs = ','.join(s)
    if strs[4] == '=':
        temp_list = s.strip().split('=')
        for key,value in enumerate(list1):
            if key+1 == int(temp_list[1]):
                count += 1
                del list1[key]
    elif strs[4] == '>':
        temp_list = s.strip().split('>')
        for key,value in enumerate(list1):
            if key+1 == int(temp_list[1]):
                count = len(list1) - (key+1)
                del list1[key+1:]
    elif strs[4] == '<':
        temp_list = s.strip().split('<')
        for key,value in enumerate(list1):
            if key+1 == int(temp_list[1]):
                count = key+1
                del list1[0:key+1]
    else:
        print("输入语法错误")


    # for key,i in enumerate(list1):
    #     if int(i[0]) == int(s1[1]):
    #         del list1[key]
    # count += 1
    sava(list1)
    print('影响了%s条记录' % count)
    print(list1)




'''
更新员工信息
'''
def update(args):

    count = 0
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
    sava(list1)
    print('影响了%s条记录' % count)


all_select()
while True:
    keyword = input("用户请输入查询语句:")

    if len(keyword) > 0:
        s = judge(keyword)
        if s[0] == 'find':
            select(keyword )
        elif s[0] == 'del':
            delete(s)
        elif s[0] == 'add':

            value = add_stuff(keyword)
            add(value)

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