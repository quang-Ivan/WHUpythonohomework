# -*- coding: utf-8 -*-
'''
Created on 2022/3/8 8:51

'''
import math
# print(2<5<8)
# print(2<5>8)
# print(2<5 and 5<8)
# print(2<5 and 5>8)
# print(3+8)
# print(3*8)
# print(3/8)
# print(3//8)
# print(13//8)
# print(3//-8)
# print(13//-8)
# print(13%8)
# print(3 or 5)
# print(3 or "hello")
# print(0 or 2)
# print(100 or 0)
# print(0 or 0, "\n")
# print(3 and 5)
# print(3 and 0)
# print(0 and 5)
# print(3 and "hello")
# print(0 and 0)
# value_1 = 2
# value_2 = 2.0
# if value_1 == value_2:
#     print('相等')
# else:
#     print('不相等')

# f = 3.5
# if (f):
#     print(True)
# else:
#     print(False)
# x=1
# print(x>0 or x==2)
# print(x)
# a = int(input('输入第 1 个整数：'))
# b = int(input('输入第 2 个整数：'))
# if a>b:
#     t=a
#     a=b
#     b=t
# print('按从小到大的顺序输出：', a, b)


def outinorder(*args):
    '''
    简单的冒泡排序算法，由小到大
    :param args: 应该输入3个数字，以逗号隔开
    :return:
    '''
    # lst = list(args)
    # lst.sort()
    lst = list(args)
    for i in range(len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst
# print(outinorder(951,521,2,8,4))

# num = int(input('输入一个大于  6 的整数: '))
# if num>6 and num%2==0:
#     print("{0}是偶数。".format(num))
# else:
#     print("{0}不大于 6或者不是一个偶数。".format(num))

def telegram(typ, words):
    '''
    计算电报费用
    :param typ: 电报类型: 普通电报，或， 加急电报
    :param words: 电报字数，应为整数
    :return:
    '''
    words = int(words)
    if words == 0:
        print("exceuse me?")
    else:
        if typ ==  "普通电报":
            fee = ((words-1)//10 +1)*7.5
            print(fee)
        elif typ == "加急电报":
            fee = 7.5+((words-1)//10)*7.5*2
            print(fee)
        else:
            print("请正确输入电报类型，普通电报，或者，加急电报")

# telegram(typ = input("电报类型："), words = input("字数"))

def solvtri(*args):
    '''
    解三角形
    :param args: 输入三个参数作为三角形三边
    :return:
    '''
    a, b, c= args
    a, b, c = float(a), float(b), float(c)
    lst = outinorder(*args)
    if lst[0]+lst[1] > lst[2] and lst[0]>0:
        p = (lst[0]+ lst[1]+lst[2])*0.5
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        length = p*2
        print("面积=",s,"周长=",length)
    else:
        print("不构成三角形")
solvtri(10,7,4)

def fun1single(x):
    x = float(x)
    if x>=0:
        y = (x**2-3*x)/(x+1)+2*math.pi+math.sin(x)
    elif x<0:
        y = math.log(-5*x)+6*math.sqrt(abs(x)+math.e**4) - (x+1)**3
    y = format(y, '.4f')
    return y
print(fun1single(8))