#coding=utf-8
a = [1,2,3,4,5,6,7,8,9,9,4,4,0]
print(a[2])
print(a.index(5))
print(a[-5::2])
print(a[1:4])
a.append(5)
print(a)
a.insert(3,88)
print(a)
a[2] = 9
print(a)
a.sort()
print(a)

#pop删除最后一个
#REMOVE
a.pop()
print(a)
a.remove(9)
print(a)
del a[1]
print(a)
a.clear()
print(a)

b= ['a','x','Z']
b.sort()
print(b)
b.reverse()
print(b)