#coding=utf-8
import os
count = 0

if os.path.exists("2.txt") and os.path.exists("3.txt"):
    #print("存在")
    f = open("2.txt",'r',encoding="utf-8")
    s = open("3.txt",'w',encoding="utf-8")
    #f.seek(0)
    for line in f.readlines():

        count += line.count('fuck')
        #print(s)
        new_line = line.replace('fuck','cao')


        #f.truncate()
        s.write(new_line)
    f.close()

else:
    print("不存在")


os.remove("2.txt")

print(count)