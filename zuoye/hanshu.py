#coding=utf-8
'''
写函数，返回扑克牌列表
'''
list1 = []
signal = ["红桃","梅花","方块","黑桃"]
bigpai = ['j','q','k','A']
def puke():
     for i in signal:
         for j in range(2,9):
            list1.append(tuple([i,j]))
         for k in bigpai:
            list1.append(tuple([i+k]))



puke()
print(list1)

'''


'''