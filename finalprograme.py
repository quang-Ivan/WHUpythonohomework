# -*- coding: utf-8 -*-
'''
Created on 2022/5/26 21:09

'''
import turtle

import pandas as pd
import numpy as np

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
    ori = pd.read_excel("Assignment_Data.xlsx", sheet_name="Shortest_Distance")  # header指选哪行作为剩下数据的表头
    com1 = ["以下为最短的10对城市",None,None]
    com2 = ["以下为最长的10对城市", None, None]
    lst= ori.to_numpy().tolist()
    lst.sort(key = lambda x: x[2])
    for i in lst:
        for j in lst:
            if i[2]==j[2] and i!=j:
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
    turtle.screensize(1000,800)
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
if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    task4()