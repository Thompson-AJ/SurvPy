import pandas as pd

lineFile = "ProposedBoundary_COGO_lines.csv"
f = open("out.txt", "x")

results = pd.read_csv(lineFile)
results = len(results) + 1
print("there are " + str(results) + " lines")

df = pd.read_csv(lineFile)
lines = [list(row) for row in df.values]
x = 0

def dd2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt,sec = divmod(abs(dd)*3600, 60)
    deg,mnt = divmod(mnt, 60)
    return str(round(mult*deg)) + "°" + str(round(mult*mnt)) + "'" + str(round(mult*sec)) + '"' # make sure the rounding is right

for i in range(results):
    line = lines[x]
    print(x)
    direction = line[1]
    distance = line[2]

    if 0 < direction < 90:
        direction_dms = direction
        direction = 'North ' + str(dd2dms(direction_dms)) + ' East'
    elif 90 < direction < 180:
        direction_dms = 180 - direction
        direction = 'South ' + str(dd2dms(direction_dms)) + ' East'
    elif 180 < direction < 270:
        direction_dms = 270 - direction
        direction = 'South ' + str(dd2dms(direction_dms)) + ' West'
    elif 270 < direction < 360:
        direction_dms = 360 - direction
        direction = 'North ' + str(dd2dms(direction_dms)) + ' West'
    elif direction == 0:
        direction = 'North'
    elif direction == 90:
        direction = 'East'
    elif direction == 180:
        direction = 'South'
    elif direction == 270:
        direction = 'West'
    f = open("out.txt", "a")
    f.write('Thence ' + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet; ')
    f.close()
    x = x + 1
    print('Thence (' + str(i) + "), " + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet; ')     # figure out terminology