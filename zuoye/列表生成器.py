#coding=utf-8
# a = [1,3,5,7,9]
#
# li = [i+1 for i in a]
# print(li)

'''
生成器
'''
# b = (i for i in range(1000))
# while True:
#     print(next(b))


'''
斐波拉伽数
'''

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(a,b)
        a,b=b,a+b
        n += 1
    return 'done'


fib(6)

