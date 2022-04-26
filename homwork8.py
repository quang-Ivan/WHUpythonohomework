# -*- coding: utf-8 -*-
'''
Created on 2022/4/26 8:10

'''
import collections.abc


def isEven(x):
    if x%2==0:
        return True
    else:
        return False

for i in [12, 3, 45, 6]:
    if isEven(i):
        print(i, end=' ')

def fact(n):
    if n!=int(n):
        print("integer plz")
    else:
        fac = 1
        for i in range(1,n+1):
            fac = fac*i
        print(fac)
        return fac
fact(10)

def getInfoOfSeq(sequence):
    if not isinstance(sequence,collections.abc.Sequence):
        return None
    else:
        t = list(sequence)
        t.sort()
        length = len(t)
        print(f"max is {t[length-1]}, min is {t[0]}, length={length}")
        
getInfoOfSeq({"TheQuickBrownFox"})


def GetFactor(n):
    n = int(n)
    factor = set()
    for i in range(2,n):
        if n%i==0:
            factor.update([i,n//i])
    factor.add(1)
    return factor

def IsPerfectNumber(n):
    for i in range(2,n+1):
        facs = GetFactor(i)
        t = sum(facs)
        if t == i:
            print(f"{i} is Perfect")
IsPerfectNumber(1000)

def toNumbers(alist):
    for i in range(len(alist)):
        alist[i]=int(alist[i])
a = ["123", "456", "789"]
toNumbers(a)
print(a)