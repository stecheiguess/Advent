FILE = "inputs/02.txt"

cubes = {
    "r": 12,
    "g": 13,
    "b": 14,
}

# ===================== P1

with open(FILE, "r") as file:
    lines = file.readlines()
    flags = [True] * len(lines)
    for l in range(len(lines)):
        line = lines[l].split()
        for i in range(len(line)):
            if line[i].isnumeric():
                if cubes[line[i+1][0]] < int(line[i]):
                    flags[l] = False

    total = 0
    for i in range(len(flags)):
        if flags[i]:
            total += i+1
    print(total)

# --------------------- P2: total number of cubes needed

with open(FILE, "r") as file:
    lines = file.readlines()
    total = 0
    for l in range(len(lines)):

        cubes2 = {
            "r": 0,
            "g": 0,
            "b": 0,
        }

        line = lines[l].split()
        for i in range(len(line)):
            if line[i].isnumeric():
                if cubes2[line[i+1][0]] < int(line[i]):
                    cubes2[line[i+1][0]] = int(line[i])

        total += cubes2["r"] * cubes2["g"] * cubes2["b"]

    print(total)
