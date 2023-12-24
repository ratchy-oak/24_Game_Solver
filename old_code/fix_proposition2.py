import array as arr
import operator
import numpy as np

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
fixnumber = int(input("Enter fix number: "))
ansnumber = 24
count = 0
setlist = []
countlist = []

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

count1 = 0
print("---------- ( X ? X ) ? X ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count1 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2],operator3, listinput[3])
                                    count += 1
                                    count1 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count1 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count1, "values in this operation.\n")

count2 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop3 = "{}".format(operator3)
                        if (checkop1 == "*" and checkop3 == "+") or (checkop1 == "*" and checkop3 == "-") or (checkop1 == "/" and checkop3 == "+") or (checkop1 == "/" and checkop3 == "-"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count2 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop3 == "*") or (checkop1 == "+" and checkop3 == "/") or (checkop1 == "-" and checkop3 == "*") or (checkop1 == "-" and checkop3 == "/"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count2 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count2 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count2, "values in this operation.\n")

count3 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count3 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count3 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count3 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count3, "values in this operation.\n")

count4 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                                count += 1
                                count4 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count4, "values in this operation.\n")

count5 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count5 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count5 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count5 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count5, "values in this operation.\n")

count6 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count6 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count6 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count6 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count6, "values in this operation.\n")

count7 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                            print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                            count += 1
                            count7 += 1
                            checkcount = "{}".format(listinput)
                            if checkcount not in countlist:
                                countlist.append(checkcount)
                            else:
                                continue
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
    else:
        continue
print("There are", count7, "values in this operation.\n")

count8 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn2(listinput[1], listinput[2]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                                count += 1
                                count8 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count8, "values in this operation.\n")

count9 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")",
                                      operator3, listinput[3], ")")
                                count += 1
                                count9 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count9, "values in this operation.\n")

count10 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber:
        if listinput[2] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                            continue
                        elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2],
                                      operator3, listinput[3], ")", ")")
                                count += 1
                                count10 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count10, "values in this operation.\n")

count11 = 0
print("---------- ( X ? X ) ? X ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count11 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2],operator3, listinput[3])
                                    count += 1
                                    count11 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count11 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count11, "values in this operation.\n")

count12 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop3 = "{}".format(operator3)
                        if (checkop1 == "*" and checkop3 == "+") or (checkop1 == "*" and checkop3 == "-") or (checkop1 == "/" and checkop3 == "+") or (checkop1 == "/" and checkop3 == "-"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count12 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop3 == "*") or (checkop1 == "+" and checkop3 == "/") or (checkop1 == "-" and checkop3 == "*") or (checkop1 == "-" and checkop3 == "/"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count12 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count12 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count12, "values in this operation.\n")

count13 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count13 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count13 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count13 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count13, "values in this operation.\n")

count14 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                                count += 1
                                count14 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count14, "values in this operation.\n")

count15 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count15 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count15 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count15 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count15, "values in this operation.\n")

count16 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count16 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count16 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count16 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count16, "values in this operation.\n")

count17 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                            print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                            count += 1
                            count17 += 1
                            checkcount = "{}".format(listinput)
                            if checkcount not in countlist:
                                countlist.append(checkcount)
                            else:
                                continue
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
    else:
        continue
print("There are", count17, "values in this operation.\n")

count18 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn2(listinput[1], listinput[2]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                                count += 1
                                count18 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count18, "values in this operation.\n")

count19 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")",
                                      operator3, listinput[3], ")")
                                count += 1
                                count19 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count19, "values in this operation.\n")

count20 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[2] == fixnumber:
        if listinput[0] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                            continue
                        elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2],
                                      operator3, listinput[3], ")", ")")
                                count += 1
                                count20 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count20, "values in this operation.\n")

count21 = 0
print("---------- ( X ? X ) ? X ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count21 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2],operator3, listinput[3])
                                    count += 1
                                    count21 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count21 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count21, "values in this operation.\n")

count22 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop3 = "{}".format(operator3)
                        if (checkop1 == "*" and checkop3 == "+") or (checkop1 == "*" and checkop3 == "-") or (checkop1 == "/" and checkop3 == "+") or (checkop1 == "/" and checkop3 == "-"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count22 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop3 == "*") or (checkop1 == "+" and checkop3 == "/") or (checkop1 == "-" and checkop3 == "*") or (checkop1 == "-" and checkop3 == "/"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count22 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count22 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count22, "values in this operation.\n")

count23 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count23 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count23 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count23 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count23, "values in this operation.\n")

count24 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                                count += 1
                                count24 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count24, "values in this operation.\n")

count25 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count25 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count25 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count25 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count25, "values in this operation.\n")

count26 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count26 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count26 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count26 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count26, "values in this operation.\n")

count27 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                            print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                            count += 1
                            count27 += 1
                            checkcount = "{}".format(listinput)
                            if checkcount not in countlist:
                                countlist.append(checkcount)
                            else:
                                continue
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
    else:
        continue
print("There are", count27, "values in this operation.\n")

count28 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn2(listinput[1], listinput[2]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                                count += 1
                                count28 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count28, "values in this operation.\n")

count29 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")",
                                      operator3, listinput[3], ")")
                                count += 1
                                count29 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count29, "values in this operation.\n")

count30 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[2] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[1] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                            continue
                        elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2],
                                      operator3, listinput[3], ")", ")")
                                count += 1
                                count30 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count30, "values in this operation.\n")

count31 = 0
print("---------- ( X ? X ) ? X ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count31 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2],operator3, listinput[3])
                                    count += 1
                                    count31 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count31 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count31, "values in this operation.\n")

count32 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop3 = "{}".format(operator3)
                        if (checkop1 == "*" and checkop3 == "+") or (checkop1 == "*" and checkop3 == "-") or (checkop1 == "/" and checkop3 == "+") or (checkop1 == "/" and checkop3 == "-"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count32 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop3 == "*") or (checkop1 == "+" and checkop3 == "/") or (checkop1 == "-" and checkop3 == "*") or (checkop1 == "-" and checkop3 == "/"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count32 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count32 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count32, "values in this operation.\n")

count33 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count33 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count33 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count33 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count33, "values in this operation.\n")

count34 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                                count += 1
                                count34 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count34, "values in this operation.\n")

count35 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count35 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count35 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count35 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count35, "values in this operation.\n")

count36 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count36 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count36 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count36 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count36, "values in this operation.\n")

count37 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                            print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                            count += 1
                            count37 += 1
                            checkcount = "{}".format(listinput)
                            if checkcount not in countlist:
                                countlist.append(checkcount)
                            else:
                                continue
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
    else:
        continue
print("There are", count37, "values in this operation.\n")

count38 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn2(listinput[1], listinput[2]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                                count += 1
                                count38 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count38, "values in this operation.\n")

count39 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")",
                                      operator3, listinput[3], ")")
                                count += 1
                                count39 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count39, "values in this operation.\n")

count40 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[3] == fixnumber:
        if listinput[1] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                            continue
                        elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2],
                                      operator3, listinput[3], ")", ")")
                                count += 1
                                count40 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count40, "values in this operation.\n")

count41 = 0
print("---------- ( X ? X ) ? X ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count41 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2],operator3, listinput[3])
                                    count += 1
                                    count41 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count41 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count41, "values in this operation.\n")

count42 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop3 = "{}".format(operator3)
                        if (checkop1 == "*" and checkop3 == "+") or (checkop1 == "*" and checkop3 == "-") or (checkop1 == "/" and checkop3 == "+") or (checkop1 == "/" and checkop3 == "-"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count42 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop3 == "*") or (checkop1 == "+" and checkop3 == "/") or (checkop1 == "-" and checkop3 == "*") or (checkop1 == "-" and checkop3 == "/"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count42 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count42 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count42, "values in this operation.\n")

count43 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count43 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count43 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count43 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count43, "values in this operation.\n")

count44 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                                count += 1
                                count44 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count44, "values in this operation.\n")

count45 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count45 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count45 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count45 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count45, "values in this operation.\n")

count46 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count46 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count46 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count46 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count46, "values in this operation.\n")

count47 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                            print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                            count += 1
                            count47 += 1
                            checkcount = "{}".format(listinput)
                            if checkcount not in countlist:
                                countlist.append(checkcount)
                            else:
                                continue
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
    else:
        continue
print("There are", count47, "values in this operation.\n")

count48 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn2(listinput[1], listinput[2]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                                count += 1
                                count48 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count48, "values in this operation.\n")

count49 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")",
                                      operator3, listinput[3], ")")
                                count += 1
                                count49 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count49, "values in this operation.\n")

count50 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[2] == fixnumber:
        if listinput[1] != fixnumber and listinput[3] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                            continue
                        elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2],
                                      operator3, listinput[3], ")", ")")
                                count += 1
                                count50 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count50, "values in this operation.\n")

count51 = 0
print("---------- ( X ? X ) ? X ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count51 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2],operator3, listinput[3])
                                    count += 1
                                    count51 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], operator3, listinput[3])
                                count += 1
                                count51 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count51, "values in this operation.\n")

count52 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop3 = "{}".format(operator3)
                        if (checkop1 == "*" and checkop3 == "+") or (checkop1 == "*" and checkop3 == "-") or (checkop1 == "/" and checkop3 == "+") or (checkop1 == "/" and checkop3 == "-"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count52 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop3 == "*") or (checkop1 == "+" and checkop3 == "/") or (checkop1 == "-" and checkop3 == "*") or (checkop1 == "-" and checkop3 == "/"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count52 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count52 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count52, "values in this operation.\n")

count53 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count53 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count53 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            else:
                                if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, listinput[1], operator2, "(", listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count53 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count53, "values in this operation.\n")

count54 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn2(fn1(listinput[0], listinput[1]), fn3(listinput[2], listinput[3])) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], ")", operator2, "(", listinput[2], operator3, listinput[3], ")")
                                count += 1
                                count54 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count54, "values in this operation.\n")

count55 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if (checkop1 == "*" and checkop2 == "+") or (checkop1 == "*" and checkop2 == "-") or (checkop1 == "/" and checkop2 == "+") or (checkop1 == "/" and checkop2 == "-"):
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count55 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
                                listinput.sort()
                                checkset = "{}".format(listinput)
                                if checkset not in setlist:
                                    setlist.append(checkset)
                                else:
                                    continue
                            else:
                                continue
                        elif (checkop1 == "+" and checkop2 == "*") or (checkop1 == "+" and checkop2 == "/") or (checkop1 == "-" and checkop2 == "*") or (checkop1 == "-" and checkop2 == "/"):
                            if fn2(listinput[1], listinput[2]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                    print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                    count += 1
                                    count55 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, listinput[1], operator2, listinput[2], ")", operator3, listinput[3])
                                count += 1
                                count55 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count55, "values in this operation.\n")

count56 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        checkop3 = "{}".format(operator3)
                        if (checkop2 == "*" and checkop3 == "+") or (checkop2 == "*" and checkop3 == "-") or (checkop2 == "/" and checkop3 == "+") or (checkop2 == "/" and checkop3 == "-"):
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count56 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        elif (checkop2 == "+" and checkop3 == "*") or (checkop2 == "+" and checkop3 == "/") or (checkop2 == "-" and checkop3 == "*") or (checkop2 == "-" and checkop3 == "/"):
                            if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                                continue
                            elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count56 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
                                    listinput.sort()
                                    checkset = "{}".format(listinput)
                                    if checkset not in setlist:
                                        setlist.append(checkset)
                                    else:
                                        continue
                                else:
                                    continue
                        else:
                            if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop1 == "/":
                                continue
                            else:
                                if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                    print(listinput[0], operator1, "(", listinput[1], operator2, listinput[2], operator3, listinput[3], ")")
                                    count += 1
                                    count56 += 1
                                    checkcount = "{}".format(listinput)
                                    if checkcount not in countlist:
                                        countlist.append(checkcount)
                                    else:
                                        continue
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
    else:
        continue
print("There are", count56, "values in this operation.\n")

count57 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        if fn3(fn2(fn1(listinput[0], listinput[1]), listinput[2]), listinput[3]) == ansnumber:
                            print("(", "(", listinput[0], operator1, listinput[1], ")", operator2, listinput[2], ")", operator3, listinput[3])
                            count += 1
                            count57 += 1
                            checkcount = "{}".format(listinput)
                            if checkcount not in countlist:
                                countlist.append(checkcount)
                            else:
                                continue
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
    else:
        continue
print("There are", count57, "values in this operation.\n")

count58 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn2(listinput[1], listinput[2]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn3(fn1(listinput[0], fn2(listinput[1], listinput[2])), listinput[3]) == ansnumber:
                                print("(", listinput[0], operator1, "(", listinput[1], operator2, listinput[2], ")", ")", operator3, listinput[3])
                                count += 1
                                count58 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count58, "values in this operation.\n")

count59 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop = "{}".format(operator1)
                        if fn3(fn2(listinput[1], listinput[2]), listinput[3]) == 0 and checkop == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn3(fn2(listinput[1], listinput[2]), listinput[3])) == ansnumber:
                                print(listinput[0], operator1, "(", "(", listinput[1], operator2, listinput[2], ")",
                                      operator3, listinput[3], ")")
                                count += 1
                                count59 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count59, "values in this operation.\n")

count60 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[1] == fixnumber and listinput[3] == fixnumber:
        if listinput[0] != fixnumber and listinput[2] != fixnumber:
            for j in range(0, 4):
                for k in range(0, 4):
                    for m in range(0, 4):
                        operator1, fn1 = operators[j]
                        operator2, fn2 = operators[k]
                        operator3, fn3 = operators[m]
                        checkop1 = "{}".format(operator1)
                        checkop2 = "{}".format(operator2)
                        if fn3(listinput[2], listinput[3]) == 0 and checkop2 == "/":
                            continue
                        elif fn2(listinput[1], fn3(listinput[2], listinput[3])) == 0 and checkop1 == "/":
                            continue
                        else:
                            if fn1(listinput[0], fn2(listinput[1], fn3(listinput[2], listinput[3]))) == ansnumber:
                                print(listinput[0], operator1, "(", listinput[1], operator2, "(", listinput[2],
                                      operator3, listinput[3], ")", ")")
                                count += 1
                                count60 += 1
                                checkcount = "{}".format(listinput)
                                if checkcount not in countlist:
                                    countlist.append(checkcount)
                                else:
                                    continue
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
    else:
        continue
print("There are", count60, "values in this operation.\n")

print("There are", count, "values in total operation.")

print("There are", len(setlist), "sets of number that can be 24.")
setlist.sort()
for i in setlist:
    for j in i:
        print(j, end="")
    print()

print("\nThere are", len(countlist), "arrays of number.")
countlist.sort()
for i in countlist:
    for j in i:
        print(j, end="")
    print()
