#this script takes a COGO vector direction and distance chart from ArcgGIS pro
#and converts it into a legal description for and area boundary. This was
#created to define the border of a fire district in legal terms.
#Created by A.J. Thompson

import pandas as pd

#read input files
lineFile = "ProposedBoundary_COGO.csv"
editFile = "editLines.txt"

#create/overwrite output files
f = open("out.txt", "w") 
e = open("cardinals.csv", "w") #this file is for use in arcpro

#read number of lines in input file for itteration range
results = pd.read_csv(lineFile)
results = len(results)

#read a voidline file to skip certain vector lines
edit = open(editFile, "r")  #open and read inputfile
editLines = edit.read() #assign inputfile contents to value
editLines = editLines.split(", ") #create list based on contents and splate using commas
editLines = [eval(i) for i in editLines] #convert list strings to integers

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
e = open("cardinals.csv", "a") #use in arcpro
#loop through lines in input file based on range
for i in range(results):
    #print(i)
    #print(voidLines)
    line = lines[i]
    direction = line[1]
    distance = line[2]
    #check the lines for direction quadrant, and call dd2dms function, and 
    if 0 < direction < 90:
        direction_dms = direction
        direction = 'North ' + str(dd2dms(direction_dms)) + ' East'
        arcdirection = 'N ' + str(dd2dms(direction_dms)) + ' E'
    elif 90 < direction < 180:
        direction_dms = 180 - direction
        direction = 'South ' + str(dd2dms(direction_dms)) + ' East'
        arcdirection = 'S ' + str(dd2dms(direction_dms)) + ' E'
    elif 180 < direction < 270:
        direction_dms = 90 - (270 - direction) #inverting angle
        direction = 'South ' + str(dd2dms(direction_dms)) + ' West'
        arcdirection = 'S ' + str(dd2dms(direction_dms)) + ' W'
    elif 270 < direction < 360:
        direction_dms = 360 - direction
        direction = 'North ' + str(dd2dms(direction_dms)) + ' West'
        arcdirection = 'N ' + str(dd2dms(direction_dms)) + ' W'
    elif direction == 0:
        direction = 'Northerly'
    elif direction == 90:
        direction = 'Easterly'
    elif direction == 180:
        direction = 'Southerly'
    elif direction == 270:
        direction = 'Westerly'
    #write the vector line info
    writeBearing = ('Thence ' + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet; ')
    writeBearingplusnum = ('Thence (' + str(i + 1) + "), " + str(direction) + ' a distance of ' + str(round(distance, 2)) + ' feet')
    if i in editLines:
        f.write(writeBearingplusnum + " along the boundary of the _ ; ")
        print(writeBearingplusnum + " along the boundary of the _ ; ")
    else:
        f.write(writeBearing + "; ")
        print(writeBearing + "; ")
    e.write(arcdirection + ", ") #use in arcpro

#close the output file. This script was created by A.J. Thompson
f.close()
e.close() # use in arcpro