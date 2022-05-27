# -*- coding: utf-8 -*-
'''
Created on 2022/5/26 21:09

'''
import turtle

import pandas as pd
import numpy as np
import plotly_express as px

def distances(x, y):
    result = np.dot(np.array(x)-np.array(y),np.array(x)-np.array(y))
    return result

def out_distances_matrix(X,Y):
    coor = list(zip(X,Y))
    mat = [] #2d
    for i in coor:
        line = []   #1d
        for j in coor:
            line.append(distances(i,j))
        mat.append(line)
    return mat

def out_shortest_distance_mat(N,X,Y):
    coor = list(zip(X, Y))
    city_info = list(zip(N, coor))
    mat = []
    for city,cor in city_info:
        value = []
        line = [city]
        for i, j in city_info:
            if city == i:
                continue
            value.append((i,distances(cor,j)))
        line = line+list(min(value,key=lambda x:x[1]))
        mat.append(line)
    return mat

    
def task1():
    xls = pd.read_excel("Assignment_Data.xlsx",sheet_name = "CHN144",header = None)#header指选哪行作为剩下数据的表头
    city_names = []
    X_coordinates = []
    Y_coordinates = []
    cities = xls.values
    for city in cities:
        X_coordinates.append(city[1])      #获得满的X坐标
        Y_coordinates.append(city[2])
        city_names.append(city[0])
    distance_matrix = out_distances_matrix(X_coordinates,Y_coordinates)

    data_frame = pd.DataFrame(distance_matrix,columns=city_names,index = city_names)
    with pd.ExcelWriter("Assignment_Data.xlsx",mode="a",engine="openpyxl") as file_wirte:
        data_frame.to_excel(file_wirte,sheet_name="Distance")

def task2():
    xls = pd.read_excel("Assignment_Data.xlsx",sheet_name = "CHN144",header = None)#header指选哪行作为剩下数据的表头
    city_names = []
    X_coordinates = []
    Y_coordinates = []
    cities = xls.values
    for city in cities:
        X_coordinates.append(city[1])      #获得满的X坐标
        Y_coordinates.append(city[2])
        city_names.append(city[0])
    distance_matrix = out_shortest_distance_mat(city_names,X_coordinates,Y_coordinates)
    data_frame = pd.DataFrame(distance_matrix,columns=['城市','最邻近的城市','距离'])
    with pd.ExcelWriter("Assignment_Data.xlsx",mode="a",engine="openpyxl",if_sheet_exists="replace") as file_wirte:
        data_frame.to_excel(file_wirte,sheet_name="Shortest_Distance",index=None)

def task3():
    '''
    注意先运行taks2()
    :return:
    '''
    ori = pd.read_excel("Assignment_Data.xlsx", sheet_name="Shortest_Distance")  # header指选哪行作为剩下数据的表头
    com1 = ["以下为最短的10对城市",None,None]
    com2 = ["以下为最长的10对城市", None, None]
    lst= ori.to_numpy().tolist()
    lst.sort(key = lambda x: x[2])
    for i in lst:
        for j in lst:
            if i[1]==j[0] and i[0]==j[1]:
                lst.remove(j)
    df = []
    df.append(com1)
    df = df + lst[0:10]
    df.append(com2)
    df = df + lst[-10:]
    data_frame = pd.DataFrame(df,columns=['城市','最邻近的城市','距离'])
    new =pd.concat([ori,data_frame],ignore_index=True)
    with pd.ExcelWriter("Assignment_Data.xlsx",mode="a",engine="openpyxl",if_sheet_exists="replace") as file_wirte:
        new.to_excel(file_wirte,sheet_name="Shortest_Distance",index=None)

def task4():
    p = turtle.Turtle()
    turtle.setworldcoordinates(-100, -100, 800, 400)
    p.pensize(1)
    p.color('red')
    p.st()
    xls = pd.read_excel("Assignment_Data.xlsx",sheet_name = "CHN144",header = None)#header指选哪行作为剩下数据的表头
    city_names = []
    X_coordinates = []
    Y_coordinates = []
    cities = xls.values
    for city in cities:
        X_coordinates.append(city[1])      #获得满的X坐标
        Y_coordinates.append(city[2])
        city_names.append(city[0])
    coor = [[j*0.1 for j in i] for i in list(zip(X_coordinates, Y_coordinates))]
    city_info = list(zip(city_names,coor))
    for i in coor:
        p.penup()
        p.goto(i)
        p.dot(5, "red")

    ori = pd.read_excel("Assignment_Data.xlsx", sheet_name="Shortest_Distance")  # header指选哪行作为剩下数据的表头
    lst = ori.to_numpy().tolist()
    short = lst[-21:-11]
    long = lst[-10:]
    for _ in short:
        i = _[0]
        j = _[1]
        for ci in city_info:
            if i==ci[0] or j==ci[0]:
                p.penup()
                p.goto(ci[1])
                p.dot(5, "green")
    for _ in long:
        i = _[0]
        j = _[1]
        for ci in city_info:
            if i == ci[0] or j == ci[0]:
                p.penup()
                p.goto(ci[1])
                p.dot(5, "blue")
    turtle.done()

def task5():
    xls = pd.read_excel(r"D:\OneDrive - aierlmalee\whu\python\Assignment_Data.xlsx", sheet_name="CHN144",
                        header=None)  # header指选哪行作为剩下数据的表头
    city_names = []
    X_coordinates = []
    Y_coordinates = []
    cities = xls.values
    for city in cities:
        X_coordinates.append(city[1])  # 获得满的X坐标
        Y_coordinates.append(city[2])
        city_names.append(city[0])
    coor = [[j * 0.1 for j in i] for i in list(zip(X_coordinates, Y_coordinates))]
    city_info = list(zip(city_names, coor))
    fig = px.scatter(X_coordinates, Y_coordinates)
    ori = pd.read_excel(r"D:\OneDrive - aierlmalee\whu\python\Assignment_Data.xlsx", sheet_name="Shortest_Distance")  # header指选哪行作为剩下数据的表头
    lst = ori.to_numpy().tolist()
    short = lst[-21:-11]
    long = lst[-10:]
    short_city = []
    long_city = []
    for i in short:
        short_city.append(i[0])
        short_city.append(i[1])
    for i in long:
        long_city.append(i[0])
        long_city.append(i[1])
    xss = []
    yss = []
    for index,value in enumerate(city_names):
        for i in short_city:
            if i==value:
                xss.append(X_coordinates[index])
                yss.append(Y_coordinates[index])
    xlls = []
    ylls = []
    for index,value in enumerate(city_names):
        for i in long_city:
            if i==value:
                xlls.append(X_coordinates[index])
                ylls.append(Y_coordinates[index])
    X_coordinates=list(set(X_coordinates)-set(xss)-set(xlls))
    Y_coordinates = list(set(Y_coordinates) - set(yss) - set(ylls))
    mat = []
    for i in range(len(X_coordinates)):    #添加normal行
        ad = ['normal']
        ad.append(X_coordinates[i])
        ad.append(Y_coordinates[i])
        mat.append(ad)
    for i in range(len(xss)):
        ad = ['short']
        ad.append(xss[i])
        ad.append(yss[i])
        mat.append(ad)
    for i in range(len(xlls)):
        ad = ['long']
        ad.append(xlls[i])
        ad.append(ylls[i])
        mat.append(ad)
    data_frame = pd.DataFrame(mat,columns=['category',"x",'y'])
    fig = px.scatter(data_frame,x="x",y="y",color="category")
    fig.show()

if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    task5()