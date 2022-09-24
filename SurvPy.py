import math
import pandas as pd
from math import atan2, degrees

layerFile = "LayerTable.csv"

results = pd.read_csv(layerFile)
results = len(results)


print('Start at reference point, and  ')

for i in range(results):
    df = pd.read_csv(layerFile)
    #print(df.loc[[i], :])
    points = [list(row) for row in df.values]
    point_1 = points[i]
    point_2 = points[i+1]         # fix index out of range error
    angle = atan2(point_1[2] - point_2[2], point_1[1] - point_2[1])
    angle = degrees(angle)
    if 0 < angle < 90:             # fix overlapping angles at cardinals
        angle = 'N ' + str(angle) + ' degrees W'
    elif 90 <= angle <= 180:
        angle = 'S ' + str(180 - angle) + ' degrees E'
    elif 0 >= angle > -90:
        angle = 'N ' + str(abs(angle)) + ' degrees W'
    elif -90 >= angle >=-180:
        angle = 'S ' + str(180 - abs(angle)) + ' degrees W'
    distance = ((point_1[1] - point_2[1])**2 + (point_1[2] - point_2[2])**2)**0.5
    print('thence, ' + str(angle) + ' for ' + str(distance) + ' feet.')     # figure out terminology

    #print('point 1 ' + str(point_1[1]))
    #print('point 2 ' + str(point_2[1]))
    #print('The angle between point ' + str(i+1) + ' and ' + str(i+2) + ' is ' + str(angle))
    #print('And the distance between them is ' + str(distance) + ' units')

print("there are " + str(results) + " lines")