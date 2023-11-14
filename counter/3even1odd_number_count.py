import array as arr
from itertools import permutations

evennumber = [2, 4, 6, 8]
oddnumber = [1, 3, 5, 7, 9]
checklist = []

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] in evennumber and listinput[1] in evennumber and listinput[2] in evennumber and listinput[3] in oddnumber:
        for p in permutations(listinput):
            p = list(p)
            if p not in checklist:
                checklist.append(p)

for i in checklist:
    i.sort()

checklist.sort()

result = []
for x in checklist:
    if x not in result:
        result.append(x)

print("There are", len(result), "sets of number")

for i in result:
    print(i, end='\n')
