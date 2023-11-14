import array as arr
import operator

fixnumber = int(input("Enter fix number: "))
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
ansnumber = 18
count = 0
checklist = []

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

rawoperator = arr.array("i")
for i in range(111, 445):
    if "0" in str(i):
        continue
    elif "5" in str(i):
        continue
    elif "6" in str(i):
        continue
    elif "7" in str(i):
        continue
    elif "8" in str(i):
        continue
    elif "9" in str(i):
        continue
    else:
        rawoperator.append(i)

print("---------- ( X X ) X X ----------")
count1 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                    count += 1
                    count1 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
                elif fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                    count += 1
                    count1 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count1, "values in this operation.\n")

print("---------- X ( X X ) X ----------")
count2 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                    count += 1
                    count2 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
                elif fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                    count += 1
                    count2 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count2, "values in this operation.\n")

print("---------- X X ( X X ) ----------")
count3 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                    count += 1
                    count3 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
                elif fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                    count += 1
                    count3 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count3, "values in this operation.\n")

print("---------- ( X X ) ( X X ) ----------")
count4 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                    print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                    count += 1
                    count4 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count4, "values in this operation.\n")

print("---------- ( X X X ) X ----------")
count5 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                    count += 1
                    count5 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
                elif fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                    count += 1
                    count5 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count5, "values in this operation.\n")

print("---------- X ( X X X ) ----------")
count6 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                    count += 1
                    count6 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
                elif fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                    count += 1
                    count6 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count6, "values in this operation.\n")

print("---------- ( ( X X ) X ) X ----------")
count7 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                    print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                    count += 1
                    count7 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count7, "values in this operation.\n")

print("---------- ( X ( X X ) ) X ----------")
count8 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                    print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                    count += 1
                    count8 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count8, "values in this operation.\n")

print("---------- X ( ( X X ) X ) ----------")
count9 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                    print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3], ")")
                    count += 1
                    count9 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count9, "values in this operation.\n")

print("---------- X ( X ( X X ) ) ----------")
count10 = 0
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                    print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")", ")")
                    count += 1
                    count10 += 1
                    if listinput not in checklist:
                        checklist.append(listinput)
            except ZeroDivisionError:
                continue
print("There are", count10, "values in this operation.\n")

print("There are", count, "values in total operation.\n")

for i in checklist:
    i.sort()

checklist.sort()

result = []
for x in checklist:
    if x not in result:
        result.append(x)

print("There are", len(result), "sets of number that can be", ansnumber)

for i in result:
    print(i, end='\n')
