# SurvPy

Do you know how to describe an area of land in proper legal terms? It's actually pretty simple.

Let's say you want to describe the border of a square property. You start at a reference point, say, the southwest corner of a census block, then you proceed north for 500 feet, then east for 1000 feet, then south for 500 feet, then west 500 feet back to the starting point. Makes sense right? And in legal terms it looks like this:

Beginning at the southwest corner of the 3025 Census Block; Thence proceeding North 500 a distance of 500 feet; Thence West a distance of 1000 feet; Thence south a distance of 500 feet, Thence East to the point of beginning.

That is pretty easy and straightforward. But what happens when your border is not perfectly square? Or has a large number of segments? This process can become much more ticky very quickly. This project was created to automate the process of describing a land border in legal terms. In fact it was created to describe the legal boundary of a fire district that has over 1000 lines that needed to be described, The final document being over 20 pages long. Imagine doing that by hand.

How to use the script:

Create an input file (csv) that contains (optional) a number, then a direction and distance field. Make sure it is named properly or change the name in the code.

The script will convert the direction from a north azimuth to the proper legal terms and concatenate the distance rounded to two decimal places. The script will output a text file containin the legal description for all lines in the input list, unless the voidlines file is used and any lines that are included will be skipped and replaced with a place holder.
