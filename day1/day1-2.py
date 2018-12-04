"""
--- Part Two ---

You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
What is the first frequency your device reaches twice?
"""

import os
import time

start_time = time.time()
f = open("./inputs/day1","r") 

suma = 0
list_suma = {0}
inputs = []

for line in f:
    inputs = inputs + [int(line)]

inputs_len = len(inputs)
found_duplicate = False
n = 0

while found_duplicate == False:
    suma += int(inputs[n%inputs_len])
    if suma in list_suma:
        print(suma)
        found_duplicate = True
    else:
        list_suma.add(int(suma))
        n += 1
            

#print(inputs)
#print(list_suma)
#print(suma)

print("--- Part TWO %s seconds ---" % (time.time() - start_time))