import math


def birth():
    yearOfBirth = int(input('Which year were you born in?'))
    if yearOfBirth > 2022:
        print("You have not born now")
    else:
        age = 2022 - yearOfBirth
        print(f'In 2022, you were {age}.')


def jingyesi():
    print("床前明月光，疑是地上霜。\n\
            举头望明月，低头思故乡。")


def sos(x1=0, x2=0):
    '''
    输出平方和
    x1,x2应该是实数
    '''
    x1 = float(x1)
    x2 = float(x2)
    return x1 ** 2 + x2 ** 2


def ball(r=0):
    '''
    打印给定球的表面积和体积
    :param r: 球的半径
    :return:
    '''
    r = float(r)
    surface = 4 * math.pi * r ** 2
    volume = 4 / 3 * math.pi * r ** 3
    print(f"surface = {surface}, volume = {volume}")


def solvefunc(a=0, b=0, c=0):
    '''
    解一元二次方程，打印两根
    :param a: x^2的系数 不应为0
    :param b: x的系数
    :param c: 常数
    :return:
    '''
    a, b, c = float(a), float(b), float(c)
    while a == 0:
        a = float(input("你应该输入不为0的a"))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("this is a complex func")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")


def calcvalue(b, r, n):
    """
    存银行模拟器
    :param b: 本金
    :param r: 利率
    :param n: 年数
    :return:
    """
    b, r, n = float(b), float(r), float(n)
    v = b * (1 + r) ** n
    print(v)


def rever(a):
    '''
    字符串逆序输出（四位数限定）
    :param a: 一个四位数
    :return:
    '''
    a = list(a)
    b = ['千位', '百位', '十位', '个位']
    d = list(zip(b, a))
    while len(a) != 4:
        a = input("you should input four-digit number")
    print(d[::-1])


def main():
    print("hello world")
    print("name ID")
    # name = input("input your name:")
    # print(f"Hi, {name}!")
    # birth()
    # jingyesi()
    # print(str(1234*5678))
    # print(sos(input("x1 = "), input("x2 = ")))
    # ball(input("radius of ball"))
    # solvefunc(input("a = "), input("b = "), input("c = "))
    # calcvalue(input("b = "), input("r = "), input("n = "))
    # rever(input("input a four-digit number:"))


if __name__ == '__main__':
    main()
