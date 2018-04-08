# #coding=utf-8
# strs = ['alex', 'steven', 'egon']
# strs1 = ''
#
# num = len(strs)
# for  key,value in str
#     if strs1：
#         strs1+='_'
#     strs1+=
#     if key < (len(strs)-1):
#         strs1 = strs1  + value + '_'
#     else:
#         strs1 = strs1 + value
# print(strs1)
#
# '_'.join(strs)
#
# strs[0]+""+strs[1]
#
# '1'+'2'
#
# ''
# s = ['alex','egon','yuan','wusir','666']
# number = s.index('666')
# s[number] = '999'
# print(s)
#
#
# s[-2]  = '9999'
# print(s)
# s1 = s[-3:]
# print(s1)

# s2 = "www.luffycity.com"
# s = s2.split(".")
# print(s)
#
# s2 = s2.replace("f",'cd')
# print(s2)
# s = 0
# for i in range(1,101):
#     s += i
#
# print(s)

# s = 0
# i = 1
# while i > 0 and i < 101
# :
#     s += i
#     i += 1
# print(s)



# i = 0
# light = True
# while light == True:
#     username = input("username:")
#     password = input("password:")
#     if username == 'root' and "password" == '123456':
#         print("登陆成功")
#     else:
#         print("登录失败")
#     i +=  1
#     if i == 3:
#         light = False

# f = open("1.txt",'ab')
# f.write("\n 8888hhh".encode('utf-8'))
# f.close()
#
#
# #在原有文件里面追加字符串存需要转码

#读写模式
#
# f = open('1.txt','r+')
# s = f.read()
# print(s)
#
# f.write("\n hahahhahha")
# f.close()

#写读模式

f = open('1.txt','w+')
s = f.read()
print(s)

f.write("\n fuck you")
f.close()








