#this script takes a COGO vector direction and distance chart from ArcgGIS pro
#and converts it into a legal description for and area boundary. This was
#created to define the border of a fire district in legal terms.
#Writen by A.J. Thompson

import pandas as pd

#read input files
lineFile = "ProposedBoundary_COGO_lines.csv"
voidFile = "VoidLines.txt"

#create output file
f = open("out.txt", "w")

#read number of lines in input file for itteration range
results = pd.read_csv(lineFile)
results = len(results)

#read a voidline file to skip certain vector lines
void = open(voidFile, "r")  #open and read inputfile
voidLines = void.read() #assign inputfile contents to value
voidLines = voidLines.split(", ") #create list based on contents and splate using commas
voidLines = [eval(i) for i in voidLines] #convert list strings to integers

#read the vector file
df = pd.read_csv(lineFile)
lines = [list(row) for row in df.values]

#function for converting decimal degrees to degrees minutes seconds
def dd2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt,sec = divmod(abs(dd)*3600, 60)
    deg,mnt = divmod(mnt, 60)
    return str(round(mult*deg)) + "°" + str(round(mult*mnt)) + "'" + str(round(mult*sec)) + '"' # !make sure the rounding is right

#open the output file
f = open("out.txt", "a")

#loop through lines in input file based on range
for i in range(results):
    # check if voiding lines
    if i in voidLines:
        f.write("Thence [__];")
        #print("___")
    else:
        #print(i)
        #print(voidLines)
        line = lines[i]
        direction = line[1]
        distance = line[2]
        #check the lines for direction quadrant, and call dd2dms function, and 
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
        #write the vector line info
        #f.write('Thence ' + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet; ') #this is for final
        f.write('Thence (' + str(i + 1) + "), " + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet; ') #this is for working
        print('Thence (' + str(i + 1) + "), " + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet; ')

#close the output file. This script was created by A.J. Thompson
f.close()