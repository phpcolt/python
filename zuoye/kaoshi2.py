#coding=utf-8
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

active  = True
# while active == True:
#     for k in menu.keys():
#         print(k)
#     gov = input("请输入地名：")
#     if gov.strip() == 'q': exit()
#     if gov.strip() not in menu.keys():
#         print("您选择的地址不在我们这个范围里面")
#         #print(gov)
#     else:
#         while True:
#             for k in menu[gov].keys():
#                 print(k)
#             city = input("请输入城市")
#             if city.strip() == 'back': break
#             if city.strip() == 'q': exit()
#             if city.strip() not in menu[gov].keys():
#                     print("不存在当前城市")
#             else:
#                # print(menu[gov][city])
#                 while True:
#                     for k in menu[gov][city].keys():
#                         print(k)
#                     area = input("请输入区域")
#                     if area.strip() == 'back': break
#                     if area.strip() == 'q': exit()
#                     if area.strip() not in menu[gov][city].keys():
#                         print("不存在当前区域")
#                     else:
#                         while True:
#                             for k in menu[gov][city][area].keys():
#                                 print(k)
#                             company = input("请输入公司名字")
#                             if company == 'back': break
#                             if company == 'q': exit()
#                             if company.strip() not in menu[gov][city][area].keys():
#                                 print("不存在当前的公司")
#                             #elif company == 'back':
#                                 #pass
#                                 #continue
#                                 #break
#                             else:
#                                 #print(menu[gov][city][area][company])
#                                 for k in menu[gov][city][area][company]:
#                                     print(k)


#current_are = menu
# current_are2 = []
# while True:
#         for k in current_are.keys():
#             print(k)
#         str = input("请输入当前展示的区域：")
#         if str.strip() == 'q':exit()
#         if str.strip() == 'back':
#             if len(current_are2) != 0:
#                 current_are2.pop()
#
#             else:
#                 print("已经在顶级目录了")
#             break
#         if str.strip() not in current_are.keys():
#             print("没有当前的区域")
#         else:
#             #s = current_are[str].keys()
#             current_are2.append(current_are)
#             current_are = current_are[str]
#             #print(current_are[str])
#             print(current_are)


current = menu
lists = []
while True:
    for k in current.keys():
        print(k)
    str = input("选择项:")
    if str == 'q':exit()   #首先判断是否选择退出键
    if str.strip() in current.keys():
        lists.append(current)
        current = current[str]
        print(current)
    elif str.strip() == 'back':
         if len(lists) != 0:
             current = lists.pop()
         else:
             print("您已经是顶级域名了")
    else:
        print("你选择的地址不存在")


'''

思路:
首先定义个可以进入到里面的死循环

定义一个动态可以用来判断当前层级的current

获取顶级的地址

判断用户输入的字符

如果是q就直接跳出整个循环，退出

如果是正确的字符就进行循环打印并且更新下一层级的内容current里面保存的值

当用户输入不存在的就直接提示，并且不会更新current里面的key值

返回上一级删除列表里面的值，并且通过列表里面的值，查出所有当前层级的key值并且打印出来


'''