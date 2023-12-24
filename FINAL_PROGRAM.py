import array as arr
import operator
from collections import defaultdict
import pandas as pd
from itertools import permutations

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
fix_set = [2345, 2534, 2453, 2543, 3245, 3524, 3452, 3542, 4235, 4523, 4352, 4532, 5234, 5423, 5342, 5432]
resultlist = []
ansnumber = 24
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

# print("---------- X X X X ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if (operator1 == '+' or operator1 == '-') and (operator2 == '+' or operator2 == '-') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '+' or operator2 == '-') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '*' or operator2 == '/') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '*' or operator1 == '/') and (operator2 == '*' or operator2 == '/') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '*' or operator1 == '/') and (operator2 == '*' or operator2 == '/') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '*' or operator1 == '/') and (operator2 == '+' or operator2 == '-') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '*' or operator2 == '/') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- ( X X ) X X ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if (operator2 == '*' or operator2 == '/') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator2 == '+' or operator2 == '-') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator2 == '+' or operator2 == '-') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator2 == '*' or operator2 == '/') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                        checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- X ( X X ) X ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if (operator1 == '*' or operator1 == '/') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '*' or operator1 == '/') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- X X ( X X ) ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if (operator1 == '*' or operator1 == '/') and (operator2 == '+' or operator2 == '-'):
                    resultnumber = fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '*' or operator2 == '/'):
                    resultnumber = fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3])))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '+' or operator2 == '-'):
                    resultnumber = fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
                elif (operator1 == '*' or operator1 == '/') and (operator2 == '*' or operator2 == '/'):
                    resultnumber = fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- ( X X ) ( X X ) ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                resultnumber = fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3]))
                # resultlist.append(resultnumber)
                if resultnumber == ansnumber:
                    print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                    checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- ( X X X ) X ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if (operator1 == '*' or operator1 == '/') and (operator2 == '+' or operator2 == '-'):
                    resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '*' or operator2 == '/'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '+' or operator1 == '-') and (operator2 == '+' or operator2 == '-'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
                elif (operator1 == '*' or operator1 == '/') and (operator2 == '*' or operator2 == '/'):
                    resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                        checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- X ( X X X ) ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                if (operator2 == '*' or operator2 == '/') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
                elif (operator2 == '+' or operator2 == '-') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3])))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
                elif (operator2 == '+' or operator2 == '-') and (operator3 == '+' or operator3 == '-'):
                    resultnumber = fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
                elif (operator2 == '*' or operator2 == '/') and (operator3 == '*' or operator3 == '/'):
                    resultnumber = fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3]))
                    # resultlist.append(resultnumber)
                    if resultnumber == ansnumber:
                        print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                        checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- ( ( X X ) X ) X ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                resultnumber = fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3])
                # resultlist.append(resultnumber)
                if resultnumber == ansnumber:
                    print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                    checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- ( X ( X X ) ) X ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                resultnumber = fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3])
                # resultlist.append(resultnumber)
                if resultnumber == ansnumber:
                    print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                    checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- X ( ( X X ) X ) ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                resultnumber = fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3]))
                # resultlist.append(resultnumber)
                if resultnumber == ansnumber:
                    print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3], ")")
                    checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

# print("---------- X ( X ( X X ) ) ----------")
for i in range(0, 6561):
    if rawinput[i] in fix_set:
        listinput = [int(x) for x in str(rawinput[i])]
        for j in range(0, 64):
            listoperator = [int(x) for x in str(rawoperator[j])]
            operator1, fn1 = operators[listoperator[0] - 1]
            operator2, fn2 = operators[listoperator[1] - 1]
            operator3, fn3 = operators[listoperator[2] - 1]
            try:
                resultnumber = fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3])))
                # resultlist.append(resultnumber)
                if resultnumber == ansnumber:
                    print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")", ")")
                    checklist.append(listinput)
            except ZeroDivisionError:
                resultnumber = "N/A"
                # resultlist.append(resultnumber)

result = []
for x in resultlist:
    if x not in result:
        result.append(x)

for i in checklist:
    i.sort()

checklist.sort()

want_result = []
for x in checklist:
    if x not in want_result:
        want_result.append(x)

print("There are", len(want_result), "sets of number that can be", ansnumber)

for i in want_result:
    print(i, end='\n')

# d = defaultdict(int)
# L = resultlist
# for i in L:
#     d[i] += 1
#
# data_items = d.items()
# data_list = list(data_items)
# df = pd.DataFrame(data_list, columns=["Result", "Times"])
# df = df.sort_values(by=['Times'], ascending=False)
# print(df.to_string(index=False))

d = defaultdict(int)
L = tuple(map(tuple, checklist))
for i in L:
    d[i] += 1

data_items = d.items()
data_list = list(data_items)
df = pd.DataFrame(data_list, columns=["Set", "Times"])
df = df.sort_values(by=['Times'], ascending=False)
print(df.to_string(index=False))
