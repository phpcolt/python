#coding=utf-8
'''

dic = {'k1':'v1',"k2":"v2","k3":[11,22,33]}

1、请循环输出所有的key
2、请循环输出所有的value
3、请循环输出所有的key和value
4、请在字典中添加一个键值对，"k4"："v4",输出添加后的字典
5、请在修改字典中"k1"对应的值为"alex",输出修改后的字典
6、请在k3对应的值中追加一个元素44，输出修改后的字典
7、请在k3对应的值得第1个位置插入元素18，输出修改后的字典

'''

# dic = {'k1':'v1',"k2":"v2","k3":[11,22,33]}
#
# for key,value in dic.items():
#     #print(key)
#     #print(value)
#     print(key,value)
#
# dic['k4'] = 'v4'
# print(dic)
#
# dic['k1'] = 'alex'
# print(dic)
#
# s = dic['k3']
# s.append(44)
# print(dic)
# s.insert(1,18)
# print(dic)


'''
1、将字符串s = 'alex'转换成列表
2、将字符串s = 'alex'转换成元祖
3、将列表li = 【'alex'，"seven"】转换成元祖
4、将元祖tu = （'alex'，''seven）转换成列表
5、将列表li = 【"alex","seven"】转换成字典且字典的key按照10开始向后叠加

'''
# s = 'alex'
# s1 = list(s)
# print(s1)
#
# s2 = tuple(s)
# print(s2)
#
# li = ['alex','seven']
# li2 = tuple(li)
# print(li2)
#
# tu = ('alex','seven')
# tu2 = list(tu)
# print(tu2)
#
# j = 10
# dic2 = {}
# for i in li:
#     dic2[j] = i
#     j += 1
# print(dic2)


'''
有如下值集合【11，22，33，44，55，66，77，88，99，90】，将所有大于66的值保存至字典的
第一个key中将小于66的值保存至第二个key的值中

即{'k1'：大于所有66的所有值，'k2'：小于66的所有值}
'''

# li3 = [11,22,33,44,55,66,77,88,99,90]
# dic5 = {'k1':[],'k2':[]}
# for j4 in li3:
#     if j4 < 66:
#         dic5['k2'].append(j4)
#     else:
#         dic5['k1'].append(j4)
# print(dic5)


'''
输出商品列表，用户输入序号，显示用户选中的商品
商品li = 【'手机'，"电脑"，"鼠标垫"，'游艇'】

1、允许用户添加商品
2、用户输入序号显示内容


'''

# light = True
# lis = ['手机','电脑','鼠标垫','游艇']
#
#
# while light:
#
#     for keys,values in enumerate(lis):
#         print("%s. %s"%(keys,values))
#
#     s5 = input("请输入商品名称和序号:")
#     length = len(lis)
#     if s5.isdigit() == True and int(s5) < length and int(s5) >= 0:
#         print(lis[int(s5)])
#
#     elif isinstance(s5,str) == True and len(s5) > 0 and s5.isdigit() == False:
#         lis.append(s5)
#         print(lis)
#
#     else:
#         print("恭喜你直接退出了，没有按照要求输入")
#         light = False
#         break


'''
用户交互显示类似省市县N级联动的选择

1、允许用户增加内容
2、允许用户选择查看某一个内容


'''
map_dic = {'湖北':{'武汉':{
                        '武昌':'光谷广场',
                        '汉口':'江汉路',
                        '汉阳':'晴川阁'
                         }
                  },
            '北京' :{'北京':{
                            '朝阳区':'爱奇艺',
                            '海淀区': '360',
                            '昌平区': '老男孩'
                            }
            }
          }
trun = True
while trun == True:
    lists = list(map_dic)
    for i in lists:
        print(i)
    strs = input("请选择省会:")
    if strs not in map_dic.keys() :
        print("您选择的省会不存在")

    else:
        #print(map_dic.get(strs))
        print(map_dic[strs])
        city = input("请输入您选择的城市：")
        if map_dic[strs].setdefault(city,None) == None :
            print("您选择的不是当前省会的城市或城市不存在")
        else:
            #print(map_dic[strs][city])
            for key in map_dic[strs][city]:
                print(key)
            area = input("请选择当前区域位置")
            if map_dic[strs][city].setdefault(area,None) == None:
                print("请当前输入的区域不存在")
            else:
                print(map_dic[strs][city][area])