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
f = open("./inputs/day5-test","r") 

line = f.readline()
explosive = True
print(line)
print(len(line))

while explosive:
    explosive = False
    string_after_explosion = ""
    my_range = len(line) - 4
    for i in range(my_range):
        print(i)
        print(line[i], line[i+1])
        if (line[i].lower() == line[i+1].lower()):
            if line[i].isupper() and line[i+i].islower():
                if  line[i+1].isupper() and line[i].islower():
                    explosive = True
                    print("YES")
        print(string_after_explosion)
    line = string_after_explosion

print(line)

print("--- Part ONE %s seconds ---" % (time.time() - start_time))
