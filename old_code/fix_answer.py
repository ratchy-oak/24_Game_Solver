import array as arr

fixnumber = int(input("Input number: "))
count = 0

rawinput = arr.array("i")
for i in range(1111, 10000):
    if "0" in str(i):
        continue
    else:
        rawinput.append(i)

count1 = 0
print("\nX1 + X2 + X3 + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] + listinput[1] + listinput[2] + listinput[3]) == fixnumber:
        count += 1
        count1 += 1
        print(listinput[0], "+", listinput[1], "+", listinput[2], "+", listinput[3])
    else:
        continue
print("This Operation Count :", count1)

count2 = 0
print("\n( ( X1 - X2 ) - X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) - listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count2 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "-", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count2)

count3 = 0
print("\n( X1 - ( X2  - X3 ) ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] - listinput[2])) - listinput[3]) == fixnumber:
        count += 1
        count3 += 1
        print("(", listinput[0], "-", "(", listinput[1], "-", listinput[2], ")", ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count3)

count4 = 0
print("\nX1 - ( ( X2 - X3 ) - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - ((listinput[1] - listinput[2]) - listinput[3])) == fixnumber:
        count += 1
        count4 += 1
        print(listinput[0], "-", "(", "(", listinput[1], "-", listinput[2], ")", "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count4)

count5 = 0
print("\nX1 - ( X2 - ( X3 - X4 ) )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - (listinput[1] - (listinput[2] - listinput[3]))) == fixnumber:
        count += 1
        count5 += 1
        print(listinput[0], "-", "(", listinput[1], "-", "(", listinput[2], "-", listinput[3], ")", ")")
    else:
        continue
print("This Operation Count :", count5)

count6 = 0
print("\n( X1 - X2 ) - ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) - (listinput[2] - listinput[3])) == fixnumber:
        count += 1
        count6 += 1
        print("(", listinput[0], "-", listinput[1], ")", "-", "(", listinput[2], "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count6)

count7 = 0
print("\nX1 * X2 * X3 * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] * listinput[1] * listinput[2] * listinput[3]) == fixnumber:
        count += 1
        count7 += 1
        print(listinput[0], "*", listinput[1], "*", listinput[2], "*", listinput[3])
    else:
        continue
print("This Operation Count :", count7)

count8 = 0
print("\n( ( X1 / X2 ) / X3 ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) / listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count8 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "/", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count8)

count9 = 0
print("\n( X1 / ( X2 / X3 ) ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / (listinput[1] / listinput[2])) / listinput[3]) == fixnumber:
        count += 1
        count9 += 1
        print("(", listinput[0], "/", "(", listinput[1], "/", listinput[2], ")", ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count9)

count10 = 0
print("\nX1 / ( ( X2 / X3 ) / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / ((listinput[1] / listinput[2]) / listinput[3])) == fixnumber:
        count += 1
        count10 += 1
        print(listinput[0], "/", "(", "(", listinput[1], "/", listinput[2], ")", "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count10)

count11 = 0
print("\nX1 / ( X2 / ( X3 / X4 ) )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / (listinput[1] / (listinput[2] / listinput[3]))) == fixnumber:
        count += 1
        count11 += 1
        print(listinput[0], "/", "(", listinput[1], "/", "(", listinput[2], "/", listinput[3], ")", ")")
    else:
        continue
print("This Operation Count :", count11)

count12 = 0
print("\n( X1 / X2 ) / ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) / (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count12 += 1
        print("(", listinput[0], "/", listinput[1], ")", "/", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count12)

count13 = 0
print("\n( X1 + X2 + X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1] + listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count13 += 1
        print("(", listinput[0], "+", listinput[1], "+", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count13)

count14 = 0
print("\nX1 - ( X2 + X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - (listinput[1] + listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count14 += 1
        print(listinput[0], "-", "(", listinput[1], "+", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count14)

count15 = 0
print("\n( X1 - X2 ) + X3 + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) + listinput[2] + listinput[3]) == fixnumber:
        count += 1
        count15 += 1
        print("(", listinput[0], "-", listinput[1], ")", "+", listinput[2], "+", listinput[3])
    else:
        continue
print("This Operation Count :", count15)

count16 = 0
print("\n( X1 + X2 ) - ( X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1]) - (listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count16 += 1
        print("(", listinput[0], "+", listinput[1], ")", "-", "(", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count16)

count17 = 0
print("\n( ( X1 - X2 ) - X3 ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) - listinput[2]) + listinput[3]) == fixnumber:
        count += 1
        count17 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "-", listinput[2], ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count17)

count18 = 0
print("\n( X1 - ( X2 - X3 ) ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] - listinput[2])) + listinput[3]) == fixnumber:
        count += 1
        count18 += 1
        print("(", listinput[0], "-", "(", listinput[1], "-", listinput[2], ")", ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count18)

count19 = 0
print("\n( ( X1 + X2 ) - X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] + listinput[1]) - listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count19 += 1
        print("(", "(", listinput[0], "+", listinput[1], ")", "-", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count19)

count20 = 0
print("\n( X1 - ( X2 + X3 ) ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] + listinput[2])) - listinput[3]) == fixnumber:
        count += 1
        count20 += 1
        print("(", listinput[0], "-", "(", listinput[1], "+", listinput[2], ")", ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count20)

count21 = 0
print("\nX1 - ( ( X2 + X3 ) - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - ((listinput[1] + listinput[2]) - listinput[3])) == fixnumber:
        count += 1
        count21 += 1
        print(listinput[0], "-", "(", "(", listinput[1], "+", listinput[2], ")", "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count21)

count22 = 0
print("\nX1 - ( X2 - ( X3 + X4 ) )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - (listinput[1] - (listinput[2] + listinput[3]))) == fixnumber:
        count += 1
        count22 += 1
        print(listinput[0], "-", "(", listinput[1], "-", "(", listinput[2], "+", listinput[3], ")", ")")
    else:
        continue
print("This Operation Count :", count22)

count23 = 0
print("\n( ( X1 - X2 ) + X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) + listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count23 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "+", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count23)

count24 = 0
print("\nX1 - ( ( X2 - X3 ) + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - ((listinput[1] - listinput[2]) + listinput[3])) == fixnumber:
        count += 1
        count24 += 1
        print(listinput[0], "-", "(", "(", listinput[1], "-", listinput[2], ")", "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count24)

count25 = 0
print("\n( X1 + X2 ) - ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1]) - (listinput[2] - listinput[3])) == fixnumber:
        count += 1
        count25 += 1
        print("(", listinput[0], "+", listinput[1], ")", "-", "(", listinput[2], "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count25)

count26 = 0
print("\n( X1 - X2 ) + ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) + (listinput[2] - listinput[3])) == fixnumber:
        count += 1
        count26 += 1
        print("(", listinput[0], "-", listinput[1], ")", "+", "(", listinput[2], "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count26)

count27 = 0
print("\n( X1 * X2 * X3 ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1] * listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count27 += 1
        print("(", listinput[0], "*", listinput[1], "*", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count27)

count28 = 0
print("\nX1 / ( X2 * X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / (listinput[1] * listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count28 += 1
        print(listinput[0], "/", "(", listinput[1], "*", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count28)

count29 = 0
print("\n( X1 / X2 ) * X3 * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) * listinput[2] * listinput[3]) == fixnumber:
        count += 1
        count29 += 1
        print("(", listinput[0], "/", listinput[1], ")", "*", listinput[2], "*", listinput[3])
    else:
        continue
print("This Operation Count :", count29)

count30 = 0
print("\n( X1 * X2 ) / ( X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1]) / (listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count30 += 1
        print("(", listinput[0], "*", listinput[1], ")", "/", "(", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count30)

count31 = 0
print("\n( ( X1 / X2 ) / X3 ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) / listinput[2]) * listinput[3]) == fixnumber:
        count += 1
        count31 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "/", listinput[2], ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count31)

count32 = 0
print("\n( X1 / ( X2 / X3 ) ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / (listinput[1] / listinput[2])) * listinput[3]) == fixnumber:
        count += 1
        count32 += 1
        print("(", listinput[0], "/", "(", listinput[1], "/", listinput[2], ")", ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count32)

count33 = 0
print("\n( ( X1 * X2 ) / X3 ) / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] * listinput[1]) / listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count33 += 1
        print("(", "(", listinput[0], "*", listinput[1], ")", "/", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count33)

count34 = 0
print("\n( X1 / ( X2 * X3 ) ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / (listinput[1] * listinput[2])) / listinput[3]) == fixnumber:
        count += 1
        count34 += 1
        print("(", listinput[0], "/", "(", listinput[1], "*", listinput[2], ")", ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count34)

count35 = 0
print("\nX1 / ( ( X2 * X3 ) / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / ((listinput[1] * listinput[2]) / listinput[3])) == fixnumber:
        count += 1
        count35 += 1
        print(listinput[0], "/", "(", "(", listinput[1], "*", listinput[2], ")", "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count35)

count36 = 0
print("\nX1 / ( X2 / ( X3 * X4 ) )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / (listinput[1] / (listinput[2] * listinput[3]))) == fixnumber:
        count += 1
        count36 += 1
        print(listinput[0], "/", "(", listinput[1], "*", listinput[2], ")", "/", listinput[3], ")", ")")
    else:
        continue
print("This Operation Count :", count36)

count37 = 0
print("\n( ( X1 / X2 ) * X3 ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) * listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count37 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "*", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count37)

count38 = 0
print("\nX1 / ( ( X2 / X3 ) * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / ((listinput[1] / listinput[2]) * listinput[3])) == fixnumber:
        count += 1
        count38 += 1
        print(listinput[0], "/", "(", "(", listinput[1], "/", listinput[2], ")", "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count38)

count39 = 0
print("\n( X1 * X2 ) / ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1]) / (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count39 += 1
        print("(", listinput[0], "*", listinput[1], ")", "/", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count39)

count40 = 0
print("\n( X1 / X2 ) * ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) * (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count40 += 1
        print("(", listinput[0], "/", listinput[1], ")", "*", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count40)

count41 = 0
print("\n( ( X1 + X2 ) - X3 ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] + listinput[1]) - listinput[2]) * listinput[3]) == fixnumber:
        count += 1
        count41 += 1
        print("(", "(", listinput[0], "+", listinput[1], ")", "-", listinput[2], ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count41)

count42 = 0
print("\n( X1 - ( X2 + X3 ) ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] + listinput[2])) * listinput[3]) == fixnumber:
        count += 1
        count42 += 1
        print("(", listinput[0], "-", "(", listinput[1], "+", listinput[2], ")", ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count42)

count43 = 0
print("\n( ( X1 * X2 ) + X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] * listinput[1]) + listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count43 += 1
        print("(", "(", listinput[0], "*", listinput[1], ")", "+", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count43)

count44 = 0
print("\nX1 - ( ( X2 * X3 ) + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - ((listinput[1] * listinput[2]) + listinput[3])) == fixnumber:
        count += 1
        count44 += 1
        print(listinput[0], "-", "(", "(", listinput[1], "*", listinput[2], ")", "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count44)

count45 = 0
print("\n( ( X1 - X2 ) * X3 ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) * listinput[2]) + listinput[3]) == fixnumber:
        count += 1
        count45 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "*", listinput[2], ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count45)

count46 = 0
print("\n( ( X1 * X2 ) - X3 ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] * listinput[1]) - listinput[2]) + listinput[3]) == fixnumber:
        count += 1
        count46 += 1
        print("(", "(", listinput[0], "*", listinput[1], ")", "-", listinput[2], ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count46)

count47 = 0
print("\n( X1 - ( X2 * X3 ) ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] * listinput[2])) + listinput[3]) == fixnumber:
        count += 1
        count47 += 1
        print("(", listinput[0], "-", "(", listinput[1], "*", listinput[2], ")", ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count47)

count48 = 0
print("\n( X1 + X2 ) - ( X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1]) - (listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count48 += 1
        print("(", listinput[0], "+", listinput[1], ")", "-", "(", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count48)

count49 = 0
print("\n( X1 * X2 ) - ( X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1]) - (listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count49 += 1
        print("(", listinput[0], "*", listinput[1], ")", "-", "(", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count49)

count50 = 0
print("\n( X1 * X2 ) + ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1]) + (listinput[2] - listinput[3])) == fixnumber:
        count += 1
        count50 += 1
        print("(", listinput[0], "*", listinput[1], ")", "+", "(", listinput[2], "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count50)

count51 = 0
print("\n( X1 - X2 ) * ( X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) * (listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count51 += 1
        print("(", listinput[0], "-", listinput[1], ")", "*", "(", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count51)

count52 = 0
print("\n( ( X1 + X2 ) - X3 ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] + listinput[1]) - listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count52 += 1
        print("(", "(", listinput[0], "+", listinput[1], ")", "-", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count52)

count53 = 0
print("\n( X1 - ( X2 + X3 ) ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] + listinput[2])) / listinput[3]) == fixnumber:
        count += 1
        count53 += 1
        print("(", listinput[0], "-", "(", listinput[1], "+", listinput[2], ")", ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count53)

count54 = 0
print("\nX1 / ( ( X2 + X3 ) - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[1] + listinput[2]) - listinput[3]) != 0:
        if (listinput[0] / ((listinput[1] + listinput[2]) - listinput[3])) == fixnumber:
            count += 1
            count54 += 1
            print(listinput[0], "/", "(", "(", listinput[1], "+", listinput[2], ")", "-", listinput[3], ")")
        else:
            continue
    else:
        continue
print("This Operation Count :", count54)

count55 = 0
print("\nX1 / ( X2 - ( X3 + X4 ) )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[1] - (listinput[2] + listinput[3])) != 0:
        if (listinput[0] / (listinput[1] - (listinput[2] + listinput[3]))) == fixnumber:
            count += 1
            count55 += 1
            print(listinput[0], "/", "(", listinput[1], "-", "(", listinput[2], "+", listinput[3], ")", ")")
        else:
            continue
    else:
        continue
print("This Operation Count :", count55)

count56 = 0
print("\n( ( X1 / X2 ) + X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) + listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count56 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "+", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count56)

count57 = 0
print("\nX1 - ( ( X2 / X3 ) + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - ((listinput[1] / listinput[2]) + listinput[3])) == fixnumber:
        count += 1
        count57 += 1
        print(listinput[0], "-", "(", "(", listinput[1], "/", listinput[2], ")", "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count57)

count58 = 0
print("\n( ( X1 - X2 ) / X3 ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) / listinput[2]) + listinput[3]) == fixnumber:
        count += 1
        count58 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "/", listinput[2], ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count58)

count59 = 0
print("\n( X1 / ( X2 - X3 ) ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[1] - listinput[2]) != 0:
        if ((listinput[0] / (listinput[1] - listinput[2])) + listinput[3]) == fixnumber:
            count += 1
            count59 += 1
            print("(", listinput[0], "/", "(", listinput[1], "-", listinput[2], ")", ")", "+", listinput[3])
        else:
            continue
    else:
        continue
print("This Operation Count :", count59)

count60 = 0
print("\n( ( X1 / X2 ) - X3 ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) - listinput[2]) + listinput[3]) == fixnumber:
        count += 1
        count60 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "-", listinput[2], ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count60)

count61 = 0
print("\n( X1 - ( X2 / X3 ) ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] / listinput[2])) + listinput[3]) == fixnumber:
        count += 1
        count61 += 1
        print("(", listinput[0], "-", "(", listinput[1], "/", listinput[2], ")", ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count61)

count62 = 0
print("\n( X1 + X2 ) - ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1]) - (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count62 += 1
        print("(", listinput[0], "+", listinput[1], ")", "-", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count62)

count63 = 0
print("\n( X1 / X2 ) - ( X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) - (listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count63 += 1
        print("(", listinput[0], "/", listinput[1], ")", "-", "(", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count63)

count64 = 0
print("\n( X1 / X2 ) + ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) + (listinput[2] - listinput[3])) == fixnumber:
        count += 1
        count64 += 1
        print("(", listinput[0], "/", listinput[1], ")", "+", "(", listinput[2], "-", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count64)

count65 = 0
print("\n( X1 - X2 ) / ( X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) / (listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count65 += 1
        print("(", listinput[0], "-", listinput[1], ")", "/", "(", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count65)

count66 = 0
print("\n( X1 + X2 ) / ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[2] - listinput[3]) != 0:
        if ((listinput[0] + listinput[1]) / (listinput[2] - listinput[3])) == fixnumber:
            count += 1
            count66 += 1
            print("(", listinput[0], "+", listinput[1], ")", "/", "(", listinput[2], "-", listinput[3], ")")
        else:
            continue
    else:
        continue
print("This Operation Count :", count66)

count67 = 0
print("\n( ( X1 * X2 ) / X3 ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] * listinput[1]) / listinput[2]) + listinput[3]) == fixnumber:
        count += 1
        count67 += 1
        print("(", "(", listinput[0], "*", listinput[1], ")", "/", listinput[2], ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count67)

count68 = 0
print("\n( X1 / ( X2 * X3 ) ) + X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / (listinput[1] * listinput[2])) + listinput[3]) == fixnumber:
        count += 1
        count68 += 1
        print("(", listinput[0], "/", "(", listinput[1], "*", listinput[2], ")", ")", "+", listinput[3])
    else:
        continue
print("This Operation Count :", count68)

count69 = 0
print("\n( ( X1 + X2 ) * X3 ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] + listinput[1]) * listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count69 += 1
        print("(", "(", listinput[0], "+", listinput[1], ")", "*", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count69)

count70 = 0
print("\nX1 / ( ( X2 + X3 ) * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] / ((listinput[1] + listinput[2]) * listinput[3])) == fixnumber:
        count += 1
        count70 += 1
        print(listinput[0], "/", "(", "(", listinput[1], "+", listinput[2], ")", "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count70)

count71 = 0
print("\n( ( X1 / X2 ) + X3 ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) + listinput[2]) * listinput[3]) == fixnumber:
        count += 1
        count71 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "+", listinput[2], ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count71)

count72 = 0
print("\n( ( X1 + X2 ) / X3 ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] + listinput[1]) / listinput[2]) * listinput[3]) == fixnumber:
        count += 1
        count72 += 1
        print("(", "(", listinput[0], "+", listinput[1], ")", "/", listinput[2], ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count72)

count73 = 0
print("\n( X1 / ( X2 + X3 ) ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / (listinput[1] + listinput[2])) * listinput[3]) == fixnumber:
        count += 1
        count73 += 1
        print("(", listinput[0], "/", "(", listinput[1], "+", listinput[2], ")", ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count73)

count74 = 0
print("\n( X1 * X2 ) / ( X3 + X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1]) / (listinput[2] + listinput[3])) == fixnumber:
        count += 1
        count74 += 1
        print("(", listinput[0], "*", listinput[1], ")", "/", "(", listinput[2], "+", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count74)

count75 = 0
print("\n( X1 + X2 ) / ( X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1]) / (listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count75 += 1
        print("(", listinput[0], "+", listinput[1], ")", "/", "(", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count75)

count76 = 0
print("\n( X1 + X2 ) * ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] + listinput[1]) * (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count76 += 1
        print("(", listinput[0], "+", listinput[1], ")", "*", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count76)

count77 = 0
print("\n( X1 / X2 ) + ( X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) + (listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count77 += 1
        print("(", listinput[0], "/", listinput[1], ")", "+", "(", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count77)

count78 = 0
print("\n( ( X1 * X2 ) / X3 ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] * listinput[1]) / listinput[2]) - listinput[3]) == fixnumber:
        count += 1
        count78 += 1
        print("(", "(", listinput[0], "*", listinput[1], ")", "/", listinput[2], ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count78)

count79 = 0
print("\n( X1 / ( X2 * X3 ) ) - X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / (listinput[1] * listinput[2])) - listinput[3]) == fixnumber:
        count += 1
        count79 += 1
        print("(", listinput[0], "/", "(", listinput[1], "*", listinput[2], ")", ")", "-", listinput[3])
    else:
        continue
print("This Operation Count :", count79)

count80 = 0
print("\nX1 - ( ( X2 * X3 ) / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - ((listinput[1] * listinput[2]) / listinput[3])) == fixnumber:
        count += 1
        count80 += 1
        print(listinput[0], "-", "(", "(", listinput[1], "*", listinput[2], ")", "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count80)

count81 = 0
print("\nX1 - ( X2 / ( X3 * X4 ) )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[0] - (listinput[1] / (listinput[2] * listinput[3]))) == fixnumber:
        count += 1
        count81 += 1
        print(listinput[0], "-", "(", listinput[1], "/", "(", listinput[2], "*", listinput[3], ")", ")")
    else:
        continue
print("This Operation Count :", count81)

count82 = 0
print("\n( ( X1 - X2 ) * X3 ) / X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) * listinput[2]) / listinput[3]) == fixnumber:
        count += 1
        count82 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "*", listinput[2], ")", "/", listinput[3])
    else:
        continue
print("This Operation Count :", count82)

count83 = 0
print("\nX1 / ( ( X2 - X3 ) * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[1] - listinput[2]) * listinput[3]) != 0:
        if (listinput[0] / ((listinput[1] - listinput[2]) * listinput[3])) == fixnumber:
            count += 1
            count83 += 1
            print(listinput[0], "/", "(", "(", listinput[1], "-", listinput[2], ")", "*", listinput[3], ")")
        else:
            continue
    else:
        continue
print("This Operation Count :", count83)

count84 = 0
print("\n( ( X1 / X2 ) - X3 ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] / listinput[1]) - listinput[2]) * listinput[3]) == fixnumber:
        count += 1
        count84 += 1
        print("(", "(", listinput[0], "/", listinput[1], ")", "-", listinput[2], ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count84)

count85 = 0
print("\n( X1 - ( X2 / X3 ) ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - (listinput[1] / listinput[2])) * listinput[3]) == fixnumber:
        count += 1
        count85 += 1
        print("(", listinput[0], "-", "(", listinput[1], "/", listinput[2], ")", ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count85)

count86 = 0
print("\n( ( X1 - X2 ) / X3 ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (((listinput[0] - listinput[1]) / listinput[2]) * listinput[3]) == fixnumber:
        count += 1
        count86 += 1
        print("(", "(", listinput[0], "-", listinput[1], ")", "/", listinput[2], ")", "*", listinput[3])
    else:
        continue
print("This Operation Count :", count86)

count87 = 0
print("\n( X1 / ( X2 - X3 ) ) * X4")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[1] - listinput[2]) != 0:
        if ((listinput[0] / (listinput[1] - listinput[2])) * listinput[3]) == fixnumber:
            count += 1
            count87 += 1
            print("(", listinput[0], "/", "(", listinput[1], "-", listinput[2], ")", ")", "*", listinput[3])
        else:
            continue
    else:
        continue
print("This Operation Count :", count87)

count88 = 0
print("\n( X1 * X2 ) / ( X3 - X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if (listinput[2] - listinput[3]) != 0:
        if ((listinput[0] * listinput[1]) / (listinput[2] - listinput[3])) == fixnumber:
            count += 1
            count88 += 1
            print("(", listinput[0], "*", listinput[1], ")", "/", "(", listinput[2], "-", listinput[3], ")")
        else:
            continue
    else:
        continue
print("This Operation Count :", count88)

count89 = 0
print("\n( X1 - X2 ) / ( X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) / (listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count89 += 1
        print("(", listinput[0], "-", listinput[1], ")", "/", "(", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count89)

count90 = 0
print("\n( X1 - X2 ) * ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] - listinput[1]) * (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count90 += 1
        print("(", listinput[0], "-", listinput[1], ")", "*", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count90)

count91 = 0
print("\n( X1 / X2 ) - ( X3 * X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] / listinput[1]) - (listinput[2] * listinput[3])) == fixnumber:
        count += 1
        count91 += 1
        print("(", listinput[0], "/", listinput[1], ")", "-", "(", listinput[2], "*", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count91)

count92 = 0
print("\n( X1 * X2 ) - ( X3 / X4 )")
for i in range(0, 6561):
    listinput = [int(x) for x in str(rawinput[i])]
    if ((listinput[0] * listinput[1]) - (listinput[2] / listinput[3])) == fixnumber:
        count += 1
        count92 += 1
        print("(", listinput[0], "*", listinput[1], ")", "-", "(", listinput[2], "/", listinput[3], ")")
    else:
        continue
print("This Operation Count :", count92)

print("\nTotal Count :", count)
