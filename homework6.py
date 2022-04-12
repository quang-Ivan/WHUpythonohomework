# -*- coding: utf-8 -*-
'''
Created on 2022/4/12 8:07

'''
from math import sqrt
from random import random

def baiqiang():
    '''
    具有一定程度上的字典排序功能
    :return:
    '''
    dict =  {"聚美优品":58,'京东':12945 ,'亚马逊中国':391 ,'当当网':357 ,'唯品\
会':728,'考拉严选':116 ,'天猫':21086}
    x = list(zip(list(i for i in dict), list(dict[i] for i in dict)))
    x.sort(key=lambda x:x[1],reverse=True)
    print("企业销售额（亿元）")
    for i,j in x:
        print(f"{i:\u3000<10}:{j:>10}")

def radord():
    lst = [random() for i in range(20)]
    lst1 = sorted(lst[0:10])
    lst2 = sorted(lst[10:20],reverse=True)
    print(lst,'\n',lst1+lst2)

def main():
    # baiqiang()
    # print(list(i for i in range(1,21) if i%2==0))
    # print(list(i**2 for i in range(1,11)))
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # print(list(list(matrix[j][i] for j in range(len(matrix))) for i in range(3)))
    radord()
if __name__ == '__main__':
    main()