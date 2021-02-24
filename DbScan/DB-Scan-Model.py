# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:22:29 2020

@author: feyzanur.akyol2016
"""

import random
import numpy as np
from array import *
import matplotlib.pyplot as plt
from random import randint



def neighboorPoints (eps, minPts, points, pointIndex):
    #neighboors of one point
    neighboors = []
    #neighboors of all points    
    firstPoint = np.array(points[pointIndex])
    
    for j in range(len(points)):
        secondPoint = np.array(points[j])

        if ((np.linalg.norm(firstPoint - secondPoint)) <= eps): 
            neighboors.append(secondPoint)
    
    return neighboors

#returns index of the objects
def find (points,point):
    for i in range(len(points)):
        if(points[i] == point):
            return i
        
    #-1 is not found
    return -1


def dbscan(points,minPts,eps):
    
    visitedPoints = [0] * len(points)
    pointTypes = [0] * len(points)
    neighboors = []
    clusters = []
    noises = []
    
    point = points[0]
    index = 0
    while True:
        #mark point as a visited
        visitedPoints[index] = 1
        
        #calculate the neighboors
        neighboors = neighboorPoints(eps, minPts, points, index)
        
        #decide if it is core point
        if(len(neighboors) >= minPts):
            pointTypes[index] = "core"
            newCluster = []
            #clusters.append(newCluster)
            newCluster.append(points[index])
            
            n = []
            for p in neighboors:
                n.append(p.tolist())
        
            #adds neighboors in a cluster
            i = 0
            lenn = len(n)
            while(i < lenn):
                #if the neighboor is not equal the core point
                #and also not visited before
                if((n[i] != points[index]) and
                   (visitedPoints[find(points, n[i])] != 1)):
                    
                    visitedPoints[find(points, n[i])] = 1
                    
                    if (len(neighboorPoints(eps, minPts, points, find(points, n[i]))) >= minPts):
                        newNeigh = neighboorPoints(eps, minPts, points, find(points, n[i]))
                        for j in newNeigh:
                            n.append(j.tolist())
                            
                    added = False
                    for m in range(len(clusters)):
                        if(find(clusters[m], n[i]) != -1):
                            added = True
                            break
                    if(added == False):
                        newCluster.append(n[i])
                i = i + 1
                lenn = len(n)
            
                 
            if(len(newCluster) >= minPts):
                 clusters.append(newCluster)

        else:
            pointTypes[index] = "noise"
            noises.append(points[index])
               
        #find not visited new point's index
        for k in range(len(visitedPoints)):
            if(k > index):
                if(visitedPoints[k] == 0):
                    index = k
                    break
                
        #assigned it to point value          
        point = points[index]
        
        #end condition for while loop
        if (find(visitedPoints, 0) == -1):
            for y in range(len(pointTypes)):
                if(pointTypes[y] == 0):
                    pointTypes[y] = "border"
            break
            
    return clusters, pointTypes,noises

def plotData(clusters,noises):
    colors = []
    for i in range(40):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    
    clusters.append(noises)
    for i in range(len(clusters)):
        color = colors[i]
        h = color.lstrip('#')
        if(i == (len(clusters)-1)):
            print("NOISE COLOR: black")
            color = "black"
        x = []
        y = []

        for j in range(len(clusters[i])):
            x.append(clusters[i][j][0])
            y.append(clusters[i][j][1])

        plt.scatter(x,y,c=color,alpha=1,marker='.')


def main():
    coords = [[277, 127], [230, 108], [168, 215], [156, 113], [20, 284], [10, 294], [193, 291], [173, 106], [108, 51], [62, 284], [29, 211], [222, 248], [261, 284], [176, 251], [128, 88], [81, 237], [90, 295], [213, 89], [223, 41], [206, 92], [182, 148], [220, 63], [182, 108], [84, 22], [287, 55], [91, 223], [134, 253], [298, 278], [245, 55], [264, 150], [68, 37], [29, 18], [208, 31], [221, 6], [42, 12], [94, 204], [62, 126], [159, 183], [130, 262], [173, 81], [46, 132], [273, 104], [173, 124], [134, 279], [33, 50], [95, 188], [227, 272], [205, 195], [260, 48], [230, 189], [129, 154], [196, 186], [244, 201], [100, 258], [198, 174], [251, 162], [154, 154], [236, 15], [77, 41], [19, 153], [0, 252], [247, 11], [3, 171], [265, 289], [278, 71], [129, 210], [163, 265], [181, 100], [89, 94], [253, 9], [63, 160], [97, 12], [290, 228], [180, 147], [271, 157], [102, 247], [28, 146], [294, 229], [47, 213], [130, 91], [169, 16], [160, 106], [72, 16], [154, 93], [201, 185], [20, 194], [18, 276], [256, 127], [161, 13], [72, 257], [212, 263], [172, 207], [31, 154], [138, 174], [13, 89], [241, 252], [252, 118], [250, 60], [218, 215], [26, 161], [61, 289], [146, 298], [250, 114], [38, 278], [216, 55], [256, 61], [228, 39], [152, 198], [265, 194], [56, 239], [190, 114], [1, 244], [211, 193], [47, 123], [204, 157], [74, 58], [198, 147], [39, 178], [116, 176], [72, 284], [149, 1], [244, 59], [275, 202], [113, 120], [157, 238], [136, 280], [83, 247], [247, 160], [24, 258], [247, 186], [24, 266], [175, 115], [147, 187], [265, 299], [68, 225], [252, 50], [113, 203], [82, 233], [184, 98], [44, 13], [87, 33], [61, 285], [156, 279], [145, 242], [90, 54], [144, 130], [197, 188], [13, 270], [210, 83], [86, 261], [275, 178], [95, 9], [146, 266], [104, 223], [67, 64], [33, 210], [143, 95], [96, 256], [196, 173], [40, 196], [97, 38], [108, 72], [208, 222], [55, 183], [191, 60], [96, 39], [138, 48], [241, 155], [129, 107], [210, 228], [218, 268], [30, 15], [67, 133], [160, 23], [231, 193], [8, 261], [35, 17], [269, 28], [151, 216], [191, 56], [191, 69], [129, 208], [119, 14], [129, 165], [189, 97], [279, 145], [57, 276], [214, 40], [159, 126], [132, 276], [151, 68], [102, 283], [276, 29], [41, 231], [273, 70], [48, 73], [169, 4], [90, 219], [47, 111], [225, 104], [239, 120], [224, 39], [174, 100], [232, 215], [74, 63], [116, 34], [212, 97], [125, 172], [110, 151], [46, 259], [166, 153], [266, 153], [112, 195], [40, 9], [70, 293], [293, 193], [252, 140], [74, 152], [80, 281], [256, 77], [220, 10], [52, 160], [66, 190], [271, 281], [288, 181], [259, 237], [207, 250], [104, 41], [138, 160], [256, 167], [173, 98], [256, 235], [201, 71], [284, 228], [3, 73], [54, 3], [29, 220], [150, 277], [67, 37], [101, 216], [82, 231], [180, 239], [16, 142], [235, 101], [268, 191], [176, 284], [179, 196], [106, 186], [263, 134], [281, 272], [280, 201], [249, 25], [261, 190], [69, 129], [41, 231], [117, 242], [126, 230], [261, 72], [98, 230], [181, 13], [148, 63], [96, 228], [270, 258], [109, 242], [252, 178], [110, 128], [279, 126], [33, 61], [143, 181], [110, 171], [192, 264], [297, 217], [144, 110], [64, 176], [161, 58], [252, 194], [136, 110], [197, 31], [87, 112], [148, 114], [3, 100], [268, 271], [29, 292], [252, 24], [161, 11], [236, 90], [253, 219], [73, 287], [35, 90], [11, 271], [182, 289], [193, 163], [160, 225], [136, 99], [198, 297], [211, 22], [286, 102], [52, 93], [275, 107], [163, 226]]
    #coords = [[int(random.random()*300), int(random.random()*300)] for _ in range(300)]
    result = dbscan(coords,10,20)
    print("Total cluster number: ",len(result[0]))
    plotData(result[0],result[2])
    
    """
    result = dbscan(coords, 10,25)
    print("Total cluster number: ",len(result[0]))
    plotData(result[0],result[2])
    
    result = dbscan(coords, 10,30)
    print("Total cluster number: ",len(result[0]))
    plotData(result[0],result[2])
    
    result = dbscan(coords, 3,20)
    print("Total cluster number: ",len(result[0]))
    plotData(result[0],result[2])

    result = dbscan(coords, 4,20)
    print("Total cluster number: ",len(result[0]))
    plotData(result[0],result[2])
    
    result = dbscan(coords, 5,20)
    print("Total cluster number: ",len(result[0]))
    plotData(result[0],result[2])

    """
    



main()
