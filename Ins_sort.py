#coding= utf-8
import random
#定义三个常量用来表示下限、上限和数组长度
start = 1
stop = 1000
length = 100
#定义一个新数组存放随机数
list = []
def random_list(start, stop, length):
    for i in range(length):
        list.append(random.randint(start, stop))  #把生成的随机数出入到list
    return list

print("随机生成的数组为：")
print(random_list(start,stop,length))
print("********")
for i in range(1, len(list)):
    key = list[i]
    j = i - 1
    while j >= 0:
        if list[j] > key:
            list[j + 1] = list[j]
            list[j] = key
        j -= 1

print("排序后的数组为：")
print(list)
