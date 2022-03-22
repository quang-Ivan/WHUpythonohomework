# -*- coding: utf-8 -*-
'''
Created on 2022/3/22 8:05

'''

# s = 1
# i = 1
# while i<=10:
#     s *= i
#     i += 1
# print("1*2*...*10 =",s)
# s = 1
# for i in range(1,11):
#     s *= i
# print('1*2*...*10 =', s)
# s = 0
# for i in range(1,10):
#     if i%2 == 0:
#         s += i
#         print(i, end=' ')
# else:
#     print("\nsum of the above evens is", s)
# for i in range(10):
#     print(i+1, end=' ')
# for i in range(3,28,3):
#     print(i)
# for i in range(25,2,-2):
#     print(i)

# s=1
# i=1
# while i<=10:
#     s *= i
#     i += 1
# else:
#     print("1*2*...*10 =",s)
# for i in range(10):
#     s *=i+1
# print("1*2*...*10 =",s)
# s=0
# for i in range(9):
#     if (i + 1 )%2==0:
#         s += i+1
# else:
#     print("sum of the evens under 10 is", s)
# dict = {'name': 'Tom', 'Age': 18, 'address': 'Disney'}
# for key in dict:
#     print(key,dict[key])
# num = input("a int")
# for i in num:
#     print(i)
# numb = int(num)
# for i in range(len(num)):
#     leng = len(str(numb))
#     print(numb//10**(leng-1))
#     numb = numb-numb//10**(leng-1)*(10**(leng-1))

# s = 0
# t = 1
# for i in range(int(num)):
#     s += t
#     if abs(i+1)%2!=0:
#         t=-t-2
#     else:
#         t = -t+2
# print(s)
def getdevide(num, divider=2):
    t = 0
    while int(num)//divider !=0:
        t +=1
        num = int(num)//2
    return t
# print(getdevide(num))
# def fib(num,a,b):
#     if int(num)==1:
#         return a
#     else:
#         return fib(int(num)-1, b, a+b)   #即在此处把1，2位向后移变成2，3位。即前面的数字减1，后面的位数向后移1
# print(fib(num,1,1))
# rmb = int(input("a int between 10 and 1000"))
# while not 10<=rmb<=1000:
#     rmb = int(input("重新输"))
def comb(rmb):
    a = rmb//5
    sum = 0
    for i in range(a):
        nrmb = rmb-5*(i+1)
        b = nrmb//2
        for j in range(b):
            nnrmb = nrmb - 2*(j+1)
            if nnrmb==0:
                continue
            print(f"5元用了,{i+1},2元用了,{j+1},1元用了,{nnrmb}")
            sum = sum+1
    print(f"共计{sum}种组合")
# comb(rmb)
def monkey(day):
    if day ==1:
        return 382
    else:
        return monkey(day-1)/2-1
print(monkey(8))