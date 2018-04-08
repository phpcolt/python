#coding=utf-8
import os
'''
请说明python2和python3中的默认编码是什么？
'''
#python3采用的utf-8编码
#python2采用的是unicode码

'''
为什么会出现中文乱码？你能列举楚集中情况

'''

#编码出现乱码跟文件编码有关，还有打开方式也有关
#开发过程中没有解码，也可以导致文件乱码
#系统中没有文件对应编码文件，也会出现编码乱码


#-*-coding:utf-8-*的作用是什么
'''
如果代码中有中文注释，就需要此声明
比较高级的编辑器，会根据头部声明，将此作为代码文件的格式。
程序会通过头部声明，解码初始化 u”人生苦短”，这样的unicode对象，（所以头部声明和代码的存储格式要一致）
'''

#pyton2和python3的bytes的区别如果代码中有中文注释，就需要此声明
#    比较高级的编辑器（比如我的emacs），会根据头部声明，将此作为代码文件的格式。
#    程序会通过头部声明，解码初始化 u”人生苦短”，这样的unicode对象，（所以头部声明和代码的存储格式要一致）
#python2的bytes是字符节

#python3的bytes是二进制


'''
r和rb的区别

'''
#r单纯的读取
#rb是以二进制方式读取文件

'''
解释一下三个参数的作用是什么
open(f_name,'r',encoding="utf-8")
'''
#f_name是读取文件的路径可以是相对路径和绝对路径
#'r'读取的模式
#encoding="utf-8" 指定文件读取的编码格式


#写函数，计算传入数字参数的和
# def sum(x,y):
#     return x+y
#
# print(sum(1,2))


# def update(filename=None,args=None):
#     strs = open('4.txt','w',encoding="utf-8")
#     with open('3.txt','r+',encoding="utf-8") as f:
#         for i in f.readlines():
#             s = i.replace('cao',args)
#             strs.write(s)
#
#     f.close()
#
#     os.remove('3.txt')
#     old_path =os.getcwd()+'/4.txt'
#     new_path =os.getcwd()+'/'+filename
#     os.renames(old_path,new_path)
#
# update('6.txt','guo')
#print(os.getcwd())
#os.renames('4.txt', '6.txt')
# olds =os.getcwd()+'/4.txt'
# news =os.getcwd()+'/5.txt'
# os.renames(olds,news)

'''
检测对象是不是有空内容
'''

# def func(args):
#     if type(args) == str:
#         print("字符串")
#         s1 = len(args)
#         for i in args:
#             strs = ''.join(i)
#         s2 = len(strs)
#         if s1 > s2:
#             print("里面有空格")
#         else:
#             print("里面没有空格")
#
#
#     elif type(args) == list:
#         print("列表")
#         s1 = len(args)
#         for i in args:
#              if i == ' ':
#                  args.remove(' ')
#         s2 = len(args)
#         if s1 > s2:
#             print("里面有空格")
#         else:
#             print("里面没有空格")
#     elif type(args) == tuple:
#         print("是元祖")
#         s1 = len(args)
#         list1 = list(args)
#         for key,i in enumerate(list1):
#             if i == ' ':
#                 #print(key)
#                 list1.pop(key)
#         s2 = len(tuple(list1))
#         if s1 > s2:
#             print("里面有空格")
#         else:
#             print("里面没有空格")
#
#
#     else:
#         print("目前只支持字符串，元祖，还有列表")
#
#
# func((1,2,3,' ',4))

'''
写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并且将新内容返回给调用者
dic ={"k1":"v1v1","k2":[11,22,33,44]}
ps字典中的value只能是字符串和列表
'''
# d = {"k1": "v1v1", "k2": [11,22,33,44]}
# def func2(args):
#     for key,value in args.items():
#         if len(value) > 2:
#             if type(value) == str:
#                 print(value[0:2])
#             elif type(value) == list:
#                 print(value[0:2])
#             else:
#                 print("字典中不能有其他类型的值")
#
#
# func2(d)


'''
解释闭包的概念
'''
#是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以，闭包是由函数和与其相关的引用环境组合而成的实体。
