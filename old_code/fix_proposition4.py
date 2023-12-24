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
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count1, "values in this operation.\n")

count2 = 0
print("---------- X ? ( X ? X ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count2, "values in this operation.\n")

count3 = 0
print("---------- X ? X ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count3, "values in this operation.\n")

count4 = 0
print("---------- ( X ? X ) ? ( X ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count4, "values in this operation.\n")

count5 = 0
print("---------- ( X ? X ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count5, "values in this operation.\n")

count6 = 0
print("---------- X ? ( X ? X ? X ) ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count6, "values in this operation.\n")

count7 = 0
print("---------- ( ( X ? X ) ? X ) ? X ----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count7, "values in this operation.\n")

count8 = 0
print("---------- ( X ? ( X ? X ) ) ? X -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count8, "values in this operation.\n")

count9 = 0
print("---------- X ? ( ( X ? X ) ? X ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count9, "values in this operation.\n")

count10 = 0
print("---------- X ? ( X ? ( X ? X ) ) -----------")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if listinput[0] == fixnumber and listinput[1] == fixnumber and listinput[2] == fixnumber and listinput[3] == fixnumber:
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
print("There are", count10, "values in this operation.\n")

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
