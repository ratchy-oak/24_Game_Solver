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
    if (listinput[1] == listinput[0] + 1 and listinput[2] == listinput[1] + 1 and listinput[3] == listinput[2] + 1) \
            or (listinput[0] == 7 and listinput[1] == 8 and listinput[2] == 9 and listinput[3] == 1) \
            or (listinput[0] == 8 and listinput[1] == 9 and listinput[2] == 1 and listinput[3] == 2) \
            or (listinput[0] == 9 and listinput[1] == 1 and listinput[2] == 2 and listinput[3] == 3):
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
