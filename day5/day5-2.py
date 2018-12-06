"""
--- Part Two ---

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
"""

import os
import time

start_time = time.time()
f = open("./inputs/day5-test","r") 

line = f.readline()
#print(line)
line_lower = line.lower()
set_of_input = set(line.lower())
#print(set_of_input)
line_with_removed_units = ""
minim_length = 200000

for s in set_of_input:
    line_with_removed_units = line.replace(s.lower(), '')
    line_with_removed_units = line_with_removed_units.replace(s.upper(), '')
    #print("line", line_with_removed_units)
    chars = []
    for c in line_with_removed_units:
        chars += [c]

    explosive = True

    while explosive:
        #print(''.join(chars))
        explosive = False
        for i in range(len(chars) - 1):
            #print(chars[i].lower(), chars[i+1].lower())
            if chars[i].lower() == chars[i+1].lower():
                #print("entered")
                #print(chars[i], chars[i+1])
                if chars[i] != chars[i+1]:
                    #print("yes")
                    explosive = True
                    chars[i] = '0'
                    chars[i+1] = '0'
                    break
        chars_after_explosion = [x for x in chars if x != '0']
        chars = chars_after_explosion
    
    #print(''.join(chars))
    minim_length = min(minim_length,len(chars))
    #print(explosive)
#print(len(''.join(chars)))
print(minim_length)
print("--- Part TWO %s seconds ---" % (time.time() - start_time))