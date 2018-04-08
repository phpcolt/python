#coding=utf-8
import os
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]

'''
功能要求：
基础要求：

1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表

2、允许用户根据商品编号购买商品

3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒

4、可随时退出，退出时，打印已购买商品和余额

5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示


扩展需求：

1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买

2、允许查询之前的消费记录


'''
# last_shopping = []
# salacy = 0#工资
# balance = 0#余额
# s = []  #列表
# sava = []
# while True:
#     username = input("用户名:")
#     password = input("密码：")
#     if username.strip() == 'root' and   password.strip() == '123456':
#         print("登录成功")
#         while True:
#             pay = input("请输入您的工资:")
#             if pay.isdigit():
#                 salacy = int(pay)
#                 for key,value in enumerate(goods):
#                     #print("%s.%s"%(key,value['name']))
#                     s.append([value['name'],value['price']])
#                 while True:
#                     for key, value in enumerate(goods):
#                         print("%s.%s" % (key, value['name']))
#                     shop = input("请输入选择的商品号：")
#                     if shop == 'q':
#                         if len(last_shopping) != 0:
#                             print(("已经购买的商品%s,余额是%s")%(last_shopping,salacy))
#
#                         else:
#                             print("你都还没购物，就离开了，太遗憾了，下次再再来")
#                         exit()
#
#                     if salacy > int(s[0][1]) and int(shop) < len(goods) and shop.isdigit():
#                         salacy -= int(s[0][1])
#
#                         if s[int(shop)] in last_shopping:
#
#                             # print(s[int(shop)])
#                             number = last_shopping.index(s[int(shop)])
#                             last_shopping[number][1] = last_shopping[number][1] * 2
#                             #last_shopping.append(s[int(shop)])
#                             print(last_shopping)
#                         else:
#                             last_shopping.append(s[int(shop)])
#                             print(last_shopping)
#                         sava.append(last_shopping)
#                         sava.append(salacy)
#                         sf = open('1.txt','w')
#                         sf.write(str(sava))
#                         sf.close()
#                     elif salacy > int(s[0][1]) and int(shop) > len(goods):
#                         print("当前选的太坑爹了，请重新选")
#                         continue
#                     else:
#                         print("您的余额不足，请下次购物,退出请按q")
#
#             else:
#                 print("请重新输入您的工资")
#
#     else:
#         print("请重新输入账户和密码")

# last_shopping = []#
# salacy = 0#工资
# balance = 0#余额
# s = []  #列表
# sava = []
# dj  = 0
# while True:
#     username = input("用户名:")
#     password = input("密码：")
#     if username.strip() == 'root' and   password.strip() == '123456':
#         print("登录成功")
#         for key, value in enumerate(goods):
#             # print("%s.%s"%(key,value['name']))
#             s.append([value['name'], value['price']])
#         #print(s)
#         while True:
#                 if os.path.getsize('1.txt') > 0:
#                     sr = open('1.txt','r')
#                     strs = sr.read()
#                     sr.close()
#                     #print("您上次购物时记录%s"%strs)
#                     #print(list(strs))
#                     new_list = eval(strs)
#                     salacy = new_list[len(new_list)-1]
#                     print(salacy)
#                     del new_list[len(new_list)-1]
#                     last_shopping = new_list
#                     print(last_shopping)
#                     # salacy = list1[len(list1)-1]
#                     # print(salacy)
#
#                 else:
#                     pay = input("请输入您的工资:")
#                     if pay.isdigit():
#                         salacy = int(pay)
#                     else:
#                         print("请重新输入您的工资")
#
#                 while True:
#                             for key, value in enumerate(goods):
#                                 print("%s.%s %s" % (key, value['name'],value['price']))
#                             shop = input("请输入选择的商品号：")
#
#                             if shop == 'q':
#                                 if len(last_shopping) != 0:
#                                     print(("已经购买的商品%s,余额是%s")%(last_shopping,salacy))
#                                     for i in last_shopping:
#                                         sava.append(i)
#                                     sava.append(salacy)
#                                     sf = open('1.txt', 'w')
#                                     sf.write(str(sava))
#                                     sf.close()
#
#                                 else:
#                                     print("你都还没购物，就离开了，太遗憾了，下次再再来")
#                                 exit()
#                             for key, value in enumerate(goods):
#                                 if key == int(shop):
#                                     dj = value['price']
#                             if salacy > dj and int(shop) < len(goods) and shop.isdigit():
#                                 salacy -= dj
#
#                                 if s[int(shop)] in last_shopping and len(last_shopping) > 0:
#                                     number = last_shopping.index(s[int(shop)])
#                                     last_shopping[number][1] += dj
#                                     #last_shopping.append(s[int(shop)])
#                                     print(last_shopping)
#
#                                 else:
#                                     last_shopping.append(s[int(shop)])
#                                     print(last_shopping)
#
#                             elif salacy > dj and int(shop) > len(goods):
#                                 print("当前选的太坑爹了，请重新选")
#                                 continue
#                             else:
#                                 print("您的余额不足，请下次购物,退出请按q")
#
#
#
#     else:
#         print("请重新输入账户和密码")

while True:

        username = input("请输入您的用户名：")
        password = input("请输入您的密码")

        if username == "root" and password == "123456":
            print("登录成功")
            for key,value in enumerate(goods):
                print(key,value)
        else:
            print("请重新登录")

