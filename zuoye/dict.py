#coding=utf-8
dic = {'k1':'v1','k2':'v2','k3':'v3'}
for i in dic:
#请循环遍历出所有的key
    #print(i)
#请循环遍历出所有的value
    #print(dic[i])
#请循环遍历出所有的key和value
    print(i,dic[i])
#请在字典中添加一个键值对，'k4'：'v4'，输出添加后的字典
dic['k4'] = 'v4'
print(dic)
#请输出字典中键值对'k1'，'v1'，并输出删除后的字典
dic.pop('k1')
print(dic)
#请获取字典中的'k6'对应的值，如果键k6不存在，则不报错，并且返回None
print(dic.get('k5'))

#请获取的对应的k2对应的值
print(dic['k2'])

#请删除字典中''k6d的值，如果键k6不存在，则不错报，返回None
print(dic.pop('k6',None))

#现有dic2 = {'k1':'v111','a':'b'}通过一行操作使其合并
dic3 = {'k1':'v1','k2':'v2','k3':'v3'}
dic2 = {'k1':'v111','a':'b'}
dic2.update(dic3)
print(dic2)

#第10题
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
s = lis[0][1][2]
print(s['k1'][0].upper())
s['k1'][0] = 'TT'
print(s['k1'][0])
#s['k1'][1] = '100'

print(s['k1'][1])

s['k1'][2] = 101

lis2 = s['k1']
print(lis2)
rep = ['100' if x == 3 else x for x in lis2 ]
print(rep)
s['k1'] = rep
print(s['k1'][1])


#最后一题
li = [1,2,3,'a','b',4,'c']
dic4 = {}
li2 = []
for i in li:
    s = li.index(i)
    #print(s)
    if s % 2 == 1:
        li2.append(li[s])
        # if dic4.setdefault('k1',None) == None:
        #     dic4.setdefault('k1',li2)
        # else:
        #     if isinstance(dic4['k1'],list):
        #         dic4['k1'] = li2
        if 'k1' in dic4.keys() == False:
            dic4.setdefault('k1', li2)
        else:
            dic4['k1'] = li2
            print("哈哈哈")

print(dic4)
