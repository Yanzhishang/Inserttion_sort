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
        list.append(random.randint(start, stop))  #把生成的随机数插入到list
    return list

print("随机生成的数组为：")
print(random_list(start,stop,length))
print("*"*30)
#插入排序
for i in range(1, len(list)): #从第二个开始
    key = list[i]
    j = i - 1
    while j >= 0:
        if list[j] > key:
            list[j + 1] = list[j]
            list[j] = key
        j -= 1

print("排序后的数组为：")
print(list)


'''
时间复杂度：即时间性能，高效率的排序算法应该是具有尽可能少的关键字比较次数和记录的移动次数
空间复杂度：主要是执行算法所需要的辅助空间，越少越好。
算法复杂性。主要是指代码的复杂性。
插入排序的时间复杂度为 O（n^2）；空间复杂度：O（1）
'''
