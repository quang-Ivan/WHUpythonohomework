# -*- coding: utf-8 -*-
'''
Created on 2022/4/19 8:24

'''

def staeng(x):
    lst = x.split(" ")
    print(len(lst))
    print(list(i.capitalize() for i in lst))
    args = list(len(i) for i in lst)
    sum = 0
    for i in args:
        sum = sum+int(i)
    mean = sum/len(args)
    print(f"mean={mean}")

def caesar(msg,key):
    msglst = msg.split(" ")
    for i in range(len(msglst)):
        ordlst = list(ord(j) for j in msglst[i])
        print(ordlst)
        for j in range(len(ordlst)):
            if ordlst[j] < 91:
                if (ordlst[j]+key-64)%26==0:
                    ordlst[j] = 64+26
                else:
                    ordlst[j] = 64+(ordlst[j]+key-64)%26
            else:
                if (ordlst[j]+key-96)%26==0:
                    ordlst[j] = 96+26
                else:
                    ordlst[j] = 96+(ordlst[j]+key-96)%26

        msglst[i] = "".join([chr(j) for j in ordlst])
    print(" ".join(msglst))


def main():
    x = "esfziukbagjlsfk aeguiknjadslikjgn EFUGKNJAFLgeaigrn dsnkjf ojnksdagofi nFES segadfgrewgfdv"
    staeng(x)
    caesar("Wuhan UniverSity Lsafgchwerghgfchef",4)
if __name__ == '__main__':
    main()