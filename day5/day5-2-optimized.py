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
f = open("./inputs/day5","r") 

line = f.readline()
set_of_input = set(line.lower())
minim_length = 200000

def explode(s):
    upper = str.upper
    lower = str.lower
    new = line.replace(lower(s), '')
    new = new.replace(upper(s), '')
    old = ""
    while len(new) != len(old):
        old = new
        for i in set_of_input:
            new = new.replace(i+upper(i),'')
            new = new.replace(upper(i)+i,'')
    return(len(new))

lengths = [explode(s) for s in set_of_input]
print(min(lengths))
print("--- Day 5 Part TWO Optimized  %s seconds ---" % (time.time() - start_time))