import pandas as pd

pointFile = "input.csv"

results = pd.read_csv(pointFile)
results = len(results) + 1
print("there are " + str(results) + " lines")

df = pd.read_csv(pointFile)
lines = [list(row) for row in df.values]

for i in range(results):
    direction = lines[2]
    distance = lines[3]
    if 0 < direction > 90:
        direction = 'N ' + str(direction) + ' degrees E'
    elif 00 < direction > 180:
        direction = 'S ' + str(180 - direction) + ' degrees E'
    elif 180 < direction > 270:
        direction = 'S ' + str(270 - direction) + ' degrees W'
    elif 270 < direction > 360:
        direction = 'N ' + str(360 - direction) + ' degrees W'
    print('thence, ' + str(direction) + ' for ' + str(distance) + ' feet.')     # figure out terminology


    #round distance to 2 decimals, round seconds