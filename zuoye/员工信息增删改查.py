#coding=utf-8
list1 = []
'''
查询整个
'''

def select():
    with open('kaoshi.txt','r',encoding="utf-8") as f:
        for key,i in enumerate(f.readlines()):
            if key > 0:
                data_list = i.strip().split(',')
                list1.append(data_list)



'''
通过年龄来查信息
'''
def data_age(number):
    count = 0
    if number.isdigit():
        for j in list1:
            if j[2] > number:
                count += 1
                print(j)
        print('影响了%s条记录' % count)
    else:
        print("请输入数字，谢谢")


'''
通过部门来查

'''

def department(args):
    count = 0
    for k in list1:
        if k[4] == args:
            count += 1
            print(k)
            print('影响了%s条记录' % count)


'''
通过时间模糊查询

'''
def data_time(args):
    count = 0
    for i in list1:
        #print(type(i[len(i)-1]))
        img_list2 = i[len(i)-1].split('-')
        #print(img_list2)
        if args in img_list2:
            count += 1

            print(i)
    print('影响了%s条记录' % count)

'''
增加员工记录
'''
def add_staff(*args):
    count = 0
    for i in list1:
        if args[3] not in i:
            s = list(args)
            length = len(s)
            s.insert(0,length)
            list1.append(s)
            count += 1
            print('影响了%s条记录' % count)
            print(list1)

        else:
            print("已经存在")

    #args. = s
    # for i in list1:
    #     if i[3] == args[3]:
    #         print("存在相同的电话号码")

'''
通过id删除员工
'''
def del_staff(args):
    count = 0
    if args.isdigit():
        s = len(list1)
        if args > 0 and args < s:
            del list1[args]
            count += 1
        else:
            print("查无此用户")

    print('影响了%s条记录' % count)

'''

修改员工部门
'''
def update_staff(args,argus2):
    # for i in list1:
    #     #print(i[4])
    #     if i[4] == args:
    #         i[4] = argus2
    #         print(i)
    count = 0
    for i in list1:

        if args in i:
            #print(i)
            count += 1
            s = i.index(args)
            i[s] = argus2
    print('影响了%s条记录' % count)
    print(list1)


'''
修改员工年龄

'''
def update_age(args,args1):
    count = 0
    for i in list1:
        #print(i)
        if args in i[1]:
            count += 1
            i[2] = args1

        print(i)
    print('影响了%s条记录' % count)









select()


data_time('2016')


