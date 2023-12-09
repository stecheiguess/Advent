FILE = "inputs/09.txt"


def after(list):
    q = []
    if list.count(0) == len(list):
        return 0
    for i in range(len(list)):
        if i == 0:
            continue
        q.append(list[i]-list[i-1])

    return(list[-1] + after(q))


with open(FILE, "r") as file:
    lines = file.readlines()
    lines = [[int(y) for y in x] for x in [x.split() for x in lines]]

    total = []
    for l in lines:
        total.append(after(l))

    print(sum(total))

# ----------------------- p2


def before(list):
    q = []
    if list.count(0) == len(list):
        return 0
    for i in range(len(list)):
        if i == 0:
            continue
        q.append(list[i]-list[i-1])

    return(list[0] - before(q))


with open(FILE, "r") as file:
    lines = file.readlines()
    lines = [[int(y) for y in x] for x in [x.split() for x in lines]]

    total = []
    for l in lines:
        total.append(before(l))

    print(sum(total))
