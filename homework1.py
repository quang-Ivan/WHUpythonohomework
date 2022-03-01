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
    '''
    x1 = float(x1)
    x2 = float(x2)
    return x1**2+x2**2

def ball(r=0):
    r = float(r)
    surface = 4*math.pi*r**2
    volume = 4/3*math.pi*r**3
    print(f"surface = {surface}, volume = {volume}")

def solvefunc(a=0, b=0, c=0):
    a, b, c = float(a), float(b), float(c)
    delta = b**2-4*a*c
    if delta < 0 :
        print("this is a complex func")
    else :
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")

def calcvalue(b, r, n):
    b, r, n = float(b), float(r), float(n)
    v = b*(1+r)**n
    print(v)

def rever(a):
    a = str(a)
    while len(a) != 4:
        a = input("you should input four-digit number")
    for i in range(len(a)-1, -1, -1):
        print(a[i])


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
    calcvalue(input("b = "), input("r = "), input("n = "))
    # rever(input("input a four-digit number:"))




if __name__ == '__main__':
    main()