import array as arr
from itertools import permutations

fixnumber = int(input("Enter fix number: "))
checklist = []

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] != fixnumber and listinput[3] != fixnumber:
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
