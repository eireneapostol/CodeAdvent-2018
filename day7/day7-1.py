"""
--- Day 7: The Sum of Its Parts ---

You find yourself standing on a snow-covered coastline; apparently, you landed a little off course. The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions." It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----
Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:

Only C is available, and so it is done first.
Next, both A and F are available. A is first alphabetically, so it is done next.
Then, even though F was available earlier, steps B and D are now also available, and B is the first alphabetically of the three.
After that, only D and F are available. E is not available because only some of its prerequisites are complete. Therefore, D is completed next.
F is the only choice, so it is done next.
Finally, E is completed.
So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?
"""
import os
import time
import re
import json

start_time = time.time()

#letters = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#letters = ['A', 'B', 'C', 'D', 'E', 'F']
levels = {}
letters = set()


f = open("./inputs/day7","r") 
tuples = []

for line in f:
    _, step1, step2 = re.findall("[A-Z]", line)
    tuples += [(step1, step2)]
    letters.add(step1)
    letters.add(step2)

alph_len = len(letters)
print(alph_len)
for i in range(alph_len):
    levels[i] = []

for i in letters:
    levels[alph_len-1] += i

print(sorted(letters))

changed = True
while changed:
    changed = False
    for step1, step2 in tuples:
        #print(step1, step2)
        for i in range(alph_len):
            if step1 in levels[i]:
                step1_level = i
            if step2 in levels[i]:
                step2_level = i
        if (step1_level > step2_level) or (step1_level == step2_level):
            levels[step1_level].remove(step1)
            levels[step2_level - 1] += step1
            changed = True
string = "" 
for i in range(alph_len):
    for j in sorted(levels[i]):
        string += str(j)
        print(j,end="")
#print(json.dumps(levels,indent=3))
print("\n")
print(string)
print(len(string))
print("\n")

print("--- Part ONE %s seconds ---" % (time.time() - start_time))

