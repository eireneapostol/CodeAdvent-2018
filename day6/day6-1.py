"""
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

[[1 1 1 1 1 0 3 3 3 3]
 [1 1 1 1 1 0 3 3 3 3]
 [1 1 1 4 4 5 3 3 3 3]
 [1 1 4 4 4 5 3 3 3 3]
 [0 0 4 4 4 5 5 3 3 3]
 [2 2 0 4 5 5 5 5 3 3]
 [2 2 2 0 5 5 5 5 0 0]
 [2 2 2 0 5 5 5 6 6 6]
 [2 2 2 0 5 5 6 6 6 6]
 [2 2 2 0 6 6 6 6 6 6]]
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
"""
import os
import time
import numpy as np
from math import sqrt

start_time = time.time()
f = open("./inputs/day6","r") 

x_max = 500
y_max = 500
array_distance = np.full((x_max,y_max),x_max*2+1)
array_points = np.full((x_max, y_max),x_max*2+1)

point = 0
margins = set()

def manhattan(x1,y1,x2,y2):
    return(abs(x1-x2)+abs(y1-y2))

for line in f:
    point += 1
    y, x = line.split(", ")
    y = int(y)
    x = int(x)
    for x1 in range(x_max):
        for y1 in range(y_max):
            dist = manhattan(x,y,x1,y1)
            if ( dist < array_distance[x1][y1]):
                array_distance[x1][y1] = dist
                array_points[x1][y1] = point
            elif x == x1 and y  == y1:
                print(x1,y1)
                array_points[x1][y1] = point
                array_distance[x1][y1] = 0
            elif dist == array_distance[x1][y1]:
                array_points[x1][y1] = 0

for i in range(x_max):
    margins.add(array_points[i][x_max-1])
    margins.add(array_points[0][i])
    margins.add(array_points[x_max-1][i])
    margins.add(array_points[i][0])
    
maxim = 0
for p in range(1,point+1):
    if p not in margins:
        maxim = max((array_points == p).sum(), maxim)
    

print(maxim)

print("--- Day 6 Part ONE %s seconds ---" % (time.time() - start_time))