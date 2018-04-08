#coding=utf-8
s = open('1.txt','r')
strs = s.read()
s.close()
print(strs)

lists = eval(strs)
print(type(lists))
print(lists[0])