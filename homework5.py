# -*- coding: utf-8 -*-
'''
Created on 2022/3/29 8:05

'''
import math
import re
import random

def collatz(x):
    '''
    Collatz猜想序列
    :param x: 输入起始数字，应该是整数
    :return:
    '''
    x = int(x)
    result = []
    print(x, end=" ")
    result.append(x)
    while x!=1:
        while x%2:
            x = 3*x+1
            print(x,end=" ")
            result.append(x)
        else:
            x=int(x/2)
            print(x,end=" ")
            result.append(x)
    return result

def meandev(*args):
    '''
    求均值和方差
    :param args: 你要求的一组数
    :return:
    '''
    sum = 0
    for i in args:
        sum = sum+int(i)
    mean = sum/len(args)
    print(f"mean={mean}")
    s=0
    for i in args:
        s = s+(int(i)-mean)**2
    dev = math.sqrt(s/len(args))
    print(f"dev={dev}")

def rlst():
    '''
    生成25个1-10的整随机数，并计算每个出现的次数
    :return:
    '''
    lst = []
    for i in range(25):
        lst.append(random.randint(1, 10))
    s = set(lst)
    ti = {}
    for i in s:
        ti[i]=0
        for ele in lst:
            if i == ele:
                ti[i] += 1
    print(lst)
    for i in ti:
        print(f"time of {i} is {ti[i]}")

def youngtri(n):
    '''
    生成杨辉三角，使用加法
    :param n: 你要生成几行
    :return:
    '''
    lst = {0:{0:1}}
    for i in range(1, n):
        lst[i]= {}
        for j in range(0, i+1):
            if j ==0:
                lst[i][j] = lst[i-1][j]
            elif len(lst[i-1])-1>=j:
                lst[i][j]=lst[i-1][j-1]+lst[i-1][j]
            else:
                lst[i][j] = lst[i - 1][j-1]
    t = len(str(lst[n-1][int(n/2)]))+1
    for i in lst:
        for j in lst[i]:
            print(f"{lst[i][j]:<{t}}",end='')
        print("")

def findprime(n,m):
    '''
    质数筛，只除质数
    :param n: 从哪里开始
    :param m: 到哪里结束
    :return:
    '''
    primefac = {2}
    t = int(math.sqrt(m))
    for i in range(3,t+1):
        for j in primefac:   #对质数表遍历，看i是否为质数
            status = True
            if i%j!=0:       #如果i不能整除所有的j，说明i也是个质数
                status = True
            elif i//j==1:      #如果i就是j，说明i就是质数
                status = True
                break
            elif i%j==0:
                status = False
                break
        if status :
            primefac.add(i)
    result = set()
    for i in range(n,m+1):
        for fac in primefac:
            status = True
            if i%fac!=0:
                status = True
            elif i//fac==1:
                status = True
                break
            elif i%fac==0:
                status = False
                break
        if status :
            result.add(i)
    return result

def getprime(n,m):
    '''
    质数筛，集合加减
    :param n: 起始数字
    :param m: 终止数字
    :return:
    '''
    s1 = set(range(n,m+1))
    t = int(math.sqrt(m))+1
    for i in range(2,t):
        s2 = set(range(2*i,m+1,i))
        s1 = s1-s2
    lst = list(s1)
    lst.sort()
    print(lst)

def getmaxmin(*args):
    '''
    输出最大最小值
    :param args: 你要求的一组数
    :return:
    '''
    lst = list(args)
    min = int(lst[0])
    max = int(lst[0])
    for i in range(len(lst)):
        if min>int(lst[i]):
            min = int(lst[i])
        if max<int(lst[i]):
            max = int(lst[i])
    print(f"min = {min},max = {max}")

def main():
    # collatz(input("the initial number"))
    # tup = input("input a set of number, use','or space to split your number")
    # t = re.findall(r"[0-9]*", tup)
    # meandev(*list(filter(None,t)))
    # rlst()
    # youngtri(20)
    print(sorted(list(findprime(2,32))))
    # getprime(2,1000)
    # usernum = input("input a set of number, use','or space to split your number")
    # temp = re.findall(r"[0-9]*", usernum)
    # getmaxmin(*list(filter(None,temp)))

if __name__ == '__main__':
    main()