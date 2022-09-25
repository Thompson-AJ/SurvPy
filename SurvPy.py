import math
import pandas as pd
from math import atan2, degrees

layerFile = "LayerTable.csv"

results = pd.read_csv(layerFile)
results = len(results) + 1
print("there are " + str(results) + " lines")

print('Start at reference point, and  ')

df = pd.read_csv(layerFile)
points = [list(row) for row in df.values]

for i in range(results - 2):
    point_1 = points[i]
    point_2 = points[i+1]
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


#DMS format
# -----------------------------

def dd2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt,sec = divmod(abs(dd)*3600, 60)
    deg,mnt = divmod(mnt, 60)
    return mult*deg, mult*mnt, round(mult*sec, 2)


for i in range(results - 2):
    point_1 = points[i]
    point_2 = points[i+1]
    angle = atan2(point_1[2] - point_2[2], point_1[1] - point_2[1])
    angle = degrees(angle)
    if 0 < angle < 90:             # fix overlapping angles at cardinals
        angle_dms = angle
        angle = 'N ' + str(dd2dms(angle_dms)) + ' degrees W'
    elif 90 <= angle <= 180:
        angle_dms = 180 - angle
        angle = 'S ' + str(dd2dms(angle_dms)) + ' degrees E'
    elif 0 >= angle > -90:
        angle_dms = abs(angle)
        angle = 'N ' + str(dd2dms(angle_dms)) + ' degrees W'
    elif -90 >= angle >=-180:
        angle_dms = 180 - abs(angle)
        angle = 'S ' + str(dd2dms(angle_dms)) + ' degrees W'
    distance = ((point_1[1] - point_2[1])**2 + (point_1[2] - point_2[2])**2)**0.5
    print(str(i) + 'thence, ' + str(angle) + ' for ' + str(distance) + ' feet.')     # figure out terminology