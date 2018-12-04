"""
--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
"""
import os
import time

start_time = time.time()
f = open("./inputs/day2","r") 

inputs = []

for line in f:
    inputs = inputs + [line]

for i in range(len(inputs) - 2):
    for k in range(i,len(inputs)-1):
        s1 = inputs[i]
        s2 = inputs[k]
        diff = [j for j in range(len(s1)) if s1[j] != s2[j]]
        if len(diff) == 1:
            position = diff[0]
            print(s1[:position]+s1[(position+1):])

print("--- Part TWO %s seconds ---" % (time.time() - start_time))