import array as arr
import operator

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
count = 0

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
for j in range(0, 64):
    listoperator = [int(x) for x in str(rawoperator[j])]
    operator1, fn1 = operators[listoperator[0] - 1]
    operator2, fn2 = operators[listoperator[1] - 1]
    operator3, fn3 = operators[listoperator[2] - 1]
    print("(", operator1, ")", operator2, operator3)
    count += 1

print("There are", count, "operations.")
