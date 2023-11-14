import array as arr

checklist = []

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] != listinput[1] and listinput[0] != listinput[2] and listinput[0] != listinput[3] and listinput[
        1] != listinput[0] and listinput[1] != listinput[2] and listinput[1] != listinput[3] and listinput[2] != \
            listinput[0] and listinput[2] != listinput[1] and listinput[2] != listinput[3] and listinput[3] != \
            listinput[0] and listinput[3] != listinput[1] and listinput[3] != listinput[2]:
        if listinput not in checklist:
            checklist.append(listinput)

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
