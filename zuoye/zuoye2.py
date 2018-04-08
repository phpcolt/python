#coding=utf-8
'''

利用下划线列表每一个元素拼接上字符串 li = ['alex','eric','rain']

'''

li = ['alex','eric','rain']
str = '_'.join(li)
print(str)


'''
查找元素中的列表，移除每个元素的空格，并且查找以a或A开头，并且以c结尾的字符串
̶li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
'''
li2 = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alec", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
for i in range(len(li2)):
    li2[i] = li2[i].replace(' ','')
print(li2)

tu2 = list(tu)
for j in range(len(tu2)):
    tu2[j] = tu2[j].replace(' ','')
print(tuple(tu2))

for key,value in dic.items():
    #print(key,value)
    dic[key] = dic[key].replace(' ','')
print(dic)

list1 = []
for k in li2:
    if k.startswith('a') or k.startswith('A') and k.endswith('c'):
        list1.append(k)
print(list1)

list2 = []
for j1 in tu2:
    if (j1.startswith('a') and j1.endswith('c')) or (j1.startswith('A')  and j1.endswith('c')) :
        list2.append(j1)
print(list2)

list3 = []
list4 = []
for key,value  in dic.items():
    list3.append(value)
for j2 in list3:
    if (j2.startswith('a') and j2.endswith('c')) or (j2.startswith('A')  and j2.endswith('c')) :
        list4.append(j2)
print(list4)


'''

li = ['alex','eric','rain']

1.计算列表的长度并输出

2。列表中追加元素'seven'，并输入添加后的列表

3.请在列表的第1位置插入元素'Tony',并输出添加后的列表

4.请在修改列表的第2个位置的元素为'Kelly'，并输出修改后的列表

5请删除列表中的元素'eric',并输出修改后的列表

6.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表

7请删除列表中的第3个元素，并输出删除元素后的列表

8.请删除列表中的第2至4个元素，并输出删除元素后的列表

9.请将列表所有元素反转，并输出反转后的列表

10.请使用for、len、range输出列表的索引

11、请使用enumrate输出列表元素和序号（序号从100开始）

12、请使用for 循环输出列表的所有元素

'''

li3 =['alex','eric','rain']
print(len(li3))
li3.append('seven')
print(li3)

li3.insert(1,'Tony')
print(li3)

li3[2] = 'Kelly'
print(li3)

li3.remove('Kelly')
print(li3)

print(li3.pop(2))
print(li3)

li3.remove(li3[2])
print(li3)

li3 = list(reversed(li3))
print(li3)

for j3 in range(len(li3)):
    print(j3)

for j4,item in enumerate(li3):
    print(j4+100,item)

for j5 in li3:
    print(j5)


'''
  li = ["hello",'seven',["mon",["h","kelly"],'all'],123,466]
  1、请根据索引输出"kelly"
  2、请使用索引找到'all'元素并将其修改为"ALL",如:li[0][1][9]...
  3、写代码，有如下元祖，按照要求实现每一个功能

'''


li4 = ["hello",'seven',["mon",["h","kelly"],'all'],123,466]
print(li4[2][1][1])

print(li4[2][2].upper())


'''
tu4 = （'alex','eric','rain'）
1、计算元祖长度并输出
2、获取元祖的第2个元素，并输出
3、获取元祖的第1-2个元素，并输出
4、请使用for输出元祖的元素
5、请使用for、len、range输出元祖的索引
6、请使用enumrate输出元祖元素和序号（序号从10开始）

'''
tu4 =('alex','eric','rain')
print(len(tu4))
print(tu4[1])
print(tu4[1:])

for k6 in tu4:
    print(k6)

for k7 in range(len(tu4)):
    print(k7)
for keys,values in enumerate(tu4):
    print(keys+10,values)


'''

tu5 = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
1、讲述元祖的特性
2、请问tu5变量中的第一个元素"alex"是否可被修改
3、请问tu5变量中的"K2"对应的值是什么类型？是否可以被修改？如果可以，请添加一个元素"Seven"
4、请问tu5变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请添加一个元素"Seven"
'''

tu5 = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
#元祖里面的元素不可修改
#元组使用小括号

#alex不能被修改，因为alex是元祖里面的元素，元祖的元素不可改

#k2对应的值是列表
s2 = tu5[1][2]['k2']
s2.append('Seven')
print(s2)

#k3的值类型是元祖，值是不可以被修改的


