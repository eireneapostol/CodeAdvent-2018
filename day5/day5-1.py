"""
--- Day 5: Alchemical Reduction ---

You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? 
"""

import os
import time

start_time = time.time()
f = open("./inputs/day5","r") 

line = f.readline()
chars = []
for c in line:
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
    #print(explosive)
print(len(''.join(chars)))

print("--- Part ONE %s seconds ---" % (time.time() - start_time))
