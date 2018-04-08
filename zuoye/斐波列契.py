#coding=utf-8
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b=b,a+b       #b=b是中间转换村存储的值
        n += 1
    return 'done'



print(list(fib(10)))


def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        print(a,b)
        a,b=b,a+b
        n += 1
    return 'done'

fib2(5)


#return  返回并且中止function
#yield 返回数据，并冻结当前的执行过程
#next唤醒冻结的函数执行过程