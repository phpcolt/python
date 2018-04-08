#coding=utf-8
'''

列举布尔值是False的所有值

None
False
数值中的零，包括0，0.0，0j（虚数）
空序列，包括空字符串(”)，空元组(())，空列表([])
空的字典{}
自定义的对象的实例，该对象的__bool__方法返回False或者__len__方法返回0
'''

'''
l1 = [11,22,33]
l2 = [22,33,44]

1、获取内容相同的元素列表
2、获取l1中有，l2中没有的元素列表
3、获取l2中有，l3中没有的元素列表
4、获取l1和l2中内容不同的元素


'''
l1 = [11,22,33]
l2 = [22,33,44]
list1 = set(l1)
list2 = set(l2)
c1 = list(list1 & list2)
print(c1)

c2 =list( list2 - list1 )
print(c2)

c3 =list( list1 - list2 )
print(c3)

c4 = list(list1 ^ list2)
print(c4)


'''
利用for循环和range输出
1、for循环从大到小输出1-100
2、for循环从小到输出100-1
3、while循环从大到小输出1-100
4、while循环从小到到输出100-1


'''

# for i in range(1,101):
#     print(i)

# for j in range(101,0,-1):
#     print(j)
i = 1
# while i < 101:
#     print(i)
#     i += 1

j = 101
while j > 0:
    print(j)
    j  -= 1

'''
利用for循环和range输出9*9乘法表

'''
for i in range(1,10):
    for j in range(1,10):
        print("%s*%s=%s"%(i,j,i*j))
