#coding=utf-8
'''
1.创建一个空列表，命名为names，往里面添加old_driver，rain，jack，shanshan，peiqi，black_girl
'''
# names = []
# names.append('old_driver')
# names.append('rain')
# names.append('jack')
# names.append('shanshan')
# names.append('peiqi')
# names.append('black_girl')
# print(names)

'''
往names列表里black_girl前面插入一个alex
'''
# names.insert(5,'alex')
# print(names)
# names[3] = "姗姗"
# print(names)
# names.insert(2,['oldboy','oldgirl'])
# print(names)
# a = names.index('peiqi')
# print(a)
# number = [1,2,3,4,2,5,6,2]
# for i in number:
#     names.append(i)
# print(names)
# b = names[4:7]
# print(b)
# print(names[2:10:2])
# print(names[-3:])
# for j in number:
#     s = number.index(j)
#     print(s,j)
#
# for z in number:
#     s = number.index(z)
#     if s % 2 == 0:
#         number[s] = -1
# print(number)
#
# for f in names:
#     if f == 2:
#         s1 = names.index(f)
#         print(s1)
#         names[s1] = "True"
# print(names)


#enumerate枚举


#
product =[['iphone8',6888],['MacPro','14800'],['小米6',2499],['Coffee',31],['Book',80],['Nikeshoes',799]]
# for h in product:
#     s = product.index(h)
#     print(s,h[0],h[1])

open = True
list = []
while open == True:
    for k,value in enumerate(product):
        print(('%s. %s %s')% (k,value[0],value[1]))

    s = input("请输入产品编号：")
    count = len(product)
    if s.isdigit() and int(s) < count and int(s) >= 0:
        list.append(product[int(s)])
    elif s == 'q':
        #print(list)
        open = False
        if len(list) >0 :
            for keys,values in enumerate(list):
                print("%s. %s %s"%(keys,values[0],values[1]))
        else:
            print("当前都没买什么东西")
        break

    else:
        print("你输的是什么东西")


