# -*- coding: utf-8 -*-
'''
Created on 2022/3/15 8:20

'''

def twage(hours, wage):
    """
    输入工作时长算工资
    :param hours: 一周工作时长
    :param wage: 时薪
    :return: 一周总薪资
    """
    hours = float(hours)
    wage = float(wage)
    if hours>40:
        twage = 40*wage+(hours-40)*1.5*wage
    elif 0<=hours<=40:
        twage = hours*wage
    return twage

def getBMI(weight, height):
    '''
    输入体重和身高输出BMI
    :param weight: 体重kg
    :param height: 身高m
    :return:
    '''
    weight, height = float(weight), float(height)
    BMI = weight/(height**2)
    if 0<=BMI<18.5:
        result = "过轻"
    elif 18.5<=BMI<24:
        result = "正常"
    elif 24<=BMI<28:
        result = "过重"
    elif 28<=BMI<=32:
        result = "肥胖"
    elif 32<BMI:
        result = "非常肥胖"
    else:
        result = "你是鬼吗"
    return result

def maidwage(startTime, endTime):
    """
    从8点开始一小时25元，21点后一小时18元
    :param startTime: 00:00  24
    :param endTime: 00:00 24
    :return: 
    """
    startmin = int(startTime.split(":")[0]) * 60 + int(startTime.split(":")[1])
    endmin = int(endTime.split(":")[0]) * 60 + int(endTime.split(":")[1])
    if endmin - startmin>24*60:
        wge = "劳动强度太大"
    elif 0<=endmin - startmin<=24*60:
        if 21*60>=startmin>=480:
            if endmin<=21*60:
                wge = (endmin - startmin) * 25 / 60
            elif 21*60<endmin<=32*60:
                wge = (21 * 60 - startmin) * 25 / 60 + (endmin - 21 * 60) * 18 / 60
            elif 32*60<endmin<=startmin+24*60:
                wge = (21 * 60 - startmin + endmin - 32 * 60) * 25 / 60 + (32 * 60 - 21 * 60) * 18 / 60
        if 0<=startmin<480:
            if endmin<=480:
                wge = (endmin - startmin) * 18 / 60
            if 480<endmin<=21*60:
                wge = (8 * 60 - startmin) * 18 / 60 + (endmin - 8 * 60) * 25 / 60
            elif 21*60<endmin<=startmin+24*60:
                wge = (8 * 60 - startmin + endmin - 21 * 60) * 18 / 60 + (21 * 60 - 8 * 60) * 25 / 60
        if 21*60<=startmin<32*60:
            if endmin<=32*60:
                wge = (endmin - startmin) * 18 / 60
            if 32*60<endmin<=45*60:
                wge = (32 * 60 - startmin) * 18 / 60 + (endmin - 32 * 60) * 25 / 60
            elif 45*60<endmin<=startmin+24*60:
                wge = (32 * 60 - startmin + endmin - 45 * 60) * 18 / 60 + (45 * 60 - 32 * 60) * 25 / 60
    return wge

def getgrade1(grade):
    '''
    输入0-100之间的分数回应ABCDE
    :param grade: 你的分数
    :return: ABCDE其中之一 str
    '''
    if int(grade)>100 or int(grade)<0:
        result = "你可真牛逼"
    else:
        gradeindex = {10:"A", 9:"A",8:"B",7:"C",6:"D"}
        ind = int(grade)//10
        result = gradeindex.get(ind,"E")
    return result

def getgrade2(grade):
    grade = int(grade)
    gr = grade//10
    if gr==10 or gr ==9:
        result = "A"
    elif gr ==8:
        result = "B"
    elif  gr==7:
        result="C"
    elif gr ==6:
        result="D"
    elif 0<=gr<=5:
        result="E"
    else:
        result="你可真牛逼"
    return result

def main():
    # hours = input("input hours")
    # wage = input("input wage")
    # print(twage(hours, wage))
    # weight = input("input weight")
    # height = input("input height")
    # print(getBMI(weight, height))
    # startTime = input("input startTime")
    # endTime = input("input endTime")
    # print(maidwage(startTime,endTime))
    grade = input("input your grade")
    # print(getgrade1(grade))
    print(getgrade2(grade))

if __name__ == '__main__':
    main()