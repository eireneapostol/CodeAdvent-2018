"""

Your puzzle answer was 84834.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 99 * 45 = 4455.)
"""

import os
import time
import re
import numpy as np

start_time = time.time()
f = open("./inputs/day4","r") 

inputs = []
time_dict = {}

for line in f:
    inputs = inputs + [line]
guard = 0
guards = []

for n in inputs:
    hours_and_minutes = re.findall("[0-9][0-9]\:[0-9][0-9]", n)
    hours, minutes = hours_and_minutes[0].split(":")
    text = n.split("]")[1]
    if "#" in text:
        guard = int(re.findall("[0-9]+",text)[0])
        if guard not in time_dict:
            time_dict[guard] = np.zeros(60)
        if guard not in guards:
            guards+=[guard]
    if "falls" in text:
        minute_falled = int(minutes)
    if "wakes" in text:
        minute_awake = int(minutes)
        for i in range(minute_falled, minute_awake):
            time_dict[guard][i] += 1 

most_slept_minute = 0
max_times_most_slept_minute = 0
guard_with_most_slept_minute = 0
for g in guards:
    for i in range(60):
        if max_times_most_slept_minute < time_dict[g][i]:
            max_times_most_slept_minute = time_dict[g][i]
            most_slept_minute = i
            guard_with_most_slept_minute = g
        

print(most_slept_minute*guard_with_most_slept_minute)
print("--- Part TWO %s seconds ---" % (time.time() - start_time))
