FILE = "inputs/06.txt"


with open(FILE, "r") as file:
    total = 1
    lines = file.readlines()

    t = [int(x) for x in lines[0].split()[1:]]
    d = [int(x) for x in lines[1].split()[1:]]

    for i in range(len(t)):
        j = 0
        races = 0
        while j <= t[i]:
            ans = j * (t[i]-j)
            if ans > d[i]:
                races += 1
            j += 1

        total *= races

    print(total)

# ------------------------

with open(FILE, "r") as file:
    total = 1
    lines = file.readlines()

    t = int(''.join(lines[0].split()[1:]))
    d = int(''.join(lines[1].split()[1:]))

    j = 0

    while j * (t-j) < d:
        j += 1
    print(t - j*2 + 1)
