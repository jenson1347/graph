import copy
from data_creator import *
def DataReader(name):
    data_graph = {}
    points = []
    listX = []
    listY= []
    with open(f"{name}", "r") as file:
        readName = file.readline()
        funcName = readName[:-1]
        # data_graph[funcName] = {}
        # data_graph[funcName]['Name'] = funcName
        # data_graph[funcName]['X'] = []
        # data_graph[funcName]['Y'] = []
        # data_graph[funcName]['points'] = []
        data_graph= {}
        data_graph['Name'] = funcName
        data_graph['X'] = []
        data_graph['Y'] = []
        data_graph['points'] = []
        for line in file:
            pointRead = line
            point = pointRead.split(",")
            try:
                point_x = float(point[0])
                data_graph['X'].append(point_x)
                #listX.append(point_x)
                point_y = float(point[1])
                data_graph['Y'].append(point_y)
                #listY.append(point_y)
                data_graph['points'].append([point_x,point_y])
                #points.append([point_x,point_y])
            except:
                point_x = float(point[0])
                data_graph['X'].append(point_x)
                #listX.append(point_x)
                point_y = 'error'
                data_graph['Y'].append(point_y)
                #listY.append(point_y)
                data_graph['points'].append([point_x,point_y])


        #points.append(list(map(float,point)))
            #points.append(point)
    return data_graph


