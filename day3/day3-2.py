"""
--- Part Two ---

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?

"""

import os
import time
import re
import numpy as np

start_time = time.time()
f = open("./inputs/day3","r") 

x_max = 2000
y_max = 2000

array = np.zeros((x_max, y_max))
inputs = []

for line in f:
    inputs = inputs + [line]

for n in inputs:
    numbers = re.findall("[0-9]+",n)
    y_dist = int(numbers[1]) # inches from left edge to fabric
    x_dist = int(numbers[2]) # inches from top to fabric
    width = int(numbers[3])
    length = int(numbers[4])
    nr = int(numbers[0])

    for i in range(x_dist, x_dist + length):
        for j in range( y_dist, y_dist + width):
            array[i][j] += nr
for n in inputs:
    numbers = re.findall("[0-9]+",n)
    y_dist = int(numbers[1]) # inches from left edge to fabric
    x_dist = int(numbers[2]) # inches from top to fabric
    width = int(numbers[3])
    length = int(numbers[4])
    nr = int(numbers[0])
    overlap = False
    for i in range(x_dist, x_dist + length):
        for j in range( y_dist, y_dist + width):
            if array[i][j] != nr:
                overlap = True
    if not overlap:
        print(nr)

print("--- Part TWO %s seconds ---" % (time.time() - start_time))
