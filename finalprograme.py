# -*- coding: utf-8 -*-
'''
Created on 2022/5/26 21:09

'''
import turtle
import pandas as pd
import numpy as np
import plotly_express as px


def distances(x, y):
    result = np.dot(np.array(x) - np.array(y), np.array(x) - np.array(y))
    return result


def out_distances_matrix(X, Y):
    coor = list(zip(X, Y))
    mat = []  # 2d
    for i in coor:
        line = []  # 1d
        for j in coor:
            line.append(distances(i, j))
        mat.append(line)
    return mat


def out_shortest_distance_mat(N, X, Y):
    coor = list(zip(X, Y))
    city_info = list(zip(N, coor))
    mat = []
    for city, cor in city_info:
        value = []
        line = [city]
        for i, j in city_info:
            if city == i:
                continue
            value.append((i, distances(cor, j)))
        line = line + list(min(value, key=lambda x: x[1]))
        mat.append(line)
    return mat


def out_catogeorized_mat():
    xls = pd.read_excel("Assignment_Data.xlsx", sheet_name="CHN144",
                        header=None)  # header指选哪行作为剩下数据的表头 ，路径选填
    aryl = xls.to_numpy().T.tolist()  #表格转置
    city_names = aryl[0]
    X_coordinates = aryl[1]
    Y_coordinates = aryl[2]
    ori = pd.read_excel("Assignment_Data.xlsx", sheet_name="Shortest_Distance")  # header指选哪行作为剩下数据的表头
    lst = ori.to_numpy()
    short = lst[-21:-11]
    long = lst[-10:]
    short_city = short.T.tolist()[0]+short.T.tolist()[1]
    long_city = long.T.tolist()[0]+long.T.tolist()[1]
    xss = []
    yss = []
    for index, value in enumerate(city_names):
        for i in short_city:
            if i == value:
                xss.append(X_coordinates[index])
                yss.append(Y_coordinates[index])
    xlls = []
    ylls = []
    for index, value in enumerate(city_names):
        for i in long_city:
            if i == value:
                xlls.append(X_coordinates[index])
                ylls.append(Y_coordinates[index])
    X_coordinates = list(set(X_coordinates) - set(xss) - set(xlls))
    Y_coordinates = list(set(Y_coordinates) - set(yss) - set(ylls))
    mat = []
    for i in range(len(X_coordinates)):  # 添加normal行
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
    return mat

def task1():
    '''
    对任意一个城市City_i，计算它和其它143个城市的距离，在文件Assignment_Data.xlsx中建立一个名为Distance的sheet，将结果保存到其中。
在Distance中第一行和第一列的内容一样，为所有144个城市的名字，第i行第j列的单元格的内容即为第i个城市和第j个城市的距离。
    '''
    xls = pd.read_excel("Assignment_Data.xlsx", sheet_name="CHN144",
                        header=None)  # header指选哪行作为剩下数据的表头
    aryl = xls.to_numpy().T.tolist()  #表格转置
    city_names = aryl[0]
    X_coordinates = aryl[1]
    Y_coordinates = aryl[2]
    distance_matrix = out_distances_matrix(X_coordinates, Y_coordinates)

    data_frame = pd.DataFrame(distance_matrix, columns=city_names, index=city_names)#建立panda数据
    with pd.ExcelWriter("Assignment_Data.xlsx", mode="a", engine="openpyxl") as file_wirte:
        data_frame.to_excel(file_wirte, sheet_name="Distance")


def task2():
    '''
    在Assignment_Data.xlsx中建立一个名为Shortest_Distance的sheet，建立标题行，第一列为144个城市的名字，标题为“城市”，第二列为与第一列对应城市距离最近的城市名，标题为“最邻近的城市”，第三列为两个城市之间的距离，标题为“距离”。
    '''
    xls = pd.read_excel("Assignment_Data.xlsx", sheet_name="CHN144",
                        header=None)  # header指选哪行作为剩下数据的表头
    aryl = xls.to_numpy().T.tolist()  #表格转置
    city_names = aryl[0]
    X_coordinates = aryl[1]
    Y_coordinates = aryl[2]
    distance_matrix = out_shortest_distance_mat(city_names, X_coordinates, Y_coordinates)
    data_frame = pd.DataFrame(distance_matrix, columns=['城市', '最邻近的城市', '距离'])
    with pd.ExcelWriter("Assignment_Data.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as file_wirte:
        data_frame.to_excel(file_wirte, sheet_name="Shortest_Distance", index=None)


def task3():
    '''
    注意先运行taks2()
    找出这些城市中距离最近的10对城市，距离最远的10对城市，在Shortest_Distance表中写入这些信息。
    '''
    ori = pd.read_excel("Assignment_Data.xlsx", sheet_name="Shortest_Distance")  # header指选哪行作为剩下数据的表头
    com1 = ["以下为最短的10对城市", None, None]
    com2 = ["以下为最长的10对城市", None, None]
    lst = ori.to_numpy().tolist()
    lst.sort(key=lambda x: x[2])
    for i in lst:
        for j in lst:
            if i[1] == j[0] and i[0] == j[1]:
                lst.remove(j)
    df = []
    df.append(com1)
    df = df + lst[0:10]
    df.append(com2)
    df = df + lst[-10:]
    data_frame = pd.DataFrame(df, columns=['城市', '最邻近的城市', '距离'])
    new = pd.concat([ori, data_frame], ignore_index=True)
    with pd.ExcelWriter("Assignment_Data.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as file_wirte:
        new.to_excel(file_wirte, sheet_name="Shortest_Distance", index=None)


def task4():
    '''
    使用Turtle库，按坐标将这144个城市的位置用点表示出。如果需要，请对城市坐标进行适当的变换。将距离最近的10对城市和距离最远的10对城市用不同颜色标识出来。
    '''

    '''初始化turtle'''
    p = turtle.Turtle()
    turtle.setworldcoordinates(-1000, -1000, 8000, 4000)
    p.pensize(1)
    p.color('red')
    p.st()
    '''获取坐标表格'''
    mat = out_catogeorized_mat()
    for i in mat:
        if i[0]=='normal':
            p.penup()
            p.goto(i[1],i[2])
            p.dot(5, "red")
        if i[0]=="short":
            p.penup()
            p.goto(i[1],i[2])
            p.dot(5, "green")
        if i[0]=="long":
            p.penup()
            p.goto(i[1],i[2])
            p.dot(5, "blue")

    turtle.done()


def task5():
    '''
    使用plotly_express库，按坐标将这144个城市的位置用点表示出。如果需要，请对城市坐标进行适当的变换。将距离最近的10对城市和距离最远的10对城市用不同颜色标识出来。
    '''
    mat = out_catogeorized_mat()
    data_frame = pd.DataFrame(mat, columns=['category', "x", 'y'])
    fig = px.scatter(data_frame, x="x", y="y", color="category")
    fig.show()


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    task5()

