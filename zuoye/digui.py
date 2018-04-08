#coding=utf-8
# import sys
# s = sys.getrecursionlimit()  #获取系统的次数
# print(s)
# def func(m):
#     m = int(m/2)
#     print(m)
#     if int(m) > 0:
#         func(m)
#     print(m)
# func(10)


# def func(n,count):
#     print(n,count)
#     if count < 5:
#         return func(n/2,count+1)
#     else:
#         return n
#
# res = func(188,1)
# print('res',res)
data = list(range(10000))

def func(args):
    for key,i in enumerate(data):
        if i == 674:
            return key

print(func(data))


print(data[674])
