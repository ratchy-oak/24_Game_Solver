import array as arr
import operator
import numpy as np

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
fixnumber = int(input("Enter fix number: "))
ansnumber = 24
count = 0
setlist = []

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            listinput.sort()
            checkset = "{}".format(listinput)
            if checkset not in setlist:
                setlist.append(checkset)
            else:
                continue
        else:
            continue
    else:
        continue

print("\nThere are", len(setlist), "sets of number.")
setlist.sort()
for i in setlist:
    for j in i:
        print(j, end="")
    print()
