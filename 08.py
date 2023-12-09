import math
FILE = "inputs/08.txt"

'''with open(FILE, "r") as file:
    lines = file.readlines()
    ins = lines[0].strip()
    ref = lines[2:]
    dic = {}

    for y in [x.split() for x in ref]:
        dic[y[0]] = (y[2][1:-1], y[3][:-1])

    current = "AAA"

    count = 0

    while current != "ZZZ":
        for i in range(len(ins)):
            if ins[i] == "L":
                current = dic[current][0]
            else:
                current = dic[current][1]
            count += 1

    print(count)'''

# --------------------------


def check(current):
    if current[-1] == "Z":
        return True
    return False


with open(FILE, "r") as file:
    lines = file.readlines()
    ins = lines[0].strip()
    ref = lines[2:]
    dic = {}

    for y in [x.split() for x in ref]:
        dic[y[0]] = (y[2][1:-1], y[3][:-1])

    fine = []

    for e in dic:
        if e[-1] == "A":
            fine.append(e)

    test = []

    for i in range(len(fine)):
        count = 0
        while True:
            flag = False

            for j in range(len(ins)):
                if ins[j] == "L":
                    fine[i] = dic[fine[i]][0]
                else:
                    fine[i] = dic[fine[i]][1]

                count += 1

                if check(fine[i]):
                    flag = True
                    break

            if flag:
                break

        test.append(int(count))


print(math.lcm(*test))
